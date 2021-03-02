import time
from socket import socket, AF_INET, SOCK_STREAM

from common.configs import HOST, PORT
from common.utils import send_message

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

while True:
    client, addr = s.accept()
    data = client.recv(4096)
    print(data.decode('utf-8'))

    msg = msg_response = {
        "response": '200',
        "time": int(time.time()),
    }

    client.send(bytes(send_message(msg).encode('utf-8')))
    client.close()
