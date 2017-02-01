# -*- coding: utf-8 -*-
import sys, os
# task-1:
# Write script which create directories dir_1 - dir_9 in that folder where script was ran.
# Create the second one which will remove all this directories
def create_dir():
    for i in [1,2,3,4,5,6,7,8,9]:
        dir_path = os.path.join(os.getcwd(), 'dir_'+str(i))
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            print('Такая директория уже существует')
def delete_dir():
    try:
        for i in [1,2,3,4,5,6,7,8,9]:
            dir_path = os.path.join(os.getcwd(), 'dir_'+str(i))
            #os.removedirs(dir_path)
            os.rmdir(dir_path)
    except FileExistsError:
        print('Nothing to remove')
#create_dir()
#delete_dir()

# Task-2:
# Create a script which show folders current directory
def show_folders():
    list_res = os.listdir(os.getcwd())
    for i in list_res[:]:
        if '.' in i:
            list_res.remove(i)
    return list_res

print(show_folders())

# Task-3:
# Напишите скрипт создающий копию файла, из которого запущен данный скрипт
def copy_current_file():
    current_file = (sys.argv[0].split('/'))[-1]
    f = open(sys.argv[0], 'r', encoding='UTF-8')
    _temp = ''
    for line in f:
        _temp += line
    f.close()
    name = current_file.split('.')[0]
    _type = current_file.split('.')[1]
    path = os.path.join(name + '_copy.' + _type)
    f = open(path, 'w', encoding='UTF-8')
    f.write(_temp)
    f.close()
    print('Copy of ' + current_file + ' created')
    pass

copy_current_file()

#Normal
# Task-1_normal:
# Напишите небольшую консольную утилиту, позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов: 1, 3,4, программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел", "Невозможно создать/удалить/прейти"

# Для решения данной задачи используйте алоритмы из задания easy,
# оформленныйе в виде соответствующих функций, и импортированные в данный файл из easy.py


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

# P.S. По возможности, сделайте кросс-платформеную реализацию.