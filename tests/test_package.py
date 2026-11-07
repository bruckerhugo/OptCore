"""Check that the development environment exposes the installed package."""

from importlib.metadata import version

import optcore


def test_package_is_installed() -> None:
    assert optcore.__name__ == "optcore"
    assert version("optcore")
