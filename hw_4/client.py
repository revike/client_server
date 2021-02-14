from socket import socket, AF_INET, SOCK_STREAM
from sys import argv

from common.utils import get_data_from_message, get_addr, parsing_server

addr, port = get_addr(argv, 'common/configs.json')
s = socket(AF_INET, SOCK_STREAM)
connect = s.connect((addr, int(port)))

data = s.recv(4096)
if data:
    server_msg = get_data_from_message(data)
    server_resp, msg_type = parsing_server(s, server_msg)
    print(server_resp)

s.close()
