import time
from socket import socket, AF_INET, SOCK_STREAM
from sys import argv
from common.utils import get_addr, send_message, get_data_from_message
from log.server_log_config import logger_server

times = time.ctime(time.time())

response_200 = {
    'response': 200,
    'time': times,
    'alert': 'Welcome!'
}

response_400 = {
    'response': 400,
    'time': times,
    'error': 'Error'
}

presence_request = {
    'action': 'probe',
    'time': times
}


def main():
    addr, port = get_addr(argv, 'common/configs.json')
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', int(port)))
    s.listen(1)

    while True:
        client, addr = s.accept()
        send_message(client, presence_request)

        data = (client.recv(4096))

        msg = get_data_from_message(data)
        response = hand_client_msg(msg)
        print(response)

        send_message(client, msg)
        client.close()


@logger_server
def hand_client_msg(msg):
    if msg['action'] == 'presence':
        return response_200
    else:
        return response_400


if __name__ == '__main__':
    main()
