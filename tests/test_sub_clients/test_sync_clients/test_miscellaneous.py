from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients import MiscellaneousClient
from pypaystack2.utils.enums import Country
from pypaystack2.utils.response_models import Bank, PaystackSupportedCountry, State


class MiscellaneousTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = MiscellaneousClient()

    def test_can_get_banks(self):
        response = self.client.get_banks(country=Country.NIGERIA, pagination=1)
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Banks retrieved")
        self.assertIsInstance(response.data, list)
        if len(response.data) > 0:
            self.assertIsInstance(response.data[0], Bank)

    def test_can_get_countries(self):
        response = self.client.get_countries()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Countries retrieved")
        self.assertIsInstance(response.data, list)
        if len(response.data) > 0:
            self.assertIsInstance(response.data[0], PaystackSupportedCountry)

    def test_can_get_states(self):
        response = self.client.get_states(country="CA")
        self.assertEqual(response.message, "States retrieved")
        self.assertIsInstance(response.data, list)
        if len(response.data) > 0:
            self.assertIsInstance(response.data[0], State)
