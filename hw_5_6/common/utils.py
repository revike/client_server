import json


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
