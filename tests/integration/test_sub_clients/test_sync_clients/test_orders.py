from pypaystack2.models import OrderLineItem
from unittest import TestCase, skip
from dotenv import load_dotenv
from pypaystack2.sub_clients.sync_clients.orders import OrderClient


class OrderClientTestCase(TestCase):
    client: OrderClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = OrderClient()

    @skip("bypass")
    def test_create(self):
        line_items = [
            OrderLineItem.model_validate(item)
            for item in [{"product": "1209661", "quantity": 1}]
        ]
        response = self.client.create("CUS_kul59mkqwd0rn16", line_items=line_items)
        print(response)
