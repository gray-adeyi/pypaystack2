from pathlib import Path
from unittest import TestCase

BASE_DIR = Path().parent

class VersionTestCase(TestCase):
    def test_package_version(self):
        # TODO: package version in the `version.py` has to match the `pyproject.toml`
        ...