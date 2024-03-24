class MissingAuthKeyException(Exception):
    """
    We can't find the authentication key
    """

    pass


class InvalidMethodException(Exception):
    """
    Invalid or unrecognized/unimplemented HTTP request method
    """

    pass


class InvalidDataException(Exception):
    """
    Invalid input recognized. Saves unnecessary request to the server
    """

    pass
