from . import test_auth_key, ApplePay, TestCase
import uuid


class TestApplePay(TestCase):
    def setUp(self):
        super(TestApplePay, self).setUp()
        self.assertNotEqual(test_auth_key, None)
        self.apple_pay = ApplePay(authorization_key=test_auth_key)

    def test_apple_pay(self):
        """
        Integration test for getting all plans and getting single plan details
        """

        def register_domain():
            # This test will fail in test mode because of
            # missing .well-known/apple-developer-merchantid-domain-association
            # file in the domain.
            domain_name = f"example.com"
            print(domain_name)
            (status_code, status, response_msg, data) = self.apple_pay.register_domain(
                domain_name=domain_name
            )
            self.assertEqual(status_code, 200)
            self.assertEqual(status, True)
            self.assertEqual(
                response_msg, "Domain successfully registered on Apple Pay"
            )
            self.assertIsInstance(data, None)

        def list_domains():
            (status_code, status, response_msg, domains) = self.apple_pay.list_domains()
            self.assertEqual(status_code, 200)
            self.assertEqual(status, True)
            self.assertEqual(response_msg, "Apple Pay registered domains retrieved")
            return domains

        def unregister_domain(domain_name):
            print(domain_name)
            (
                status_code,
                status,
                response_msg,
                data,
            ) = self.apple_pay.unregister_domain(domain_name)
            print(response_msg)
            self.assertEqual(status_code, 200)
            self.assertEqual(status, True)
            self.assertEqual(
                response_msg, "Domain successfully unregistered on Apple Pay"
            )
            self.assertIsNone(data)

        # register_domain()
        domains = list_domains()
        unregister_domain("example.com")
