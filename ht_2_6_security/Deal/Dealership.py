# -*- coding: utf-8 -*-
import mysql.connector
from mysql.connector import Error
import time
import hashlib
import datetime


class Dealership:

    # при создании объекта класса, коннектится к базе
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        try:
            connection = mysql.connector.connect(host=host,
                                                 database=database,
                                                 user=user,
                                                 password=password)
            if connection.is_connected():
                print(str(datetime.datetime.today())[:19] + " INFO: Connected to MySQL db")
        except Error as e:
            print(e)

    # закрытие соединения с бд
    def break_connection(self):
        connection = mysql.connector.connect(host=self.host,
                                             database=self.database,
                                             user=self.user,
                                             password=self.password)
        connection.close()
        print(str(datetime.datetime.today())[:19] + " INFO: Соединение закрыто")

    # вывести на экран все модели
    def printer_models(self):
        try:
            sql = "select  distinct cars.car_model, dealership.amount from dealership join cars on cars.id_" \
                  "car=dealership.id_car group by cars.car_model;"
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            c = connection.cursor()
            c.execute(sql)
            print(str(datetime.datetime.today())[:19] + " INFO: Выведен список моделей автомобилей, доступных в "
                                                        "автоцентре в output")
            rows = c.fetchall()
            #rows.insert(0, ("№", "Model name"))
            return rows
        except Error as e:
            # вывод и в лог и в GUI
            print(e)
            return e

    # вывести на экран всех производителей
    def printer_makers(self):
        try:
            sql = "select  distinct cars.maker from dealership join cars on cars.id_car=dealership.id_car"
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            c = connection.cursor()
            c.execute(sql)
            print(str(datetime.datetime.today())[:19] + " INFO: Выведен список производителей автомобилей, доступных в "
                                                        "автоцентре в output")
            rows = c.fetchall()
            print(rows)
            return rows
        except Error as e:
            print(e)
            return e

    # Вывести на экран все доступные автомобили салона
    def printer_car_dealership(self):
        try:
            sql = "select dealership.id, cars.car_model, cars.maker, cars.car_engine, cars.cost, dealership.amount" \
                  " from dealership join cars on cars.id_car=dealership.id_car"
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            c = connection.cursor()
            c.execute(sql)
            print(str(datetime.datetime.today())[:19] + "INFO: Выведен подробный список автомобилей, доступных в "
                                                        "автоцентре в output")
            rows = c.fetchall()
            for row in rows:
                print(row)
            return rows
        except Error as e:
            print(e)
            return e

    # Список автомобилей не в наличии в автосалоне
    def printer_not_available_car(self):
        try:
            sql = "select distinct cars.car_model, cars.maker, cars.car_engine, cars.cost from cars " \
                  "where id_car not in (select id_car from dealership);"
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            c = connection.cursor()
            c.execute(sql)
            print(str(datetime.datetime.today())[:19] + " INFO: Список автомобилей, не доступных в автоцентре на "
                                                        "данный момент в output")
            rows = c.fetchall()
            return rows
        except Error as e:
            print(e)
            return e

    # Добавление записи в таблицу Cars
    def add_car(self, car_model, maker, year_production, car_engine, cost):
        try:
            id_car = "select max(id_car) from cars;"
            sql = "INSERT INTO Cars(id_car, car_model, maker, year_production, car_engine, cost)" \
                      " VALUES(%s,%s,%s,%s,%s,%s)"

            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            c = connection.cursor()
            c.execute(id_car)

            id_car = c.fetchall()
            id_car = list(id_car)[0][0] + 1
            print(id_car)
            args = (id_car, car_model, maker, year_production, car_engine, cost)
            c.execute(sql, args)
            connection.commit()
            info = (str(datetime.datetime.today())[:19] + " INFO: Модель {} добавлена в таблицу Cars".format(args))
            print(info)
            return info
        except Error as e:
            print(e)
            return e

    # Добавление записи в связанные таблицы Cars, Lobbies
    def add_lorry(self, id_car, car_model, maker, year_production, car_engine, cost, weight_limit):
        try:
            sql1 = "INSERT INTO Cars(id_car, car_model, maker, year_production, car_engine, cost)" \
                      " VALUES(%s, %s, %s, %s, %s, %s)"
            args1 = (id_car, car_model, maker, year_production, car_engine, cost)
            sql2 = "INSERT INTO Lorries(id_car, weight_limit) VALUES(%s, %s)"
            args2 = (id_car, weight_limit)
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            c = connection.cursor()
            c.execute(sql1, args1)
            c.execute(sql2, args2)
            connection.commit()
            info = (str(datetime.datetime.today())[:19] + " INFO: Модель {}{} добавлена в таблицы Cars, Lorries".format(args1, args2))
            print(info)
            return info
        except Error as e:
            print(e)
            return e

    # Добавление автомобиля в салон
    def add_car_to_dealership(self, id_car, amount):
        try:
            sql = "INSERT INTO dealership(id_car, amount) VALUES(%s,%s)"
            args = (id_car, amount)
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            c = connection.cursor()
            c.execute(sql, args)
            connection.commit()
            info = (str(datetime.datetime.today())[:19] + " INFO: Модель {} добавлена в таблицу Dealership".format(args))
            print(info)
            return info
        except Error as e:
            print(e)
            return e

    # Изменить кол-во автомобилей в салоне по id
    def update_amount(self, id_row, amount):
        try:
            sql = "UPDATE dealership SET amount = %s WHERE id = %s"
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            c = connection.cursor()
            c.execute(sql, (amount, id_row))
            connection.commit()
            info = (str(datetime.datetime.today())[:19] + " INFO: Обновлена запись {} в таблице Dealership".format(id_row))
            print(info)
            return info
        except Error as e:
            print(e)
            return e

    # для выпадающих списков - взвращает словарь из связанных таблиц
    def return_dict(self):
        sql = "select d.id, cars.car_model from dealership d join cars on d.id_car = cars.id_car;"
        result = {}
        try:
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            c = connection.cursor()
            c.execute(sql)
            rows = c.fetchall()
            for row in rows:
                result[row[0]] = row[1]
            return result
        except Error as e:
            print(e)
            return e

    # для выпадающих списков - взвращает словарь
    def retrive_from_one_db(self, name_db, column1, column2):
        sql = "select {}, {} from {};".format(column1, column2, name_db)
        result = {}
        try:
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            c = connection.cursor()
            c.execute(sql)
            rows = c.fetchall()
            for row in rows:
                result[row[0]] = row[1]
            return result
        except Error as e:
            print(e)
            return e

    # Удалить линейку автомобилей из салона - ПОЧЕМУ НЕ РАБОТАЕТ??
    def delete_car_from_dealership(self, id_row):
        try:
            sql = "DELETE FROM dealership WHERE id = %s"
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            c = connection.cursor()
            c.execute(sql, (id_row,))
            connection.commit()
            info = (str(datetime.datetime.today())[:19] + " INFO: Удалена запись {} в таблице Dealership".format(id_row))
            print(info)
            return info
        except Error as e:
            print(e)
            return e

    # Обновить цену машины
    def update_car(self, id_car, cost):
        try:
            sql = "UPDATE cars SET cost = %s WHERE id_car = %s"
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            c = connection.cursor()
            c.execute(sql, (cost, id_car))
            connection.commit()
            info = (str(datetime.datetime.today())[:19] + " INFO: Обновлена запись {} в таблице Car".format(id_car))
            print(info)
            return info
        except Error as e:
            print(e)
            return e

    # Обновить грузоподъемность
    def update_lorry(self, id_lorry, weight_limit):
        try:
            sql = "UPDATE lorries SET weight_limit = %s WHERE id_lorry = %s"
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            c = connection.cursor()
            c.execute(sql, (weight_limit, id_lorry))
            connection.commit()
            info = (str(datetime.datetime.today())[:19] + " INFO: Обновлена запись {} в таблице Lorry".format(id_lorry))
            print(info)
            return info
        except Error as e:
            print(e)
            return e

    def delete_car(self, id_car):
        try:
            sql = "DELETE FROM cars WHERE id_car = %s"
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            c = connection.cursor()
            c.execute(sql, (id_car,))
            connection.commit()
            info = (str(datetime.datetime.today())[:19] + " INFO: Удалена запись ID{} в таблице Cars".format(id_car))
            print(info)
            return info
        except Error as e:
            print(e)
            return e

    # Удаление записей из связанных таблиц Cars, Lorries по id_car
    # Почему то не выдает ошибку при удалении не существующей записи
    def delete_lorry(self, id_car):
        try:
            sql1 = "DELETE FROM lorries WHERE id_car = %s"
            sql2 = "DELETE FROM cars WHERE id_car = %s"
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            c = connection.cursor()
            c.execute(sql1, (int(id_car),))
            c.execute(sql2, (int(id_car),))
            connection.commit()
            info = (str(datetime.datetime.today())[:19] + " INFO: Удалена запись ID{} в таблицах Lorries, Cars".format(id_car))
            print(info)
            return info
        except Error as e:
            print(e)
            return e

    # Поиск модели в Car_dealership
    def search_car_model(self, model):
        try:
            sql = "SELECT dealership.id, cars.car_model, cars.year_production, cars.car_engine, " \
                  "cars.cost, dealership.amount FROM dealership JOIN cars on cars.id_car = dealership.id_car " \
                  "where cars.car_model = %s;"
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            c = connection.cursor()
            c.execute(sql, (model,))
            rows = c.fetchall()
            print(str(datetime.datetime.today())[:19] + " INFO: Результаты поиска модели {} в таблице Dealership".format(model))
            return rows
        except Error as e:
            print(e)
            return e

    # Поиск по производителю в Car_dealership
    def search_car_maker(self, maker):
        try:
            sql = "SELECT dealership.id, cars.car_model, cars.year_production, cars.car_engine, " \
                  "cars.cost, dealership.amount FROM dealership JOIN cars on cars.id_car = dealership.id_car " \
                  "where cars.maker = %s;"
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            c = connection.cursor()
            c.execute(sql, (maker,))
            rows = c.fetchall()
            print(str(datetime.datetime.today())[:19] + " INFO: Результаты поиска моделей по производителю {} в таблице"
                                                        " Dealership".format(maker))
            return rows
        except Error as e:
            print(e)
            return e

    def export_to_file(self, text, filename, rows):
        # lock = threading.BoundedSemaphore(2)
        # lock.acquire()
        for row in rows:
            filename.write(text + str(row)+'\n')
            time.sleep(0.2)
        # lock.release()

    def authorization(self, log, pas):
        try:
            sql = "SELECT Role FROM users WHERE Login = %s and Password = %s"
            conn = mysql.connector.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password)
            connection = conn.cursor()
            h = pas.encode()
            h = hashlib.md5(h).hexdigest()
            connection.execute(sql, (log, h))
            rows = connection.fetchall()
            if rows == []:
                rows = ['e', 'r', 'r', 'o', 'r']
            return rows[0]
        except Error as e:
            return e

    def create_user(self, log, pas, role):
        try:
            sql = "insert into users (login, password, role) values (%s, %s, %s);"
            args = (log, pas, int(role))
            conn = mysql.connector.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password)
            c = conn.cursor()
            c.execute(sql, args)
            conn.commit()
            roles = {0: 'admin', 1: 'regular', 2: 'reader'}
            info = "New user {} with role {} was added to DB".format(log, roles[int(role)])
            print(str(datetime.datetime.today())[:19], info)
            return info
        except Error as e:
            return e

    def printer_users(self):
        try:
            sql = "SELECT * from users;"
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            c = connection.cursor()
            c.execute(sql,)
            rows = c.fetchall()
            print("INFO: Выведены все пользователи из таблицы Users")
            return rows
        except Error as e:
            print(e)
            return e

Dealership1 = Dealership('localhost', 'dealership', 'root', 'password')
