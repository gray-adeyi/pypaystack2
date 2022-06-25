from . import test_auth_key, uuid4, Customer, TestCase


class TestCustomer(TestCase):
    def setUp(self):
        super(TestCustomer, self).setUp()
        self.assertNotEqual(test_auth_key, None)
        self.customer = Customer(authorization_key=test_auth_key)

    def test_customer_setup_and_update(self):
        """
        Integration test for creating customer and updating created customer details
        """
        # using random generator for email id to ensure email is unique, thus ensuring success on retests
        user_email = f"{uuid4()}@mail.com"
        user_details = {"email": user_email,
                        "first_name": "Test",
                        "last_name": "Customer",
                        "phone": "08012345678"}
        updated_user_details = {
            "email": user_email,
            "first_name": "Updated",
            "last_name": "Customer",
            "phone": "080987654321"}

        def create_customer():
            (status_code, status, response_msg,
             created_customer_data) = self.customer.create(**user_details)
            self.assertEqual(status_code, 200)
            self.assertEqual(status, True)
            self.assertEqual(response_msg, 'Customer created')
            # assert if subset
            self.assertLessEqual(
                user_details.items(), created_customer_data.items())
            return created_customer_data

        def update_customer():
            (status_code, status, response_msg, updated_customer_data) = self.customer.update(
                user_id=created_customer_data['id'], **updated_user_details)
            self.assertEqual(status_code, 200)
            self.assertEqual(status, True)
            self.assertEqual(response_msg, 'Customer updated')
            # assert if subset
            self.assertLessEqual(
                updated_user_details.items(), updated_customer_data.items())

        created_customer_data = create_customer()
        update_customer()
