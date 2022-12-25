from pypaystack2.api import BulkCharge
from tests.tests_with_mocked_requests.mocked_request_testcase import (
    MockedRequestTestCase,
)


class BulkChargeTestCase(MockedRequestTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.bulk_charge = BulkCharge(auth_key="test_key")

    def test_initiate(self):
        response = self.bulk_charge.initiate(body=[{"data": "test value"}])
        self.assert_is_mocked_response(response)

    def test_get_batches(self):
        response = self.bulk_charge.get_batches()
        self.assert_is_mocked_response(response)

    def test_get_batch(self):
        response = self.bulk_charge.get_batch(id_or_code="test_id")
        self.assert_is_mocked_response(response)
