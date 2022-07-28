# -*- coding: utf=8-*-

import socket
import sys

HOST, PORT = '192.168.1.100', 8000
data = " ".join(sys.argv[1:])

# Создать сокет (SOCK_STREAM означает TCP сокет)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Подключиться к серверу и отправить данные
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    # Получение данных с сервера и завершение работы
    received = str(sock.recv(1024), "utf-8")

print("Sent:     {}".format(data))
print("Received: {}".format(received))
