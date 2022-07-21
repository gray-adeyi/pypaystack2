from . import test_auth_key, Plan, TestCase
from pypaystack2.utils import Interval


class TestPlan(TestCase):
    def setUp(self):
        super(TestPlan, self).setUp()
        self.assertNotEqual(test_auth_key, None)
        self.plan = Plan(authorization_key=test_auth_key)

    def test_plan_setup_and_update(self):
        """
        Integration test for creating plan and updating created plan
        """

        initial_plan_detail = {
            "name": "test_plan_1",
            "amount": 1000 * 100,
            "interval": Interval.WEEKLY,
        }

        updated_plan_details = {
            "name": "test_plan_1",
            "amount": 300 * 100,
            "interval": Interval.DAILY,
        }

        def create_plan():
            (status_code, status, response_msg, created_plan_data) = self.plan.create(
                **initial_plan_detail
            )
            self.assertEqual(status_code, 201)
            self.assertEqual(status, True)
            self.assertEqual(response_msg, "Plan created")
            # assert if subset
            self.assertLessEqual(initial_plan_detail.items(), created_plan_data.items())
            return created_plan_data

        def update_plan():
            (status_code, status, response_msg, updated_plan_data) = self.plan.update(
                plan_id=created_plan_data["id"], **updated_plan_details
            )
            self.assertEqual(status_code, 200)
            self.assertEqual(status, True)
            self.assertEqual(response_msg, "Plan updated. 0 subscription(s) affected")
            self.assertEqual(updated_plan_data, None)

        created_plan_data = create_plan()
        update_plan()
