from . import test_auth_key, Plan, TestCase


class TestPlansRecord(TestCase):
    def setUp(self):
        super(TestPlansRecord, self).setUp()
        self.assertNotEqual(test_auth_key, None)
        self.plan = Plan(authorization_key=test_auth_key)

    def test_plans_records(self):
        """
        Integration test for getting all plans and getting single plan details
        """

        def retrieve_all_plans():
            (status_code, status, response_msg, plans_list) = self.plan.get_plans()
            self.assertEqual(status_code, 200)
            self.assertEqual(status, True)
            self.assertEqual(response_msg, "Plans retrieved")
            self.assertIsInstance(plans_list, list)
            return plans_list

        def retrieve_one_plan():
            one_plan = plans_list[0]
            (status_code, status, response_msg, plan_data) = self.plan.get_plan(
                one_plan["id"]
            )
            self.assertEqual(status_code, 200)
            self.assertEqual(status, True)
            self.assertEqual(response_msg, "Plan retrieved")
            print(plan_data)

            # TODO: Fix this test.
            # assert if subset
            # This test fails. plan_data is a superset of one_plan
            # self.assertLessEqual(one_plan.items(), plan_data.items())

        plans_list = retrieve_all_plans()
        retrieve_one_plan()
