# -*- coding: utf-8 -*-
# Task: синхронизировать работу потоков с помощью блокировок
import threading
import time
import datetime


def fulfill_file(filename, n, text):
    lock = threading.Lock()
    file = open(filename, 'a')
    for i in range(n):
        print("Процесс %s запрашивает ресурс %s" % (text, filename))
        lock.acquire()
        file.write('%s INFO:Process %s logging(%s)\n' % (str(datetime.datetime.today()), text, i))
        print("Процесс %s выполняется" % text)
        time.sleep(0.6)
        lock.release()
    file.close()


def thread_runner():
    thread_1 = threading.Thread(target=fulfill_file, args=('test3.txt', 10, "'thread 1'"))
    thread_2 = threading.Thread(target=fulfill_file, args=('test3.txt', 20, "'thread 2'"))
    thread_3 = threading.Thread(target=fulfill_file, args=('test3.txt', 5, "'thread 3'"))
    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_1.join()
    thread_2.join()
    thread_3.join()
thread_runner()
