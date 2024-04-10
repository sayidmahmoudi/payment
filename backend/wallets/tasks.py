from celery import shared_task

from wallets.models import Wallet, Transaction


@shared_task(queue="withdraw")
def withdraw()-> None:
    pass
