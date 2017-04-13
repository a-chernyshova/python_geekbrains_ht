# -*- coding: utf-8 -*-
import exifread
from os import listdir
import os
print('Task7: Find image created before others')


def oldest_one():
    file_list = listdir(os.getcwd())
    file_list = filter(lambda x: x.endswith('.jpg') or x.endswith('.PNG') or x.endswith('.png') or x.endswith('GPG'), file_list)
    oldest = {'res': [0, 0, 0]}
    # создаем словарь имя файла: дата создания
    for file in file_list:
        f = open(file, 'rb')
        tags = exifread.process_file(f)
        oldest[file] = list(map(int, str(tags.get('EXIF DateTimeOriginal'))[:10].split(':')))
    # создаем список дат
    list_dates = list(oldest.values())
    # находим наиболее старую дату
    for i in list_dates:
        if list_dates[0][0] == 0:
            list_dates[0] = i
        elif i[0] < list_dates[0][0]:
            list_dates[0] = i
        elif i[0] == list_dates[0][0]:
            if i[1] == list_dates[0][1]:
                if i[2] < list_dates[0][2]:
                    list_dates[0] = i
            elif i[1] < oldest[0][1]:
                list_dates[0] = i
    # ищем в словаре соответствующее название файла
    for k, v in oldest.items():
        if v == list_dates[0]:
            return k

print(oldest_one())
