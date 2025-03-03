from unittest.async_case import IsolatedAsyncioTestCase

from dotenv import load_dotenv

from pypaystack2.sub_clients.async_clients.terminals import AsyncTerminalClient


class AsyncTerminalTestCase(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = AsyncTerminalClient()

    async def test_can_send_event(self): ...

    async def test_can_get_event_status(self): ...

    async def test_can_get_terminal_status(self): ...

    async def test_can_get_terminals(self): ...

    async def test_can_get_terminal(self): ...

    async def test_can_update_terminal(self): ...

    async def test_can_commission_terminal(self): ...

    async def test_can_decommission_terminal(self): ...
