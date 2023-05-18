from unittest import TestCase

from dotenv import load_dotenv

from pypaystack2.api import Terminal
from tests.test_api.mocked_api_testcase import MockedAPITestCase


class MockedTerminalTestCase(MockedAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = Terminal()


class TerminalTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = Terminal()

    def test_can_send_event(self):
        ...

    def test_can_get_event_status(self):
        ...

    def test_can_get_terminal_status(self):
        ...

    def test_can_get_terminals(self):
        ...

    def test_can_get_terminal(self):
        ...

    def test_can_update_terminal(self):
        ...

    def test_can_commission_terminal(self):
        ...

    def test_can_decommission_terminal(self):
        ...
