import requests


def call_get_api(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()
