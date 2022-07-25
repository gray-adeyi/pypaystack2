from . import test_auth_key, ControlPanel, TestCase


class TestControlPanel(TestCase):
    def setUp(self):
        super().setUp()
        self.assertNotEqual(test_auth_key, None)
        self.control_panel = ControlPanel(auth_key=test_auth_key)

    def tearDown(self) -> None:
        super().tearDown()
        self.control_panel.update_payment_session_timeout(timeout=0)

    def test_can_get_payment_session_timeout(self):
        response = self.control_panel.get_payment_session_timeout()
        self.assertTrue(response.status)
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.data, {"payment_session_timeout": 0})
        self.assertEqual(response.message, "Payment session timeout retrieved")

    def test_can_update_payment_session_timeout(self):
        response = self.control_panel.update_payment_session_timeout(timeout=5)
        self.assertTrue(response.status)
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.data, {"payment_session_timeout": 5})
        self.assertEqual(response.message, "Payment session timeout updated")
