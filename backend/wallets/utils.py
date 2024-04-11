import requests

from backend.settings import THIRD_PARTY_URL


def request_third_party_deposit():
    response = requests.post(THIRD_PARTY_URL)
    return response.json()
