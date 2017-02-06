# -*- coding: utf-8 -*-
import sys, os
from les_5 import show_folders

#Normal
# Task-1_normal:# Напишите небольшую консольную утилиту, позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов: 1, 3,4, программа запрашивает название папки # и выводит результат действия:
# "Успешно создано/удалено/перешел", "Невозможно создать/удалить/прейти"
# Для решения данной задачи используйте алоритмы из задания easy,
# оформленныйе в виде соответствующих функций, и импортированные в данный файл из easy.py
#print('sys.argv = ', sys.argv)

def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("_goto<path> - перейти в папку")
    print("show_folders - посмотреть содержимое текущей папки")
    print("rem_folder<folder_name> - удалить папку")

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def _goto():
    if not dir_name:
        print("Необходимо указать имя директории")
        return
    try:
        dir_path = os.path.join(os.getcwd(), dir_name)
        os.chdir(dir_path)
        print(dir_name + 'вы здесь')
    except FileNotFoundError:
        print('директории {} не существует'.format(dir_name))

def rem_folder():
    if not dir_name:
        print("Необходимо указать имя директории для удаления вторым параметром")
        return
    try:
        dir_path = os.path.join(os.getcwd(), dir_name)
        os.rmdir(dir_path)
        print(dir_name + ' была удалена')
    except FileNotFoundError:
        print('директории {} не существует'.format(dir_name))

do = {
    "help": print_help,
    "mkdir": make_dir,
    "_goto":_goto,
    "rem_folder":rem_folder,
    "show_folders":show_folders
}

if __name__ == '__main__':
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
            print("Задан неверный ключ (module normal)")
            print("Укажите ключ help для получения справки")