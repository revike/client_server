from socket import socket, AF_INET, SOCK_STREAM
from sys import argv

from common.utils import get_addr, send_message, presence_request, get_data_from_message, hand_client_msg

addr, port = get_addr(argv, 'common/configs.json')
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', int(port)))
s.listen(5)

while True:
    client, addr = s.accept()
    send_message(client, presence_request)

    data = (client.recv(4096))
    msg = get_data_from_message(data)

    res = hand_client_msg(data)

    send_message(client, res)
    client.close()
