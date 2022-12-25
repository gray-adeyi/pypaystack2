"""Pypaystack2 is a simple python wrapper for Paystack API.

it is a fork of the original project [Pypaystack](https://github.com/edwardpopoola/pypaystack)
Modules and packages exported by this package:
   - `api`: A package containing several wrappers for Paystack API, like apple pay api, bulk charges api e.t.c.
   - `utils`: A module containing useful utilities and enums
   - `errors`: A module containing error types for pypaystack2
"""
from .version import __version__, __author__, __copyright__, __license__, __title__
from pypaystack2.api.paystack import Paystack
