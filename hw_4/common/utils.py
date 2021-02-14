import json
import time

times = time.ctime(time.time())
presence_request = {
    'action': 'probe',
    'time': times
}

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

presence_msg = {
    "action": "presence",
    "time": times,
    "type": "status",
    "user":
        {"account_name":"Evgenii",
         "status": "Yep, I am here!"
         }
}


def get_data_from_message(some_response):
    return json.loads(some_response.decode('utf-8'))


def send_message(some_data, msg):
    res = json.dumps(msg)
    some_data.send(res.encode('utf-8'))


def get_addr(argv, file):
    if len(argv) == 3:
        addr, port = argv[1], get_settings(file)[1]
    elif len(argv) == 5:
        if argv[1] == '-a':
            addr, port = argv[2], argv[4]
        elif argv[1] == '-p':
            addr, port = argv[4], argv[2]
    else:
        addr, port = get_settings(file)[0], get_settings(file)[1]

    return addr, port


def get_settings(file):
    with open(file, encoding='utf-8') as f:
        result = json.load(f)
    return result['HOST'], result['PORT']


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


def hand_client_msg(data):
    if data:
        print(response_200)
    else:
        print(response_400)
