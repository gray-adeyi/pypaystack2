from pathlib import Path
from unittest import TestCase, skip

import tomli

from pypaystack2 import __title__, __version__, __author__, __license__

BASE_DIR = Path().parent


class PackageMetadataTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        with (BASE_DIR / "pyproject.toml").open("r") as f:
            cls.pyproject_data = tomli.loads(f.read())

    def test_package_title(self) -> None:
        self.assertEqual(
            self.pyproject_data["project"]["name"],
            __title__,
            "Mismatched package name",
        )

    @skip("Package version is now dynamic")
    def test_package_version(self) -> None:
        self.assertEqual(
            self.pyproject_data["project"]["version"],
            __version__,
            "Mismatched package version",
        )

    def test_package_author(self) -> None:
        self.assertListEqual(
            self.pyproject_data["project"]["authors"],
            __author__,
            "Mismatched package authors",
        )

    def test_package_license(self) -> None:
        self.assertEqual(
            self.pyproject_data["project"]["license"],
            __license__,
            "Mismatched package license",
        )
