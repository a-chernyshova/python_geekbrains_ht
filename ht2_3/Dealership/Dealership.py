# -*- coding: utf-8 -*-
import mysql.connector
from mysql.connector import Error


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
                print("INFO: Connected to MySQL db")
        except Error as e:
            print(e)

    # закрытие соединения с бд
    def break_connection(self):
        connection = mysql.connector.connect(host=self.host,
                                             database=self.database,
                                             user=self.user,
                                             password=self.password)
        connection.close()
        print("INFO: Соединение закрыто")

    # вывести на экран все модели
    def printer_models(self):
        try:
            sql = "select cars.car_model, dealership.amount from dealership join cars on cars.id_car=dealership.id_car"
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            c = connection.cursor()
            c.execute(sql)
            print("Список моделей автомобилей, доступных в автоцентре")
            rows = c.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(e)

    # вывести на экран всех производителей
    def printer_makers(self):
        try:
            sql = "select cars.maker from dealership join cars on cars.id_car=dealership.id_car"
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            c = connection.cursor()
            c.execute(sql)
            print("Список производителей автомобилей, доступных в автоцентре")
            rows = c.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(e)

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
            print("Подробный список автомобилей, доступных в автоцентре")
            rows = c.fetchall()

            for row in rows:
                print(row)
        except Error as e:
            print(e)

    # Список автомобилей не в наличии в автосалоне
    def printer_not_available_car(self):
        try:
            sql = "select cars.car_model, cars.maker, cars.car_engine, cars.cost from cars " \
                  "where id_car not in (select id_car from dealership);"
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            c = connection.cursor()
            c.execute(sql)
            print("Список автомобилей, не доступных в автоцентре на данный момент")
            rows = c.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(e)

    # Добавление записи в таблицу Cars
    def add_car(self, id_car, car_model, maker, year_production, car_engine, cost):
        try:
            sql = "INSERT INTO Cars(id_car, car_model, maker, year_production, car_engine, cost)" \
                      " VALUES(%s,%s,%s,%s,%s,%s)"
            args = (id_car, car_model, maker, year_production, car_engine, cost)
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            c = connection.cursor()
            c.execute(sql, args)
            connection.commit()
            print("INFO: Модель {} добавлена в таблицу Cars".format(args))
        except Error as e:
            print(e)

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
            print("INFO: Модель {}{} добавлена в таблицы Cars, Lorries".format(args1, args2))
        except Error as e:
            print(e)

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
            print("INFO: Модель {} добавлена в таблицу Dealership".format(args))
        except Error as e:
            print(e)

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
            print("INFO: Обновлена запись {} в таблице Dealership".format(id_row))
        except Error as e:
            print(e)

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
            print("INFO: Удалена запись {} в таблице Dealership".format(id_row))
        except Error as e:
            print(e)

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
            print("INFO: Обновлена запись {} в таблице Car".format(id_car))
        except Error as e:
            print(e)

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
            print("INFO: Обновлена запись {} в таблице Lorry".format(id_lorry))
        except Error as e:
            print(e)

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
            print("INFO: Удалена запись ID{} в таблице Cars".format(id_car))
        except Error as e:
            print(e)

    # Удаление записей из связанных таблиц Cars, Lorries по id_car
    def delete_lorry(self, id_car):
        try:
            sql1 = "DELETE FROM lorries WHERE id_car = %s"
            sql2 = "DELETE FROM cars WHERE id_car = %s"
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            c = connection.cursor()
            c.execute(sql1, (id_car, ))
            c.execute(sql2, (id_car,))
            connection.commit()
            print("INFO: Удалена запись ID{} в таблицах Lorries, Cars".format(id_car))
        except Error as e:
            print(e)

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
            print("INFO: Результаты поиска модели {} в таблице Dealership".format(model))
            for row in rows:
                print(row)
        except Error as e:
            print(e)
        pass

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
            print("INFO: Результаты поиска моделей по производителю {} в таблице Dealership".format(maker))
            for row in rows:
                print(row)
        except Error as e:
            print(e)
        pass
