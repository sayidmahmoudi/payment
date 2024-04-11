from rest_framework.exceptions import NotFound

from wallets.domains import DepositDomain
from wallets.models import Wallet, Transaction


class DepositService:

    @classmethod
    def deposit(cls, amount: int, wallet_uuid: str) -> Transaction:
        try:
            wallet: Wallet = DepositDomain.get_wallet_by_uuid(wallet_uuid=wallet_uuid)
            return DepositDomain.deposit(amount=amount, wallet=wallet)
        except Wallet.DoesNotExist:
            raise NotFound('wallet does not exist')
