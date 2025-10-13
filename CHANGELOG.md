# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## unreleased

## [3.0.2] - (10th October 2025)

### Fixed

- Missing `domain` field in `Customer` model.

## [3.0.1] - (4th October 2025)

### Fixed

- Missing `update_existing_subscriptions` parameter in `AsyncPlanClient.update` and `PlanClient.update`

## [3.0.0] - (9th March 2025)

### Added

- Pydantic v2 to project dependencies.
- Utility methods for fees calculation `calculate_fee`, `to_base_unit`, `to_subunit`.
- `ClientNetworkError`. An exception raised for all network related errors.

### Changed

- `auth_key` parameter to `secret_key`.
- secret key environmental variable name from `PAYSTACK_AUTHORIZATION_KEY` to `PAYSTACK_SECRET_KEY`
- `MissingAuthKeyException` to  `MissingSecretKeyException`
- Rename wrappers to clients. All usages of wrappers are now deprecated in favour of clients.
  `Paystack` wrapper class in the past is now `PaystackClient` likewise all other api wrappers
  are now sub clients e.g. `ApplePay` is now  `ApplePayClient`

### Fixed

- Unused `amount` parameter in `TransactionClient.export`

### Removed

- Support for `python<=3.10`
- Package defined `HTTPMethod` enum. Now using `HTTPMethod` from the standard lib.
- `validate_amount` and `validate_interval` helper methods
- `InvalidMethodException`, `InvalidDataException`

## [2.1.1] - (9th December 2024)

### Added

- Rwanda to paystack supported countries
- RWF to paystack supported currencies

### Changed

- Make `TransactionSplit.get_splits` parameters optional

### Changed

- Charge.setAddress -> Charge.submitAddress

## [2.1.0] - (8th October 2024)

### Added

- Param documentation for ApplePay.unregister_domain
- Param documentation for AsyncApplePay.unregister_domain
- `meta`, `type` and `code` fields to `Response`

### Changed

- Bumped httpx to 0.27.2
- Transaction.get_transactions(customer: Optional[int]) -> Transaction.get_transactions(customer: Optional[str])
- AsyncTransaction.get_transactions(customer: Optional[int]) -> AsyncTransaction.get_transactions(customer:
  Optional[str])
- Transaction.export(customer: Optional[int]) -> Transaction.export(customer: Optional[str])
- AsyncTransaction.export(customer: Optional[int]) -> AsyncTransaction.export(customer: Optional[str])
- Transaction.export(settlement: Optional[int]) -> Transaction.export(settlement: Optional[str])
- AsyncTransaction.export(settlement: Optional[int]) -> AsyncTransaction.export(settlement: Optional[str])
- Transaction.export(payment_page: Optional[int]) -> Transaction.export(payment_page: Optional[str])
- AsyncTransaction.export(payment_page: Optional[int]) -> AsyncTransaction.export(payment_page: Optional[str])
- PaymentRequest.update `line_item` and `tax` parameter to use `Tax` and `LineItem` inplace of `list`
- AsyncPaymentRequest.update `line_item` and `tax` parameter to use `Tax` and `LineItem` inplace of `list`
- PaymentPage.metadata type
- AsyncPaymentPage.metadata type
- Plan.update documentation

## Fixed

- Use of literal "POST" in TransactionSplit.add_or_update
- Use of literal "POST" in AsyncTransactionSplit.add_or_update

## Removed

- Redundant payload from Subscription.send_update_link
- Redundant payload from AsyncSubscription.send_update_link

## [2.0.3] - (24th March 2024)

### Added

- Changelog to project.

### Fixed

- `ApplePay.unregister_domain` and `AsyncApplePay.unregister_domain` raises `NotImplementedError`
- Client raises `JSONDecodeError` when response is not json serializable. It now returns with a
  `Response` with the `data` parameter containing a `content` field with the bytes content returned.
- Mismatched source code and documentation links in docs

## [2.0.2] - (1st December 2023)

### Added

- Parameter options to ApplePay wrapper methods
- `back_transfer` parameter to `Charge.charge` and `AsyncCharge.charge`
- `pay_with_bank_transfer`, `pay_with_bank` parameters to `Miscellaneous.get_banks` and
  `AsyncMiscellaneous.get_banks`
- `split_code` parameter to `PaymentPage.create` and `AsyncPaymentPage.create`
- `QUARTERLY` and `BIANNUALLY` to `Interval` enum

### Removed

- `birthday` parameter from `Charge.charge` and `AsyncChrge.charge`
- `Miscellaneous.get_providers` and `AsyncMiscellaneous.get_providers`

### Fixed

- Broken docstrings API reference documentation links

## [2.0.1] - (27th July 2023)

### Changed

- Refactor project internals

## [2.0.0] - (18th May 2023)

### Added

- Asynchronous wrappers and `AsyncPaystack` class which provided bindings to other async
  wrappers.

### Changed

- Use `httpx` in place of `requests`

## [1.1.3] - (10th March 2023)

### Added

- `Paystack` class which had bindings to other wrappers

## [1.0.3] - (26th December 2022)

### Added

- Cleanup documentation

## [1.0.2] - (25th December 2022)

### Added

- Implement additional wrappers to cover all endpoints provided by paystack

## [1.0.0] - (25th July 2022)

### Added

- Fork project from [pypaystack](https://github.com/edwardpopoola/pypaystack)

### Fixed

- Breaks projects were it is added as a dependency

[unreleased]: https://github.com/gray-adeyi/pypaystack2/compare/v2.1.1...HEAD

[2.1.1]: https://github.com/gray-adeyi/pypaystack2/compare/v2.1.0...v2.1.1

[2.1.0]: https://github.com/gray-adeyi/pypaystack2/compare/v2.0.3...v2.1.0

[2.0.3]: https://github.com/gray-adeyi/pypaystack2/compare/v2.0.2...v2.0.3

[2.0.2]: https://github.com/gray-adeyi/pypaystack2/compare/v2.0.1...v2.0.2

[2.0.1]: https://github.com/gray-adeyi/pypaystack2/compare/v2.0.0...v2.0.1

[2.0.0]: https://github.com/gray-adeyi/pypaystack2/compare/v1.1.3...v2.0.0

[1.1.3]: https://github.com/gray-adeyi/pypaystack2/compare/v1.0.3...v1.1.3

[1.0.3]: https://github.com/gray-adeyi/pypaystack2/compare/v1.0.2...v1.0.3

[1.0.2]: https://github.com/gray-adeyi/pypaystack2/compare/v1.0.0...v1.0.2

[1.0.0]: https://github.com/gray-adeyi/pypaystack2/releases/tag/v1.0.0
