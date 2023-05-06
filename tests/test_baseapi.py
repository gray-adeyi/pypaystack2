from unittest import TestCase


class BaseAPITestCase(TestCase):

    def test_raises_exception_for_missing_key(self):
        ...

    def test__parse_url(self):
        ...

    def test__headers(self):
        ...

    def test__parse_response(self):
        ...
    def test__handle_request(self):
        ...


class BaseAsyncAPITestCase(TestCase):

    def test_raises_exception_for_missing_key(self):
        ...

    def test__parse_url(self):
        ...

    def test__headers(self):
        ...

    def test__parse_response(self):
        ...

    def test__handle_request(self):
        ...
