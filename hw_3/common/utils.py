import json


def get_data_from_message(some_response: bytes):
    return json.loads(some_response.decode('utf-8'))


def send_message(some_data: dict):
    return json.dumps(some_data)
