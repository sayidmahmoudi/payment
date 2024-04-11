from datetime import datetime

from django.db import transaction as django_transaction
from django.db.models import F

from wallets.models import Wallet, Transaction


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
    def withdraw(cls, amount: int, transaction_id: int) -> Transaction:
        with django_transaction.atomic():
            transaction = Transaction.objects.get(id=transaction_id)
            wallet = Wallet.objects.select_for_update(id=transaction.wallet_id)
            transaction.state = Transaction.DONE
            wallet.balance = F("balance") - amount
            wallet.save()
        return transaction
