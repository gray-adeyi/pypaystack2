from unittest import TestCase

from dotenv import load_dotenv

from pypaystack2.sub_clients.sync_clients.webhook_events import WebhookEventClient


class WebhookEventClientTestCase(TestCase):
    client: WebhookEventClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = WebhookEventClient()

    def test_can_retrieve_all_webhook_events(self): ...
