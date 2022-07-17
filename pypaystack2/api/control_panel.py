from typing import Mapping, Optional

from pypaystack2.errors import InvalidDataError
from .baseapi import BaseAPI
from . import utils
from .utils import ChargeStatus, TRType, add_to_payload, append_query_params


class ControlPanel(BaseAPI):
    """
    The Control Panel API allows
    you manage some settings on
    your integration
    """

    def get_payment_session_timeout(self):
        """ """
        url = self._url("/integration/payment_session_timeout")
        return self._handle_request("GET", url)

    def update_payment_session_timeout(self, timeout: int):
        """ """
        payload = {"timeout": timeout}
        url = self._url("/integration/payment_session_timeout")
        return self._handle_request("PUT", url, payload)
