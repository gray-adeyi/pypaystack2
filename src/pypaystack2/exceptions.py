class MissingSecretKeyException(Exception):
    """Custom exception raised when we can't find the secret key"""

    ...


class ClientNetworkError(Exception):
    """Custom exception for wrapping httpx-related errors."""

    def __init__(self, message: str, original_exception: Exception | None = None):
        super().__init__(message)
        self.original_exception = (
            original_exception  # Store the original exception for debugging
        )
