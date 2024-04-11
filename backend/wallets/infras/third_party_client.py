from wallets.utils import request_third_party_deposit
from wallets.exceptions import ThirdPartyIsDownException


class ThirdPartyClient:
    @classmethod
    def withdraw(cls, amount: int, wallet_uuid: str):
        response = request_third_party_deposit()
        if response.get('status') == 200:
            return response
        raise ThirdPartyIsDownException()
