import time
from socket import socket, AF_INET, SOCK_STREAM
from common.configs import HOST, PORT
from common.utils import send_message, get_data_from_message

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

msg = {
        "action": "presence",
        "time": int(time.time()),
        "type": "status",
        "user": {
            "account_name": "Evgenii",
            "status": "Yep, I am here!"
        }
    }

s.send(bytes(send_message(msg).encode('utf-8')))
data = get_data_from_message(s.recv(4096))
print(data)
s.close()
