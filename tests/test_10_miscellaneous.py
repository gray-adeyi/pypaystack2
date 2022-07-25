from urllib import response
from . import test_auth_key, Miscellaneous, TestCase
from pypaystack2.utils import Country


class TestMiscellaneous(TestCase):
    def setUp(self):
        super().setUp()
        self.assertNotEqual(test_auth_key, None)
        self.misc = Miscellaneous(auth_key=test_auth_key)

    def test_can_get_banks(self):
        response = self.misc.get_banks(country=Country.NIGERIA)
        self.assertTrue(response.status)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.message, "Banks retrieved")

    def test_can_get_providers(self):
        response = self.misc.get_providers()
        self.assertTrue(response.status)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.message, "Banks retrieved")

    def test_can_get_states(self):
        response = self.misc.get_states(country=Country.NIGERIA)
        self.assertEqual(response.message, "")
        self.assertTrue(response.status)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.message, "Banks retrieved")
