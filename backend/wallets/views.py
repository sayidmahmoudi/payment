from typing import Dict

from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from wallets.models import Wallet, Transaction
from wallets.serializers import WalletSerializer, DepositSerializer, TransactionSerializer, WithdrawSerializer
from wallets.services import DepositService, WithdrawService


class CreateWalletView(CreateAPIView):
    serializer_class = WalletSerializer


class RetrieveWalletView(RetrieveAPIView):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()
    lookup_field = "uuid"


class CreateDepositView(APIView):
    @swagger_auto_schema(request_body=DepositSerializer)
    def post(self, request, uuid,  *args, **kwargs):
        serializer: DepositSerializer = DepositSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        amount: int = serializer.validated_data['amount']
        transaction: Transaction = DepositService.deposit(wallet_uuid=uuid, amount=amount)
        data: Dict = TransactionSerializer(transaction).data
        return Response(data=data, status=status.HTTP_201_CREATED)


class ScheduleWithdrawView(APIView):
    @swagger_auto_schema(request_body=WithdrawSerializer)
    def post(self, request, uuid, *args, **kwargs):
        serializer: WithdrawSerializer = WithdrawSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        amount: int = serializer.validated_data['amount']
        execute_time = serializer.validated_data['execute_time']
        transaction: Transaction = WithdrawService.create_transaction(
            wallet_uuid=uuid,
            amount=amount,
            execute_time=execute_time
        )
        data: Dict = TransactionSerializer(transaction).data
        return Response(data=data, status=status.HTTP_201_CREATED)

