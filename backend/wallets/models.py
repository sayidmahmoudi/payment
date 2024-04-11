import uuid

from django.db import models


class Transaction(models.Model):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    TYPE_CHOICES = (
        (DEPOSIT, DEPOSIT),
        (WITHDRAW, WITHDRAW),
    )
    type = models.CharField(choices=TYPE_CHOICES, max_length=10, null=False, db_index=True)

    CREATED = "created"
    FAILED = "failed"
    DONE = "done"
    STATE_CHOICES = (
        (CREATED, CREATED),
        (FAILED, FAILED),
        (DONE, DONE),
    )
    state = models.CharField(choices=STATE_CHOICES, max_length=10, null=False, db_index=True)

    amount = models.BigIntegerField()
    wallet = models.ForeignKey('Wallet', on_delete=models.PROTECT, related_name="transactions")
    execute_time = models.DateTimeField()


class Wallet(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    balance = models.BigIntegerField(default=0)
