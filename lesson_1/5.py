# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип
# на кириллице.

import subprocess
yandex = ['ping', 'yandex.ru']
youtube = ['ping', 'youtube.com']
subproc_ping = subprocess.Popen(yandex, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))

subproc_ping = subprocess.Popen(youtube, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))