from decimal import Decimal
from unittest import TestCase

from dotenv import load_dotenv

from pypaystack2 import PaystackClient
from pypaystack2.enums import Currency


class PaystackFeesCalculationTestcase(TestCase):
    client: PaystackClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = PaystackClient()

    def test_calculate_fee(self) -> None:
        cases = [
            {
                "name": "NGN: Test fee for less than NGN 2500",
                "options": {"currency": Currency.NGN, "amount": 240_000},
                "expected_value": 3600,
            },
            {
                "name": "NGN: Test fee for greater than NGN 2500",
                "options": {"currency": Currency.NGN, "amount": 500_000},
                "expected_value": 17_500,
            },
            {
                "name": "NGN: Test fee is capped at NGN 2000",
                "options": {"currency": Currency.NGN, "amount": 100_000_000},
                "expected_value": 200_000,
            },
            {
                "name": "NGN: Test international non american express card",
                "options": {
                    "currency": Currency.NGN,
                    "amount": 100_000_000,
                    "is_international": True,
                    "card": "visa",
                },
                "expected_value": 3_910_000,
            },
            {
                "name": "NGN: Test international for american express card",
                "options": {
                    "currency": Currency.NGN,
                    "amount": 100_000_000,
                    "is_international": True,
                    "card": "american_express",
                },
                "expected_value": 4_500_000,
            },
            {
                "name": "NGN: Test local transfer below NGN 5000",
                "options": {
                    "currency": Currency.NGN,
                    "amount": 200_000,
                    "service": "transfers",
                },
                "expected_value": 1000,
            },
            {
                "name": "NGN: Test local transfer above NGN 5000 and below NGN 50_001",
                "options": {
                    "currency": Currency.NGN,
                    "amount": 1_000_000,
                    "service": "transfers",
                },
                "expected_value": 2500,
            },
        ]
        for case in cases:
            with self.subTest(case["name"]):
                self.assertEqual(
                    self.client.calculate_fee(**case["options"]), case["expected_value"]
                )

    def test_to_base_unit(self) -> None:
        cases = [
            {"value": 100, "expected": Decimal(1)},
            {"value": 1000, "expected": Decimal(10)},
            {"value": Decimal(100), "expected": Decimal(1)},
            {"value": Decimal("10.0"), "expected": Decimal("0.1")},
            {"value": 50, "expected": Decimal("0.5")},
        ]
        for case in cases:
            with self.subTest(
                f"expects {case['value']} to base unit to be {case['expected']}"
            ):
                self.assertEqual(
                    self.client.to_base_unit(case["value"]), case["expected"]
                )

    def test_to_base_unit_raises_error_on_invalid_input_value(self) -> None:
        with self.assertRaises(ValueError) as context:
            self.client.to_base_unit(10.00)  # type: ignore
        self.assertEqual(
            context.exception.args[0], "value must be an integer or Decimal"
        )

    def test_to_subunit(self) -> None:
        cases = [
            {"value": 1, "expected": 100},
            {"value": 10, "expected": 1000},
            {"value": 1.5, "expected": 150},
            {"value": Decimal("10.5"), "expected": 1050},
        ]
        for case in cases:
            with self.subTest(
                f"expects {case['value']} to subunit to be {case['expected']}"
            ):
                self.assertEqual(
                    self.client.to_subunit(case["value"]), case["expected"]
                )
