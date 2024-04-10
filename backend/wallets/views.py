from typing import Dict

from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from wallets.models import Wallet
from wallets.serializers import WalletSerializer, DepositSerializer
from wallets.services import DepositService


class CreateWalletView(CreateAPIView):
    serializer_class = WalletSerializer


class RetrieveWalletView(RetrieveAPIView):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()
    lookup_field = "uuid"


class CreateDepositView(APIView):
    def post(self, request, uuid,  *args, **kwargs):
        serializer: DepositSerializer = DepositSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        amount: int = serializer.validated_data['amount']
        wallet: Wallet = DepositService.deposit(wallet_uuid=uuid, amount=amount)
        data: Dict = WalletSerializer(wallet).data
        return Response(data=data, status=status.HTTP_200_OK)


class ScheduleWithdrawView(APIView):
    def post(self, request, *args, **kwargs):
        # todo: implement withdraw logic
        pass
        return Response({})

