# -*- coding: utf-8 -*-
import time
import hashlib
import datetime
import mysql.connector
from mysql.connector import Error

TIMESTAMP = datetime.datetime.today().strftime("%d.%m.%Y %H:%M:%S")


class Dealership:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        try:
            global connection
            connection = mysql.connector.connect(host=host,
                                                 database=database,
                                                 user=user,
                                                 password=password)
            if connection.is_connected():
                print(TIMESTAMP + " INFO: Connected to MySQL db")
        except Error as e:
            # CR: re-throw exception or exit the program with ERROR. don't allow it to go forward.
            print(e)

    def close_connection(self):
        connection.close()
        info = TIMESTAMP + " INFO: Соединение закрыто"
        print(info)
        return info

    ''' Class methods: '''
    ''' Show all models '''
    def printer_models(self):
        try:
            sql = "select  distinct cars.car_model, dealership.amount from dealership " \
                  "join cars on cars.id_car=dealership.id_car group by cars.car_model;"

            c = connection.cursor()
            c.execute(sql)
            print(TIMESTAMP + " INFO: Выведен список моделей автомобилей, доступных в автоцентре в output")
            rows = c.fetchall()
            return rows
        except Error as e:
            print(e)
            return e

    ''' Show all makers '''
    def printer_makers(self):
        try:
            sql = "select  distinct cars.maker from dealership join cars on cars.id_car=dealership.id_car"

            c = connection.cursor()
            c.execute(sql)
            print(TIMESTAMP + " INFO: Выведен список производителей автомобилей, доступных в автоцентре в output")
            rows = c.fetchall()
            print(rows)
            return rows
        except Error as e:
            print(e)
            return e

    ''' Show all dealership cars '''
    def printer_car_dealership(self):
        try:
            sql = "select dealership.id, cars.car_model, cars.maker, cars.car_engine, cars.cost, " \
                  "dealership.amount from dealership join cars on cars.id_car=dealership.id_car group by cars.car_model"

            c = connection.cursor()
            c.execute(sql)
            print(TIMESTAMP + "INFO: Выведен подробный список автомобилей, доступных в автоцентре в output")
            rows = c.fetchall()
            for row in rows:
                print(row)
            return rows
        except Error as e:
            print(e)
            return e

    ''' List of unavailable cars '''
    def printer_not_available_car(self):
        try:
            sql = "select distinct cars.car_model, cars.maker, cars.car_engine, cars.cost from cars " \
                  "where id_car not in (select id_car from dealership);"

            c = connection.cursor()
            c.execute(sql)
            print(TIMESTAMP + " INFO: Список автомобилей, не доступных в автоцентре на данный момент в output")
            rows = c.fetchall()
            return rows
        except Error as e:
            print(e)
            return e

    ''' Add car to cars table '''
    def add_car(self, car_model, maker, year_production, car_engine, cost):
        try:
            id_car = "select max(id_car) from cars;"
            sql = "INSERT INTO Cars(id_car, car_model, maker, year_production, car_engine, cost)" \
                  "VALUES(%s,%s,%s,%s,%s,%s)"

            c = connection.cursor()
            c.execute(id_car)

            id_car = c.fetchall()
            id_car = list(id_car)[0][0] + 1
            args = (id_car, car_model, maker, year_production, car_engine, cost)
            c.execute(sql, args)
            connection.commit()
            info = (TIMESTAMP + " INFO: Модель {} добавлена в таблицу Cars".format(car_model, maker, year_production))
            print(info)
            return info
        except Error as e:
            print(e)
            return e

    ''' Add car to related tables Cars, Lorries '''
    def add_lorry(self, car_model, maker, year_production, car_engine, cost, weight_limit):
        try:
            id_car1 = "select max(id_car) from cars;"
            sql1 = "INSERT INTO Cars(id_car, car_model, maker, year_production, car_engine, cost) " \
                   "VALUES(%s, %s, %s, %s, %s, %s)"
            sql2 = "INSERT INTO Lorries(id_car, weight_limit) VALUES(%s, %s)"

            c = connection.cursor()
            c.execute(id_car1)
            id_car1 = c.fetchall()
            id_car1 = list(id_car1)[0][0] + 1
            args1 = (id_car1, car_model, maker, year_production, car_engine, cost)
            args2 = (id_car1, weight_limit)
            c.execute(sql1, args1)
            c.execute(sql2, args2)
            connection.commit()
            info = (TIMESTAMP + " INFO: Модель {}{} добавлена в таблицы Cars, Lorries".format(car_model, maker))
            print(info)
            return info
        except Error as e:
            print(e)
            return e

    ''' Add car to dealership '''
    def add_car_to_dealership(self, id_car, amount):
        try:
            sql = "INSERT INTO dealership(id_car, amount) VALUES(%s,%s)"
            args = (id_car, amount)
            c = connection.cursor()
            c.execute(sql, args)
            connection.commit()
            info = (TIMESTAMP + " INFO: Модель {} добавлена в таблицу Dealership".format(args))
            print(info)
            return info
        except Error as e:
            print(e)
            return e

    # Change amount of dealership car with help id
    def update_amount(self, id_row, amount):
        try:
            sql = "UPDATE dealership SET amount = %s WHERE id = %s"
            c = connection.cursor()
            c.execute(sql, (amount, id_row))
            connection.commit()
            info = (TIMESTAMP + " INFO: Обновлена запись {} в таблице Dealership".format(id_row))
            print(info)
            return info
        except Error as e:
            print(e)
            return e

    # Return dict for dropdown lists
    def return_dict(self):
        sql = "select d.id, cars.car_model from dealership d join cars on d.id_car = cars.id_car;"
        result = {}
        try:
            c = connection.cursor()
            c.execute(sql)
            rows = c.fetchall()
            for row in rows:
                result[row[0]] = row[1]
            return result
        except Error as e:
            print(e)
            return e

    def retrive_from_2_tables(self):
        sql = 'select cars.id_car, car_model from cars join lorries on cars.id_car = lorries.id_car;'
        result = {}
        try:
            c = connection.cursor()
            c.execute(sql)
            rows = c.fetchall()
            for row in rows:
                result[row[0]] = row[1]
            return result
        except Error as e:
            print(e)
            return e

    def retrive_cars_only(self):
        sql = 'select cars.id_car, car_model from cars left join dealership on ' \
              'cars.id_car = dealership.id_car where dealership.id_car is NULL;'
        result = {}
        try:
            c = connection.cursor()
            c.execute(sql)
            rows = c.fetchall()
            for row in rows:
                result[row[0]] = row[1]
            return result
        except Error as e:
            print(e)
            return e

    # return dict for dropdown list
    def retrive_from_one_db(self, name_db, column1, column2):
        sql = "select {}, {} from {};".format(column1, column2, name_db)
        result = {}
        try:
            c = connection.cursor()
            c.execute(sql)
            rows = c.fetchall()
            for row in rows:
                result[row[0]] = row[1]
            return result
        except Error as e:
            print(e)
            return e

    # Remove car from dealership
    def delete_car_from_dealership(self, id_row):
        try:
            sql = "DELETE FROM dealership WHERE id = %s"
            c = connection.cursor()
            c.execute(sql, (id_row,))
            connection.commit()
            info = (TIMESTAMP + " INFO: Удалена запись {} в таблице Dealership".format(id_row))
            print(info)
            return info
        except Error as e:
            print(e)
            return e

    # Car cost update
    def update_car(self, id_car, cost):
        try:
            sql = "UPDATE cars SET cost = %s WHERE id_car = %s"
            c = connection.cursor()
            c.execute(sql, (cost, id_car))
            connection.commit()
            info = (TIMESTAMP + " INFO: Обновлена запись {} в таблице Car".format(id_car))
            print(info)
            return info
        except Error as e:
            print(e)
            return e

    # Weight limit update
    def update_lorry(self, id_lorry, weight_limit):
        try:
            sql = "UPDATE lorries SET weight_limit = %s WHERE id_lorry = %s"
            c = connection.cursor()
            c.execute(sql, (weight_limit, id_lorry))
            connection.commit()
            info = (TIMESTAMP + " INFO: Обновлена запись {} в таблице Lorry".format(id_lorry))
            print(info)
            return info
        except Error as e:
            print(e)
            return e

    def delete_car(self, id_car):
        try:
            sql = "DELETE FROM cars WHERE id_car = %s"
            c = connection.cursor()
            c.execute(sql, (id_car,))
            connection.commit()
            info = (TIMESTAMP + " INFO: Удалена запись ID{} в таблице Cars".format(id_car))
            print(info)
            return info
        except Error as e:
            print(e)
            return e

    # Remove row from related tables Cars, Lorries with help id_car
    # FIXME: Почему то не выдает ошибку при удалении не существующей записи
    def delete_lorry(self, id_car):
        try:
            sql1 = "DELETE FROM lorries WHERE id_car = %s"
            sql2 = "DELETE FROM cars WHERE id_car = %s"
            c = connection.cursor()
            c.execute(sql1, (int(id_car),))
            c.execute(sql2, (int(id_car),))
            connection.commit()
            info = (TIMESTAMP + " INFO: Удалена запись ID{} в таблицах Lorries, Cars".format(id_car))
            print(info)
            return info
        except Error as e:
            print(e)
            return e

    # Search model in Car_dealership
    def search_car_model(self, model):
        try:
            sql = "SELECT dealership.id, desc cars.car_model, cars.year_production, cars.car_engine, " \
                  "cars.cost, dealership.amount FROM dealership JOIN cars on " \
                  "cars.id_car = dealership.id_car where cars.car_model = %s;"
            c = connection.cursor()
            c.execute(sql, (model,))
            rows = c.fetchall()
            print(TIMESTAMP + " INFO: Результаты поиска модели {} в таблице Dealership".format(model))
            return rows
        except Error as e:
            print(e)
            return e

    # Search maker in Car_dealership
    def search_car_maker(self, maker):
        try:
            sql = "SELECT dealership.id, desc cars.car_model, cars.year_production, cars.car_engine, " \
                  "cars.cost, dealership.amount FROM dealership JOIN cars on " \
                  "cars.id_car = dealership.id_car where cars.maker = %s;"
            c = connection.cursor()
            c.execute(sql, (maker,))
            rows = c.fetchall()
            print(TIMESTAMP + " INFO: Результаты поиска моделей по производителю {} в "
                              "таблице Dealership".format(maker))
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
            c = connection.cursor()
            h = pas.encode()
            h = hashlib.md5(h).hexdigest()
            c.execute(sql, (log, h))
            rows = c.fetchall()
            if rows == []:
                rows = ['e', 'r', 'r', 'o', 'r']
            return rows[0]
        except Error as e:
            return e

    def create_user(self, log, pas, role):
        try:
            sql = "insert into users (login, password, role) values (%s, %s, %s);"
            args = (log, pas, role)
            c = connection.cursor()
            c.execute(sql, args)
            connection.commit()
            info = "New user {} with role {} was added to DB".format(log, role)
            print(TIMESTAMP, info)
            return info
        except Error as e:
            return e

    def del_user(self, id_user):
        try:
            sql = "DELETE FROM users WHERE id = %s"
            c = connection.cursor()
            c.execute(sql, (id_user,))
            connection.commit()
            info = (TIMESTAMP + " INFO: Удален user ID{} в таблице Users".format(id_user))
            print(info)
            return info
        except Error as e:
            print(e)
            return e

    def printer_users(self):
        try:
            sql = "SELECT * from users;"
            c = connection.cursor()
            c.execute(sql,)
            rows = c.fetchall()
            print("INFO: Выведены все пользователи из таблицы Users")
            return rows
        except Error as e:
            print(e)
            return e

Dealership_object = Dealership('localhost', 'dealership', 'root', 'password')
print(help(__name__))
