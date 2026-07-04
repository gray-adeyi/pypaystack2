from pypaystack2.models import OrderLineItem
from dotenv import load_dotenv
from unittest import IsolatedAsyncioTestCase, skip
from pypaystack2.sub_clients.async_clients.orders import AsyncOrderClient


class AsyncOrderClientTestCase(IsolatedAsyncioTestCase):
    client: AsyncOrderClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = AsyncOrderClient()

    @skip("bypass")
    async def test_create(self):
        line_items = [
            OrderLineItem.model_validate(item)
            for item in [{"product": "1209661", "quantity": 1}]
        ]
        response = await self.client.create(
            "CUS_kul59mkqwd0rn16", line_items=line_items
        )
        print(response)
