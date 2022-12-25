from pypaystack2.api import ApplePay
from tests.tests_with_mocked_requests.mocked_request_testcase import (
    MockedRequestTestCase,
)


class ApplePayTestCase(MockedRequestTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.apple_pay = ApplePay(auth_key="test_key")

    def test_register_domain(self):
        response = self.apple_pay.register_domain(domain_name="jigani.com")
        self.assert_is_mocked_response(response)

    def test_get_domains(self):
        response = self.apple_pay.get_domains()
        self.assert_is_mocked_response(response)

    def test_unregister_domain(self):
        response = self.apple_pay.unregister_domain(domain_name="jigani.com")
        self.assert_is_mocked_response(response)
