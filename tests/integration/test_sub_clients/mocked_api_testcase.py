from unittest import TestCase, IsolatedAsyncioTestCase
from unittest.mock import Mock, patch

import httpx


class TestDummyData:
    @classmethod
    def setUpClass(cls) -> None:
        cls.mocked_api_response = Mock(spec="httpx.Response")
        cls.mocked_api_response.status_code = httpx.codes.OK
        cls.mocked_api_response.json = Mock()
        cls.mocked_api_response.json.return_value = {
            "status": True,
            "message": "This is a mocked response. No real API call to Paystack servers was made.",
            "data": {"isValid": True},
        }


class MockedAPITestCase(TestDummyData, TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.get_patcher = patch("httpx.get")
        cls.post_patcher = patch("httpx.post")
        cls.put_patcher = patch("httpx.put")
        cls.patch_patcher = patch("httpx.patch")
        cls.delete_patcher = patch("httpx.delete")
        cls.options_patcher = patch("httpx.options")
        cls.head_patcher = patch("httpx.head")

        mock_get = cls.get_patcher.start()
        mock_get.return_value = cls.mocked_api_response

        mock_post = cls.post_patcher.start()
        mock_post.return_value = cls.mocked_api_response

        mock_put = cls.put_patcher.start()
        mock_put.return_value = cls.mocked_api_response

        mock_patch = cls.patch_patcher.start()
        mock_patch.return_value = cls.mocked_api_response

        mock_delete = cls.delete_patcher.start()
        mock_delete.return_value = cls.mocked_api_response

        mock_options = cls.options_patcher.start()
        mock_options.return_value = cls.mocked_api_response

        mock_head = cls.head_patcher.start()
        mock_head.return_value = cls.mocked_api_response

    @classmethod
    def tearDownClass(cls) -> None:
        cls.get_patcher.stop()
        cls.post_patcher.stop()
        cls.put_patcher.stop()
        cls.patch_patcher.stop()
        cls.delete_patcher.stop()
        cls.options_patcher.stop()
        cls.head_patcher.stop()


class MockedAsyncAPITestCase(TestDummyData, IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.get_patcher = patch("httpx._client.AsyncClient.get")
        cls.post_patcher = patch("httpx._client.AsyncClient.post")
        cls.put_patcher = patch("httpx._client.AsyncClient.put")
        cls.patch_patcher = patch("httpx._client.AsyncClient.patch")
        cls.delete_patcher = patch("httpx._client.AsyncClient.delete")
        cls.options_patcher = patch("httpx._client.AsyncClient.options")
        cls.head_patcher = patch("httpx._client.AsyncClient.head")

        mock_get = cls.get_patcher.start()
        mock_get.return_value = cls.mocked_api_response

        mock_post = cls.post_patcher.start()
        mock_post.return_value = cls.mocked_api_response

        mock_put = cls.put_patcher.start()
        mock_put.return_value = cls.mocked_api_response

        mock_patch = cls.patch_patcher.start()
        mock_patch.return_value = cls.mocked_api_response

        mock_delete = cls.delete_patcher.start()
        mock_delete.return_value = cls.mocked_api_response

        mock_options = cls.options_patcher.start()
        mock_options.return_value = cls.mocked_api_response

        mock_head = cls.head_patcher.start()
        mock_head.return_value = cls.mocked_api_response

    @classmethod
    def tearDownClass(cls) -> None:
        cls.get_patcher.stop()
        cls.post_patcher.stop()
        cls.put_patcher.stop()
        cls.patch_patcher.stop()
        cls.delete_patcher.stop()
        cls.options_patcher.stop()
        cls.head_patcher.stop()
