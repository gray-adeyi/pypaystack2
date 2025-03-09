from decimal import Decimal
from typing import Unpack, TypedDict, cast

from pypaystack2.enums import Currency
from pypaystack2.models.payload_models import (
    NigeriaServiceFeeOptions,
    CoteDIvoreServiceFeeOptions,
    GhanaServiceFeeOptions,
    KenyaServiceFeeOptions,
    SouthAfricaServiceFeeOptions,
    RwandaServiceFeeOptions,
    EgyptServiceFeeOptions,
)


class ServiceFeeOptions(TypedDict):
    is_international: bool | None
    service: str
    is_eft: bool | None
    card: str | None


class FeesCalculationMixin:
    _NGN_LOCAL_TRANSACTIONS_DECIMAL_FEE = Decimal("0.015")
    _NGN_LOCAL_TRANSACTIONS_FLAT_FEE = 10_000
    _NGN_LOCAL_TRANSACTIONS_FEE_CAP = 200_000
    _NGN_LOCAL_TRANSACTIONS_FLAT_FEE_WAIVED = 250_000
    _NGN_INTERNATIONAL_TRANSACTIONS_FLAT_FEE = 10_000
    _NGN_INTERNATIONAL_TRANSACTIONS_NON_AMERICAN_EXPRESS_CARDS_DECIMAL_FEE = Decimal(
        "0.039"
    )
    _NGN_INTERNATIONAL_TRANSACTIONS_AMERICAN_EXPRESS_CARDS_DECIMAL_FEE = Decimal(
        "0.045"
    )
    _NGN_LIVE_SMARTPEAK_P1000_COST_PER_DEVICE = 10_000_000
    _NGN_TEST_SMARTPEAK_P1000_COST_PER_DEVICE = 8_500_000
    _NGN_PHYSICAL_TERMINAL_CARD_TRANSACTIONS_DECIMAL_FEE = Decimal("0.005")
    _NGN_PHYSICAL_TERMINAL_CARD_TRANSACTIONS_FEE_CAP = 100_000

    _GHS_LOCAL_AND_INTERNATIONAL_TRANSACTIONS_DECIMAL_FEE = Decimal("0.0195")
    _GHS_FEE_PER_MOBILE_MONEY_TRANSFERS = 100
    _GHS_FEE_PER_BANK_ACCOUNT_TRANSFERS = 800

    _ZAR_LOCAL_TRANSACTIONS_DECIMAL_FEE = Decimal("0.029")
    _ZAR_LOCAL_TRANSACTIONS_FLAT_FEE = 100
    _ZAR_LOCAL_TRANSACTIONS_FLAT_FEE_WAIVED = 1000
    _ZAR_LOCAL_EFT_TRANSACTIONS_DECIMAL_FEE = Decimal("0.02")
    _ZAR_INTERNATIONAL_TRANSACTIONS_DECIMAL_FEE = Decimal("0.031")
    _ZAR_INTERNATIONAL_TRANSACTIONS_FLAT_FEE = 100
    _ZAR_FEE_PER_BANK_ACCOUNT_TRANSFERS = 300

    _KES_MPESA_TRANSACTIONS_DECIMAL_FEE = Decimal("0.015")
    _KES_LOCAL_CARD_TRANSACTIONS_DECIMAL_FEE = Decimal("0.029")
    _KES_INTERNATIONAL_CARD_TRANSACTIONS_DECIMAL_FEE = Decimal("0.038")

    _XOF_MOBILE_MONEY_DECIMAL_FEE = Decimal("0.0195")
    _XOF_LOCAL_CARD_TRANSACTIONS_DECIMAL_FEE = Decimal("0.032")
    _XOF_INTERNATIONAL_CARD_TRANSACTIONS_DECIMAL_FEE = Decimal("0.038")

    _RWF_LOCAL_TRANSACTIONS_DECIMAL_FEE = Decimal("0.029")
    _RWF_INTERNATIONAL_TRANSACTIONS_DECIMAL_FEE = Decimal("0.038")

    _EGP_LOCAL_TRANSACTIONS_NON_MEEZA_CARD_DECIMAL_FEE = Decimal("0.027")
    _EGP_LOCAL_TRANSACTIONS_FLAT_FEE = 250
    _EGP_LOCAL_TRANSACTIONS_MEEZA_CARD_DECIMAL_FEE = Decimal("0.02")
    _EGP_INTERNATIONAL_TRANSACTIONS_FLAT_FEE = 250
    _EGP_INTERNATIONAL_TRANSACTIONS_DECIMAL_FEE = Decimal("0.035")

    def calculate_fee(
        self, amount: int, currency: Currency, **options: Unpack[ServiceFeeOptions]
    ) -> int:
        """Calculates the fee paystack charges.

        Fees can vary based on the currency of your integration, the service you're
        utilizing.

        Args:
            amount: The currency value in its subunit (e.g. kobo) that you want to calculate
                its paystack fee. amount may also be used to denote quantity in some cases.
                e.g. when currency=`Currency.NGN` and  service="physical_terminal_live_smartpeak_p1000"
            currency: The currency the amount is in. e.g. `Currency.NGN` if amount=1000 (i.e. a
                thousand kobos)
            options: These are additional keyword arguments that can modify how the fees is calculated
                or what the fee is calculated for. valid options keyword arguments can vary depending
                on currency but can be any combination of `is_international` denoting if we're
                calculating for a local or international transaction. it defaults to False
                to indicate local transactions. `service` denoting the paystack service we want to
                calculate the fee for, `is_eft` and `card`. Valid arguments for these options can
                be gotten from the pydantic models used to validate them based on the currency.
                See `NigeriaServiceFeeOptions`, `GhanaServiceFeeOptions`, `SouthAfricaServiceFeeOptions`,
                `KenyaServiceFeeOptions`, `CoteDIvoreServiceFeeOptions`, `RwandaServiceFeeOptions`,
                and EgyptServiceFeeOptions,
                i.e. NigeriaServiceFeeOptions is used to validate the options when currency=`Currency.NGN`
                Suitable defaults are provided, you'll only ever need to provide options
                when what you need to calculate changes.

        Notes:
            Use this method with care. it is implemented with hard coded values referenced from
            https://support.paystack.com/en/articles/2130306  and
            https://paystack.com/ci/pricing?localeUpdate=true
            which are subject to changes in the future.
            Its important that the rates are still valid for correct calculations.
            Please create an issue here https://github.com/gray-adeyi/pypaystack2/issues
            if you find a bug.
        """
        try:
            options_validator_class = {
                Currency.NGN: NigeriaServiceFeeOptions,
                Currency.GHS: GhanaServiceFeeOptions,
                Currency.ZAR: SouthAfricaServiceFeeOptions,
                Currency.KES: KenyaServiceFeeOptions,
                Currency.XOF: CoteDIvoreServiceFeeOptions,
                Currency.RWF: RwandaServiceFeeOptions,
                Currency.EGP: EgyptServiceFeeOptions,
            }[currency]
        except KeyError:
            raise ValueError(
                f"fees calculation for currency {currency} is not supported"
            )
        options_model = options_validator_class.model_validate(options)  # type: ignore

        if currency == Currency.NGN:
            return self._calculate_ngn_fee(amount, options_model)
        if currency == Currency.GHS:
            return self._calculate_ghs_fee(amount, options_model)
        if currency == Currency.ZAR:
            return self._calculate_zar_fee(amount, options_model)
        if currency == Currency.KES:
            return self._calculate_kes_fee(amount, options_model)
        if currency == Currency.XOF:
            return self._calculate_xof_fee(amount, options_model)
        if currency == Currency.RWF:
            return self._calculate_rwf_fee(amount, options_model)
        if currency == Currency.EGP:
            return self._calculate_egp_fee(amount, options_model)
        raise ValueError(
            f"calculations not supported for the provided currency {currency}"
        )

    def to_base_unit(self, value: int | Decimal) -> Decimal:
        """Converts a currency value from its subunit to its base unit.

        i.e. Kobo -> Naira, Pesewa -> Ghanaian Cedi, Cent ->  South African Rand,
        Cent -> Kenyan Shilling, Centime -> West African CFA Franc,
        Centime -> Rwandan Franc, Piastre ->  Egyptian Pound.

        Args:
            value: The currency value in its subunit. e.g. Kobo
        """
        _value = value
        is_integer = isinstance(_value, int)
        is_decimal = isinstance(_value, Decimal)
        if not any([is_integer, is_decimal]):
            raise ValueError("value must be an integer or Decimal")
        if is_integer:
            _value = Decimal(_value)
        _value = cast(Decimal, _value)
        return _value / 100

    def to_subunit(self, value: int | float | Decimal) -> int:
        """Converts a currency value from its base unit to its subunit.

        i.e. Naira-> Kobo,Ghanaian Cedi ->  Pesewa,South African Rand -> Cent,
        Kenyan Shilling -> Cent,West African CFA Franc -> Centime,
        Rwandan Franc -> Centime,Egyptian Pound -> Piastre.

        Args:
            value: The currency value in its base unit. e.g. Naira
        """
        is_integer = isinstance(value, int)
        is_float = isinstance(value, float)
        is_decimal = isinstance(value, Decimal)
        if not any([is_integer, is_float, is_decimal]):
            raise ValueError("value must be an integer, float or Decimal")
        if is_integer:
            value = Decimal(value)
        if is_float:
            value = Decimal(str(round(value, 2)))
        return round(value * 100)

    def _calculate_ngn_fee(self, amount: int, options: NigeriaServiceFeeOptions) -> int:
        if (
            options.service == "transactions" and not options.is_international
        ) or options.service in [
            "virtual_terminal_ussd_transactions",
            "virtual_terminal_local_card_transactions",
            "physical_terminal_ussd_transactions",
            "physical_terminal_bank_transfers",
        ]:
            return self._calculate_ngn_local_transaction_fee(amount)
        if (
            options.service == "transactions" and options.is_international
        ) or options.service == "virtual_terminal_international_card_transactions":
            if options.card == "american_express":
                return round(
                    amount
                    * self._NGN_INTERNATIONAL_TRANSACTIONS_AMERICAN_EXPRESS_CARDS_DECIMAL_FEE
                )
            return round(
                (
                    amount
                    * self._NGN_INTERNATIONAL_TRANSACTIONS_NON_AMERICAN_EXPRESS_CARDS_DECIMAL_FEE
                )
                + self._NGN_INTERNATIONAL_TRANSACTIONS_FLAT_FEE
            )
        if options.service == "transfers":
            if amount <= 500_000:
                return 1000
            if 500_001 <= amount <= 5_000_000:
                return 2500
            return 5000
        if (
            options.service == "virtual_account_transactions"
            or options.service == "virtual_terminal_transfers"
        ):
            fees = round(0.01 * amount)
            return fees if fees < 30_000 else 30_000
        if options.service == "physical_terminal_live_smartpeak_p1000":
            return amount * self._NGN_LIVE_SMARTPEAK_P1000_COST_PER_DEVICE
        if options.service == "physical_terminal_test_smartpeak_p1000":
            return amount * self._NGN_TEST_SMARTPEAK_P1000_COST_PER_DEVICE
        if options.service == "physical_terminal_card_transactions":
            fee = amount * self._NGN_PHYSICAL_TERMINAL_CARD_TRANSACTIONS_DECIMAL_FEE
            return (
                round(fee)
                if round(fee) < self._NGN_PHYSICAL_TERMINAL_CARD_TRANSACTIONS_FEE_CAP
                else self._NGN_PHYSICAL_TERMINAL_CARD_TRANSACTIONS_FEE_CAP
            )
        raise ValueError("unsupported service option")

    def _calculate_ngn_local_transaction_fee(self, amount: int) -> int:
        fee = amount * self._NGN_LOCAL_TRANSACTIONS_DECIMAL_FEE
        if amount > self._NGN_LOCAL_TRANSACTIONS_FLAT_FEE_WAIVED:
            fee += self._NGN_LOCAL_TRANSACTIONS_FLAT_FEE
        return (
            round(fee)
            if round(fee) < self._NGN_LOCAL_TRANSACTIONS_FEE_CAP
            else self._NGN_LOCAL_TRANSACTIONS_FEE_CAP
        )

    def _calculate_ghs_fee(self, amount: int, options: GhanaServiceFeeOptions) -> int:
        if options.service == "transactions":
            return round(
                amount * self._GHS_LOCAL_AND_INTERNATIONAL_TRANSACTIONS_DECIMAL_FEE
            )
        if options.service == "transfers_to_mobile_money":
            return self._GHS_FEE_PER_MOBILE_MONEY_TRANSFERS
        if options.service == "transfers_to_bank_accounts":
            return self._GHS_FEE_PER_BANK_ACCOUNT_TRANSFERS
        raise ValueError("unsupported service option")

    def _calculate_zar_fee(
        self, amount: int, options: SouthAfricaServiceFeeOptions
    ) -> int:
        if options.service == "transactions" and not options.is_international:
            if options.is_eft:
                return round(amount * self._ZAR_LOCAL_EFT_TRANSACTIONS_DECIMAL_FEE)
            fee = amount * self._ZAR_LOCAL_TRANSACTIONS_DECIMAL_FEE
            if amount > self._ZAR_LOCAL_TRANSACTIONS_FLAT_FEE_WAIVED:
                fee += self._ZAR_LOCAL_TRANSACTIONS_FLAT_FEE
            return round(fee)
        if options.service == "transactions" and options.is_international:
            return round(
                (amount * self._ZAR_INTERNATIONAL_TRANSACTIONS_DECIMAL_FEE)
                + self._ZAR_INTERNATIONAL_TRANSACTIONS_FLAT_FEE
            )
        if options.service == "transfers":
            return self._ZAR_FEE_PER_BANK_ACCOUNT_TRANSFERS
        raise ValueError("unsupported service option")

    def _calculate_kes_fee(self, amount: int, options: KenyaServiceFeeOptions) -> int:
        if options.service == "mpesa_transactions":
            return round(amount * self._KES_MPESA_TRANSACTIONS_DECIMAL_FEE)
        if options.service == "card_transactions":
            if options.is_international:
                return round(
                    amount * self._KES_INTERNATIONAL_CARD_TRANSACTIONS_DECIMAL_FEE
                )
            return round(amount * self._KES_LOCAL_CARD_TRANSACTIONS_DECIMAL_FEE)
        if options.service == "transfers_to_mpesa_wallet":
            if 100 <= amount <= 150_000:
                return 2000
            if 150_100 <= amount <= 2_000_000:
                return 4000
            if amount >= 2_000_100:
                return 6000
            raise ValueError(
                f"{amount} is an invalid amount for transfers_to_mpesa_wallet. see https://paystack.com/ke/pricing?localeUpdate=true for a valid amount"
            )
        if options.service == "transfers_to_mpesa_paybill":
            if 100 <= amount <= 150_000:
                return 4000
            if 150_100 <= amount <= 1_000_000:
                return 8000
            if 1_000_100 <= amount <= 4_000_000:
                return 14000
            if 4_000_100 <= amount <= 99_999_900:
                return 18_000
            if amount >= 100_000_000:
                return 35_000
            raise ValueError(
                f"{amount} is an invalid amount for transfers_to_mpesa_paybill. see https://paystack.com/ke/pricing?localeUpdate=true for a valid amount"
            )
        if options.service == "transfers_to_bank_account":
            if 100 <= amount <= 1_000_000:
                return 8000
            if 1_000_100 <= amount <= 5_000_000:
                return 14_000
            if 5_000_100 <= amount <= 99_999_900:
                return 18_000
            if amount >= 100_000_000:
                return 35_000
            raise ValueError(
                f"{amount} is an invalid amount for transfers_to_bank_account. see https://paystack.com/ke/pricing?localeUpdate=true for a valid amount"
            )
        raise ValueError("unsupported service option")

    def _calculate_xof_fee(
        self, amount: int, options: CoteDIvoreServiceFeeOptions
    ) -> int:
        if options.service == "mobile_money_transactions":
            return round(amount * self._XOF_MOBILE_MONEY_DECIMAL_FEE)
        if options.service == "card_transactions":
            if options.is_international:
                return round(
                    amount * self._XOF_INTERNATIONAL_CARD_TRANSACTIONS_DECIMAL_FEE
                )
            round(amount * self._XOF_LOCAL_CARD_TRANSACTIONS_DECIMAL_FEE)
        raise ValueError("unsupported service option")

    def _calculate_rwf_fee(self, amount: int, options: RwandaServiceFeeOptions) -> int:
        if options.is_international:
            return round(amount * self._RWF_INTERNATIONAL_TRANSACTIONS_DECIMAL_FEE)
        return round(amount * self._RWF_LOCAL_TRANSACTIONS_DECIMAL_FEE)

    def _calculate_egp_fee(self, amount: int, options: EgyptServiceFeeOptions) -> int:
        if options.is_international:
            return round(
                (amount * self._EGP_INTERNATIONAL_TRANSACTIONS_DECIMAL_FEE)
                + self._EGP_INTERNATIONAL_TRANSACTIONS_FLAT_FEE
            )
        if options.card == "others":
            return round(
                (amount * self._EGP_LOCAL_TRANSACTIONS_NON_MEEZA_CARD_DECIMAL_FEE)
                + self._EGP_LOCAL_TRANSACTIONS_FLAT_FEE
            )
        return round(
            (amount * self._EGP_LOCAL_TRANSACTIONS_MEEZA_CARD_DECIMAL_FEE)
            + self._EGP_LOCAL_TRANSACTIONS_FLAT_FEE
        )
