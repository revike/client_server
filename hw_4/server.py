from socket import socket, AF_INET, SOCK_STREAM
from sys import argv
import time
from common.utils import get_addr, send_message, presence_request, get_data_from_message, hand_client_msg


times = time.ctime(time.time())
presence_msg = {
    "action": "presence",
    "time": times,
    "type": "status",
    "user":
        {"account_name":"Evgenii",
         "status": "Yep, I am here!"
         }
}


def main():
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


def parsing_server(s, server_msg):
    if 'action' in server_msg.keys():
        if server_msg['action'] == 'probe':
            send_message(s, presence_msg)
            return server_msg, 'action'

    elif 'response' in server_msg.keys():
        server_response = {'response': server_msg['response'], 'time': server_msg['time'],
                           'contents': server_msg['alert'], 'type': 'alert'}
        if server_msg['alert']:
            return server_response, 'response'
        elif server_msg['error']:
            server_response['contents'] = server_msg['error']
            server_response['type'] = 'error'
        else:
            server_response['response'] = 'unknown'
            server_response['time'] = times
            server_response['contents'] = [server_msg]
            server_response['type'] = 'unknown'
        return server_response, 'response'
    else:
        server_response = {'response': 'unknown', 'time': times,
                           'contents': [server_msg], 'type': 'unknown'}
        return server_response, 'response'


if __name__ == '__main__':
    main()
