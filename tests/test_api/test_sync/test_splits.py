from unittest import TestCase

from dotenv import load_dotenv

from pypaystack2.api import Split
from tests.test_api.mocked_api_testcase import MockedAPITestCase


class MockedSplitTestCase(MockedAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = Split()


class SplitTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = Split()

    def test_can_create(self):
        ...

    def test_can_get_splits(self):
        ...

    def test_can_get_split(self):
        ...

    def test_can_update(self):
        ...

    def test_can_add_or_update(self):
        ...

    def test_can_remove(self):
        ...
