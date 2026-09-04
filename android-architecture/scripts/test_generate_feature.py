"""Run with python -B android-architecture/scripts/test_generate_feature.py."""

import contextlib
import io
import tempfile
from pathlib import Path
from unittest.mock import patch

from generate_feature import generate_feature_module, write_file


def main():
    snapshots = []
    for name in ("user-profile", "user_profile"):
        with tempfile.TemporaryDirectory(prefix="android-naming-test-") as directory:
            root = Path(directory)
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                generate_feature_module(name, "com.example.app", root)
            assert (root / "feature" / "userprofile").is_dir()
            files = {p.relative_to(root): p.read_text(encoding="utf-8")
                     for p in root.rglob("*") if p.is_file()}
            assert len(files) == 7
            for path, content in files.items():
                assert "user_profile" not in str(path)
                if path.suffix == ".kt":
                    assert content.startswith("package com.example.app.feature.userprofile.")
                    assert "UserProfile" in path.name
            assert 'include(":feature:userprofile:api")' in output.getvalue()
            assert 'include(":feature:userprofile:impl")' in output.getvalue()
            assert 'implementation(projects.feature.userprofile.impl)' in output.getvalue()
            # Keep the existing route string contract; only identifiers/paths normalize.
            snapshots.append({p: text.replace(f'"{name}"', '"<route>"')
                              for p, text in files.items()})
            other_name = "user_profile" if name == "user-profile" else "user-profile"
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    generate_feature_module(other_name, "com.example.app", root)
            except FileExistsError:
                pass
            else:
                raise AssertionError("Equivalent name bypassed module protection")
            assert files == {p.relative_to(root): p.read_text(encoding="utf-8")
                             for p in root.rglob("*") if p.is_file()}
    assert snapshots[0] == snapshots[1]
    with tempfile.TemporaryDirectory(prefix="android-feature-test-") as directory:
        root = Path(directory)
        with contextlib.redirect_stdout(io.StringIO()):
            generate_feature_module("user-profile", "com.example.app", root)
        files = {p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file()}
        assert len(files) == 7
        try:
            generate_feature_module("user-profile", "com.example.app", root)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Existing module was not rejected")
        assert files == {p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file()}
        # Model a feature parent redirected outside the project by a link/junction.
        original_resolve = Path.resolve

        def redirected_resolve(path, *args, **kwargs):
            if path == root / "feature" / "redirected":
                return root.parent / "outside-project" / "redirected"
            return original_resolve(path, *args, **kwargs)

        with patch.object(Path, "resolve", redirected_resolve):
            try:
                generate_feature_module("redirected", "com.example", root)
            except ValueError:
                pass
            else:
                raise AssertionError("Resolved target escaped the project")
        assert not (root / "feature" / "redirected").exists()

        target = root / next(iter(files))
        try:
            write_file(target, "must not overwrite")
        except FileExistsError:
            pass
        else:
            raise AssertionError("Existing file was overwritten")
        assert target.read_bytes() == files[target.relative_to(root)]

        for name, package in [
            ("../escape", "com.example"), ("/escape", "com.example"),
            ("C:\\escape", "com.example"), ("bad/name", "com.example"),
            ("", "com.example"), ("123", "com.example"),
            ("con", "com.example"), ("valid", "../../escape"),
            ("valid", "com/example"), ("valid", "com..example"),
        ]:
            try:
                generate_feature_module(name, package, root)
            except ValueError:
                pass
            else:
                raise AssertionError(f"Unsafe input accepted: {name!r}, {package!r}")
        assert files == {p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file()}
    print("PASS: equivalent naming, collision protection, generation, file preservation, invalid inputs, resolved-path boundary")


if __name__ == "__main__":
    main()
