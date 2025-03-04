from unittest import skip
from unittest.async_case import IsolatedAsyncioTestCase

from dotenv import load_dotenv

from pypaystack2.sub_clients import AsyncTerminalClient


class AsyncTerminalTestCase(IsolatedAsyncioTestCase):
    client: AsyncTerminalClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = AsyncTerminalClient()

    @skip("incomplete test")
    async def test_can_send_event(self) -> None: ...

    @skip("incomplete test")
    async def test_can_get_event_status(self) -> None: ...

    @skip("incomplete test")
    async def test_can_get_terminal_status(self) -> None: ...

    @skip("incomplete test")
    async def test_can_get_terminals(self) -> None: ...

    @skip("incomplete test")
    async def test_can_get_terminal(self) -> None: ...

    @skip("incomplete test")
    async def test_can_update_terminal(self) -> None: ...

    @skip("incomplete test")
    async def test_can_commission_terminal(self) -> None: ...

    @skip("incomplete test")
    async def test_can_decommission_terminal(self) -> None: ...
