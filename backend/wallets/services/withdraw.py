from rest_framework.exceptions import NotFound
from datetime import datetime
from django.db import transaction as django_transaction

from wallets.domains import WithdrawDomain
from wallets.exceptions import InsufficientBalanceException, ThirdPartyIsDownException
from wallets.models import Wallet, Transaction


class WithdrawService:

    @classmethod
    def create_transaction(cls, amount: int, wallet_uuid: str, execute_time: datetime) -> Transaction:
        try:
            wallet: Wallet = WithdrawDomain.get_wallet_by_uuid(wallet_uuid=wallet_uuid)
            return WithdrawDomain.create_transaction(amount=amount, wallet=wallet, execute_time=execute_time)
        except Wallet.DoesNotExist:
            raise NotFound('wallet does not exist')

    @classmethod
    def withdraw(cls, transaction_id: int) -> None:
        transaction = Transaction.objects.get(id=transaction_id)
        try:
            with django_transaction.atomic():
                WithdrawDomain.withdraw(transaction.id)
                WithdrawDomain.send_withdraw_request(transaction)
        except (InsufficientBalanceException, ThirdPartyIsDownException):
            WithdrawDomain.fail_transaction(transaction)
