from rest_framework import serializers

from wallets.models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ("uuid", "balance")
        read_only_fields = ("uuid", "balance")


class DepositSerializer(serializers.Serializer):
    amount = serializers.IntegerField()

    def validate_amount(self, amount):
        if amount <= 0:
            raise serializers.ValidationError("value must be positive")
        return amount
