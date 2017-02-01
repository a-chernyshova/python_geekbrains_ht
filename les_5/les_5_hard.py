# -*- coding: utf-8 -*-
#Hard
# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд(переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл(запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным(full_path) - в Linux начинается с /, в Windows с имени диска
# все остальные пути считать относительными
# Важно! Все операции должны выполняться в той директории, в который вы находитесь. Исходной директорией считать ту,
# в которой был запущен скрипт.
import os
import sys
from les_5 import copy_current_file
from les_5_normal import rem_folder
print('sys.argv = ', sys.argv)

def ls():
    print(os.getcwd())

def cd():
    print("Временно не работает")

def print_help():
    print("help - получение справки")
    print("copy<file_name> - создает копию указанного файла"),
    print("remove<file_name> - удаляет указанный файл(запросить подтверждение операции)"),
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную"),
    print("ls - отображение полного пути текущей директории")

do = {
    "help": print_help,
    "copy":copy_current_file,
    "remove":rem_folder,
    "cd":cd,
    "ls":ls
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ(module hard)")