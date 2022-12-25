class PyPaystackError(Exception):
    """
    Python Paystack Error
    """

    pass


class MissingAuthKeyError(PyPaystackError):
    """
    We can't find the authentication key
    """

    pass


class InvalidMethodError(PyPaystackError):
    """
    Invalid or unrecognized/unimplemented HTTP request method
    """

    pass


class InvalidDataError(PyPaystackError):
    """
    Invalid input recognised. Saves unnecessary request to the server
    """

    pass
