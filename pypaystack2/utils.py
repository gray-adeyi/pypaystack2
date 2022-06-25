from .errors import InvalidDataError
import enum


class Currency(str, enum.Enum):
    """
    Provides an enum of currencies
    supported by paystack.
    """
    NGN = "NGN"
    GHS = "GHS"
    ZAR = "ZAR"
    USD = "USD"


class Interval(str, enum.Enum):
    """
    Provides an enum of intervals
    supported by paystack.
    """
    HOURLY = 'hourly'
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    ANNUALLY = 'annually'


def validate_amount(amount):

    if not amount:
        raise InvalidDataError("Amount to be charged is required")

    if isinstance(amount, int) or isinstance(amount, float):  # Save the sever some headaches
        if amount < 0:
            raise InvalidDataError("Negative amount is not allowed")
        return amount
    else:
        raise InvalidDataError("Amount should be a number")


def validate_interval(interval):

    interval = interval if interval.lower(
    ) in ['hourly', 'daily', 'weekly', 'monthly', 'annually'] else None
    if not interval:
        raise InvalidDataError("Please provide a valid plan interval")
    return interval
