"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать
результаты из байтовового в строковый тип на кириллице.
"""
import subprocess

pings = [
    ['ping', 'yandex.ru'],
    ['ping', 'youtube.com']
]

for ping in pings:
    subproc_ping = subprocess.Popen(ping, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))
