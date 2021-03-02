import time
from json import JSONDecodeError
from socket import socket, AF_INET, SOCK_STREAM
from sys import argv

from common.utils import get_data_from_message, get_addr, send_message
from log.client_log_config import logger_client


times = time.ctime(time.time())
presence_msg = {
    "action": "presence",
    "time": times,
    "type": "status",
    "user":
        {"account_name": "Evgenii",
         "status": "Yep, I am here!"
         }
}


@logger_client
def main():
    try:
        addr, port = get_addr(argv, 'common/configs.json')
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((addr, int(port)))

        data = s.recv(4096)
        server_msg = get_data_from_message(data)
        server_resp, msg_type = parsing_server(s, server_msg)
        print(server_resp)
    except JSONDecodeError:
        data = 'JSONDecodeError'
    except FileNotFoundError:
        data = 'FileNotFoundError'
    except TypeError:
        data = 'TypeError'
    except ValueError:
        data = 'Value Error'

    return data


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
