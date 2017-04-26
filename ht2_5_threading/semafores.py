# -*- coding: utf-8 -*-
# Task: Cинхронизировать работу потоков с помощью семафоров
from threading import BoundedSemaphore
import threading
import time

sem = BoundedSemaphore(2)
lock = threading.Lock()


def fulfill_file(filename, n, text):
    file = open(filename, 'a')
    for i in range(n):
        sem.acquire()
        print("Процесс %s выполняется" % text)
        time.sleep(1)
        sem.release()
    file.close()


def thread_runner():
    thread_1 = threading.Thread(target=fulfill_file, args=('test3.txt', 10, "'thread 1'"))
    thread_2 = threading.Thread(target=fulfill_file, args=('test3.txt', 20, "'thread 2'"))
    thread_3 = threading.Thread(target=fulfill_file, args=('test3.txt', 5, "'thread 3'"))
    thread_4 = threading.Thread(target=fulfill_file, args=('test3.txt', 5, "'thread 4'"))
    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()
    thread_1.join()
    thread_2.join()
    thread_3.join()
    thread_4.join()

thread_runner()
# Вывод в консоль идет одновременно только из двух потоков, а не из 4х