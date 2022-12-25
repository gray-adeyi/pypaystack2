from unittest import TestCase
from unittest.mock import patch

from pypaystack2.baseapi import Response


class MockedRequestTestCase(TestCase):
    def setUp(self) -> None:
        handle_request_patcher = patch("pypaystack2.baseapi.BaseAPI._handle_request")
        self.handle_request_mock = handle_request_patcher.start()
        self.handle_request_mock.return_value = Response(
            status_code=200,
            status=True,
            message="Test Okay",
            data={"data": "test data"},
        )

    def assert_is_mocked_response(self, response: Response):
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.status, True)
        self.assertEqual(response.message, "Test Okay")
        self.assertDictEqual(response.data, {"data": "test data"})
