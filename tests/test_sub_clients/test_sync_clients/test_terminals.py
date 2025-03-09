from unittest import TestCase, skip

from dotenv import load_dotenv

from pypaystack2.sub_clients import TerminalClient


class TerminalClientTestCase(TestCase):
    client: TerminalClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = TerminalClient()

    @skip("incomplete test")
    def test_can_send_event(self) -> None: ...

    @skip("incomplete test")
    def test_can_get_event_status(self) -> None: ...

    @skip("incomplete test")
    def test_can_get_terminal_status(self) -> None: ...

    @skip("incomplete test")
    def test_can_get_terminals(self) -> None: ...

    @skip("incomplete test")
    def test_can_get_terminal(self) -> None: ...

    @skip("incomplete test")
    def test_can_update_terminal(self) -> None: ...

    @skip("incomplete test")
    def test_can_commission_terminal(self) -> None: ...

    @skip("incomplete test")
    def test_can_decommission_terminal(self) -> None: ...
