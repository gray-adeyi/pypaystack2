class MissingSecretKeyException(Exception):
    """
    We can't find the authentication key
    """

    pass


class InvalidDataException(Exception):
    """
    Invalid input recognized. Saves unnecessary request to the server
    """

    pass
