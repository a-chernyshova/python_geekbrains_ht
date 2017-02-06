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
            print('директория {} создана'.format(dir_path))
        except FileExistsError:
            print('{} директория уже существует'.format(dir_path))
def delete_dir():
    try:
        for i in [1,2,3,4,5,6,7,8,9]:
            dir_path = os.path.join(os.getcwd(), 'dir_'+str(i))
            #os.removedirs(dir_path)
            os.rmdir(dir_path)
            print('{} директория удалена'.format(dir_path))
    except FileExistsError:
        print('Nothing to remove')

# Task-2:
# Create a script which show folders current directory
def show_folders():
    list_res = os.listdir(os.getcwd())
    list_res = [i for i in list_res[:] if '.' not in i]
    #for i in list_res[:]:
    #    if '.' in i:
    #        list_res.remove(i)
    return list_res

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

if __name__ == '__main__':
    copy_current_file()
    create_dir()
    delete_dir()
    print(show_folders())
