from django.db import transaction as django_transaction
from django.db.models import F
from django.utils import timezone

from wallets.models import Wallet, Transaction


class DepositDomain:
    @classmethod
    def get_wallet_by_uuid(cls, wallet_uuid: str):
        return Wallet.objects.get(uuid=wallet_uuid)

    @classmethod
    def deposit(cls, amount: int, wallet: Wallet) -> Transaction:
        with django_transaction.atomic():
            transaction = Transaction.objects.create(
                amount=amount,
                wallet=wallet,
                execute_time=timezone.now(),
                type=Transaction.DEPOSIT,
                state=Transaction.DONE,
            )
            wallet.balance = F("balance") + amount
            wallet.save()
        return transaction
