import uuid

from django.db import models


class Transaction(models.Model):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    TYPE_CHOICES = (
        (DEPOSIT, DEPOSIT),
        (WITHDRAW, WITHDRAW),
    )
    type = models.CharField(choices=TYPE_CHOICES, max_length=10, null=False)

    CREATED = "created"
    DONE = "done"
    STATE_CHOICES = (
        (CREATED, CREATED),
        (DONE, DONE),
    )
    state = models.CharField(choices=STATE_CHOICES, max_length=10, null=False)

    amount = models.BigIntegerField()
    wallet = models.ForeignKey('Wallet', on_delete=models.PROTECT, related_name="transactions")
    execute_time = models.DateTimeField(auto_now_add=True)


class Wallet(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    balance = models.BigIntegerField(default=0)
