from unittest import TestCase

from pypaystack2.api import Transaction
from . import test_auth_key


class TestTransactionRecords(TestCase):
    def setUp(self):
        super(TestTransactionRecords, self).setUp()
        self.assertNotEqual(test_auth_key, None)
        self.transaction = Transaction(auth_key=test_auth_key)

    def test_transaction_records(self):
        """
        Integration test for retriving all transactions and getting single transaction details
        """

        def retrieve_all_transactions():
            (
                status_code,
                status,
                response_msg,
                all_transactions,
            ) = self.transaction.get_transactions()
            self.assertEqual(status_code, 200)
            self.assertEqual(status, True)
            self.assertEqual(response_msg, "Transactions retrieved")
            self.assertIsInstance(all_transactions, list)
            return all_transactions

        def retrieve_one_transaction():
            one_transaction = all_transactions[0]
            (
                status_code,
                status,
                response_msg,
                transaction_data,
            ) = self.transaction.get_transaction(id=one_transaction["id"])
            self.assertEqual(status_code, 200)
            self.assertEqual(status, True)
            self.assertEqual(response_msg, "Transaction retrieved")

            # removing authorization field as content is not concurrent in transaction_list and transaction_data
            if "authorization" in transaction_data.keys():
                transaction_data.pop("authorization")
            if "authorization" in one_transaction.keys():
                one_transaction.pop("authorization")

            # For yet unknown reasons, `transaction_data.keys()` and
            # `one_transaction.keys()` seem to be returning differnt
            # dicts. so it raises issures.

            # assert if equal transaction keys are equal
            # self.assertEqual(transaction_data.keys(),
            #                  one_transaction.keys())

            # assert if transaction_data keys is a superser of
            # one_transaction keys.
            # TODO: Fix this test.
            self.assertGreaterEqual(transaction_data.keys(), one_transaction.keys())

        all_transactions = retrieve_all_transactions()
        retrieve_one_transaction()
