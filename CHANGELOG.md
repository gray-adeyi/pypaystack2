# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Changelog to project.

## [2.0.2] - 2023-12-01

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

## [2.0.1] - 2023-07-27

### Changed

- Refactor project internals

## [2.0.0] - 2023-05-18

### Added

- Asynchronous wrappers and `AsyncPaystack` class which provided bindings to other async
  wrappers.

### Changed

- Use `httpx` in place of `requests`

## [1.1.3] - 2023-03-10

### Added

- `Paystack` class which had bindings to other wrappers

## [1.0.3] - 2022-12-26

### Added

- Cleanup documentation

## [1.0.2] - 2022-12-25

### Added

- Implement additional wrappers to cover all endpoints provided by paystack

## [1.0.0] - 2022-07-25

### Added

- Fork project from [pypaystack](https://github.com/edwardpopoola/pypaystack)

### Fixed

- Breaks projects were it is added as a dependency

[unreleased]: https://github.com/olivierlacan/keep-a-changelog/compare/v2.0.2...HEAD

[2.0.2]: https://github.com/gray-adeyi/pypaystack2/compare/v2.0.1...v2.0.2

[2.0.1]: https://github.com/gray-adeyi/pypaystack2/compare/v2.0.0...v2.0.1

[1.1.3]: https://github.com/gray-adeyi/pypaystack2/compare/v1.0.3...v1.1.3

[1.0.3]: https://github.com/gray-adeyi/pypaystack2/compare/v1.0.2...v1.0.3

[1.0.2]: https://github.com/gray-adeyi/pypaystack2/compare/v1.0.0...v1.0.2
