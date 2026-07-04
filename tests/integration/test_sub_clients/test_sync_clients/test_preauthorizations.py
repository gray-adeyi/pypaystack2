from dotenv import load_dotenv
from unittest import TestCase
from pypaystack2.sub_clients.sync_clients.preauthorizations import (
    PreauthorizationClient,
)


class PreauthorizationClientTestCase(TestCase):
    client: PreauthorizationClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = PreauthorizationClient()
