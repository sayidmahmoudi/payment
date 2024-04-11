from celery import shared_task
from django.utils import timezone

from wallets.models import Transaction
from wallets.services import WithdrawService


@shared_task(queue="withdraw")
def withdraw() -> None:
    transactions = Transaction.objects.filter(
        type=Transaction.WITHDRAW,
        state=Transaction.CREATED,
        execute_time__lte=timezone.now()
    )
    for transaction in transactions:
        WithdrawService.withdraw(transaction.id)
