from django.db import transaction
from django.db.models import F

from wallets.models import Wallet, Transaction


class DepositDomain:

    @classmethod
    def get_wallet_by_uuid(cls, wallet_uuid: str):
        return Wallet.objects.get(uuid=wallet_uuid)

    @classmethod
    def deposit(cls, amount: int, wallet: Wallet) -> Wallet:
        with transaction.atomic():
            Transaction.objects.create(
                amount=amount,
                type=Transaction.DEPOSIT,
                state=Transaction.DONE,
            )
            wallet.balance = F("balance") + amount
            wallet.save()
            wallet.refresh_from_db()
        return wallet
