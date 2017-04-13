# -*- coding: utf-8 -*-
#play with encoding

s1 = open('test1.txt', 'w+')
s1.write('task1:\n Записать строку символов в текстовый файл\n и вывести содержимое файла.\n')
s1.seek(0, 0)
for line in s1:
    print(line)
s1.close()

s2 = open('test2.txt', 'wb+')
s2.write(bytes('task2:\nЗаписать строку символов в файл,явным указанием кодировки utf-8\nPrint out file.\n', 'utf-8'))
s2.seek(0, 0)
for line in s2: print(line)
s2.close()

print('Task3\n Декодировать содержимое файла из предыдущего задания.\n')
s3 = open('test2.txt', 'r', encoding='utf-8')
print(s3.read())
s3.close()

s4 = open('test_3.txt', 'wb+')
s4.write(bytes('Task4\nWrite down string into binary file.\n', 'ASCII'))
s4.seek(0, 0)
for line in s4:
    print(line)
s4.close()

s5 = open('test_4.txt', 'wb+')
s5.write(bytes('Task5.\n Write down string into the file encoded latin-1.\n Print out file', 'latin-1'))
s5.seek(0, 0)
for line in s5:
    print(line)
s5.close()

print('Task6: Декодировать содержимое файла из предыдущего задания.')
s6 = open('test_4.txt', 'r', encoding='latin-1').read()
print(s6)
