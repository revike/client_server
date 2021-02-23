import logging
from logging import handlers


def logger_server(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        formatter = logging.Formatter("%(asctime)s - %(levelname)-8s - %(message)s")

        time_handler = handlers.TimedRotatingFileHandler(
            'log/server/server.log', encoding='utf-8',
            when='midnight', interval=1
        )
        time_handler.setFormatter(formatter)

        log = logging.getLogger('server')
        log.setLevel(logging.INFO)
        log.addHandler(time_handler)
        if res['response'] == 200:
            log.info('The client is here')
        elif res['response'] == 400:
            log.critical('Critical Error 400')

        return res

    return wrapper
