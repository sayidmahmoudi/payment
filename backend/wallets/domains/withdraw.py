from datetime import datetime

from django.db import transaction as django_transaction
from django.db.models import F

from wallets.exceptions import InsufficientBalanceException
from wallets.models import Wallet, Transaction
from wallets.infras import ThirdPartyClient


class WithdrawDomain:
    @classmethod
    def get_wallet_by_uuid(cls, wallet_uuid: str):
        return Wallet.objects.get(uuid=wallet_uuid)

    @classmethod
    def create_transaction(cls, amount: int, wallet: Wallet, execute_time: datetime) -> Transaction:
        return Transaction.objects.create(
                amount=amount,
                wallet=wallet,
                execute_time=execute_time,
                type=Transaction.WITHDRAW,
                state=Transaction.CREATED,
            )

    @classmethod
    def fail_transaction(cls, transaction: Transaction) -> None:
        transaction.state = Transaction.FAILED
        transaction.save()

    @classmethod
    def send_withdraw_request(cls, transaction: Transaction) -> None:
        ThirdPartyClient.withdraw(amount=transaction.amount, wallet_uuid=transaction.wallet.uuid)

    @classmethod
    def withdraw(cls, transaction_id: int) -> Transaction:
        with django_transaction.atomic():
            transaction = Transaction.objects.get(id=transaction_id)
            wallet = Wallet.objects.select_for_update().get(id=transaction.wallet_id)

            if wallet.balance < transaction.amount:
                raise InsufficientBalanceException()

            transaction.state = Transaction.DONE
            transaction.save()
            wallet.balance = F("balance") - transaction.amount
            wallet.save()
        return transaction
