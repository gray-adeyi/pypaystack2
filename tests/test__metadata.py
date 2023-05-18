from pathlib import Path
from unittest import TestCase

import tomli
from pypaystack2 import __title__, __version__, __author__, __license__

BASE_DIR = Path().parent


class PackageMetadataTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        with (BASE_DIR / "pyproject.toml").open("r") as f:
            cls.pyproject_data = tomli.loads(f.read())

    def test_package_title(self):
        self.assertEqual(
            self.pyproject_data["tool"]["poetry"]["name"],
            __title__,
            "Mismatched package name",
        )

    def test_package_version(self):
        self.assertEqual(
            self.pyproject_data["tool"]["poetry"]["version"],
            __version__,
            "Mismatched package version",
        )

    def test_package_author(self):
        self.assertListEqual(
            self.pyproject_data["tool"]["poetry"]["authors"],
            __author__,
            "Mismatched package authors",
        )

    def test_package_license(self):
        self.assertEqual(
            self.pyproject_data["tool"]["poetry"]["license"],
            __license__,
            "Mismatched package license",
        )
