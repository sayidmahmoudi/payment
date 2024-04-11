from django.utils import timezone
from rest_framework import serializers

from wallets.models import Wallet, Transaction


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ("uuid", "balance")
        read_only_fields = ("uuid", "balance")


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("type", "state", "amount")


class DepositSerializer(serializers.Serializer):
    amount = serializers.IntegerField(required=True)

    def validate_amount(self, amount):
        if amount <= 0:
            raise serializers.ValidationError("value must be positive")
        return amount


class WithdrawSerializer(serializers.Serializer):
    amount = serializers.IntegerField(required=True)
    execute_time = serializers.DateTimeField(required=True)

    def validate_amount(self, amount):
        if amount <= 0:
            raise serializers.ValidationError("value must be positive")
        return amount

    def validate_execute_time(self, execute_time):
        if execute_time <= timezone.now():
            raise serializers.ValidationError("can't give past execute time")
        return execute_time
