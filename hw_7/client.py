from socket import socket, AF_INET, SOCK_STREAM

address = ('localhost', 8888)


def client_1():
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(address)
        while True:
            msg = input('Your message: ')
            if msg == 'exit':
                break
            if msg:
                sock.send(msg.encode('utf-8'))
                data = sock.recv(1024).decode('utf-8')
                print(f'Response: {data}')
            else:
                client_2()


def client_2():
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(address)
        while True:
            data = sock.recv(1024).decode('utf-8')
            if data:
                print(f'Response: {data}')


if __name__ == '__main__':
    client_1()
