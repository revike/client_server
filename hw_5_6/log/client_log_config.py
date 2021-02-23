import logging


def logger_client(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        formatter = logging.Formatter("%(asctime)s - %(levelname)-8s - %(message)s")

        file_handler = logging.FileHandler('log/client/client.log', encoding='utf-8')
        file_handler.setFormatter(formatter)

        log = logging.getLogger('client')
        log.setLevel(logging.INFO)
        log.addHandler(file_handler)
        if res == "FileNotFoundError":
            log.critical('FileNotFoundError')
        if res == "TypeError":
            log.critical('TypeError')
        if res == "JSONDecodeError":
            log.critical('JSONDecodeError')
        if res == "Value Error":
            log.critical('Value Error')
        if b'action' in res:
            log.info('Server action')
        if b'response' in res:
            log.warning('Sever action unknown')

        return res

    return wrapper
