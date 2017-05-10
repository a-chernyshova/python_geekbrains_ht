# -*- coding: utf-8 -*-
import unittest
import hashlib
import datetime
import mysql.connector
import random
from Deal.Dealership import Dealership


class DealershipTest(unittest.TestCase):

    def setUp(self):
        global Dealership1
        Dealership1 = Dealership('localhost', 'dealership_test', 'root', 'password')

    def test_add_user(self):
        h = 'test_pass2'.encode()
        h = hashlib.md5(h)
        result = Dealership1.create_user('test_log2', h.hexdigest(), 2)
        self.assertEqual(result, "New user {} with role {} was added to DB".format('test_log2', 'reader'))

    def test_auth(self):
        result = Dealership1.authorization('test_log2', 'test_pass2')
        self.assertEqual(result, (2,))

    def test_del_user(self):
        result = Dealership1.del_user(12)
        self.assertEqual(result, str(datetime.datetime.today())[:19] + " INFO: Удален user ID{} в таблице Users".format(12))

    def test_add_car(self, ):
        args = ('lada', 'zhiguli', 2017, 2, 5000)
        result = Dealership1.add_car('lada3', 'zhiguli', 2017, 2, 5000)
        self.assertEqual(result, str(datetime.datetime.today())[:19] + " INFO: Модель {} добавлена в таблицу Cars".
                         format('lada3', 'zhiguli', 2017))

    def test_add_dscar(self):
        sql = "select id_car from cars where car_model='lada3' and maker='zhiguli';"
        connection = mysql.connector.connect(host='localhost',
                                             database='dealership_test',
                                             user='root',
                                             password='password')
        c = connection.cursor()
        c.execute(sql)
        rows = c.fetchall()
        id_car = rows[0][0]
        # Вычислить id машины из предыдущего теста для добавления
        result = Dealership1.add_car_to_dealership(id_car, 10)
        self.assertEqual(result, str(datetime.datetime.today())[:19] + " INFO: Модель {} добавлена в таблицу "
                                                                       "Dealership".format((id_car, 10)))

    # проверять в текущей последовательности, после запуска двух предыдущих тестов, результат поиска будет не пустым
    def test_search_model(self):
        result = Dealership1.search_car_model('lada3')
        self.assertTrue(result)

    def test_search_maker(self):
        result = Dealership1.search_car_maker('zhiguli')
        self.assertTrue(result)

    def test_change_amount(self):
        sql = "select max(id) from dealership"
        connection = mysql.connector.connect(host='localhost',
                                             database='dealership_test',
                                             user='root',
                                             password='password')
        c = connection.cursor()
        c.execute(sql)
        rows = c.fetchall()
        id_car = rows[0][0]
        n = random.randint(1, 10)
        result = Dealership1.update_amount(id_car, n)
        self.assertEqual(result, str(datetime.datetime.today())[:19] + " INFO: Обновлена запись {} в таблице "
                                                                       "Dealership".format(id_car))

    def test_change_cost(self):
        sql = "select max(id_car) from cars"
        connection = mysql.connector.connect(host='localhost',
                                             database='dealership_test',
                                             user='root',
                                             password='password')
        c = connection.cursor()
        c.execute(sql)
        rows = c.fetchall()
        id_car = rows[0][0]
        n = random.randint(5000, 100000)
        result = Dealership1.update_car(id_car, n)
        self.assertEqual(result, str(datetime.datetime.today())[:19] + " INFO: Обновлена запись {} в таблице "
                                                                       "Car".format(id_car))

    def test_del_dscar(self):
        sql = "select max(id) from dealership;"
        connection = mysql.connector.connect(host='localhost',
                                             database='dealership_test',
                                             user='root',
                                             password='password')
        c = connection.cursor()
        c.execute(sql)
        rows = c.fetchall()
        id_car = rows[0][0]
        result = Dealership1.delete_car_from_dealership(id_car)
        self.assertEqual(result, str(datetime.datetime.today())[:19] + " INFO: Удалена запись {} в таблице "
                                                                       "Dealership".format(id_car))

    @unittest.skip('Тест еще не готов')
    def test_del_car(self):
        pass

    def test_add_lorry(self):
        result = Dealership1.add_lorry('Lorry_test', 'lorry', 2016, 2, 2000, 50)
        self.assertEqual(result, str(datetime.datetime.today())[:19] + " INFO: Модель {}{} добавлена в таблицы Cars, "
                                                                       "Lorries".format('Lorry_test', 'lorry'))

    @unittest.skipIf(1 > 2, 'Переключатель теста')
    def test_del_lorry(self):
        sql = "select id_car from cars where car_model='Lorry_test'"
        connection = mysql.connector.connect(host='localhost',
                                             database='dealership_test',
                                             user='root',
                                             password='password')
        c = connection.cursor()
        c.execute(sql)
        rows = c.fetchall()
        id_car = rows[0][0]
        result = Dealership1.delete_lorry(id_car)
        self.assertEqual(result, str(datetime.datetime.today())[:19] + " INFO: Удалена запись ID{} в таблицах Lorries, "
                                                                       "Cars".format(id_car))

    # Возвращает не пустую выборку
    def test_print_model(self):
        result = Dealership1.printer_models()
        self.assertTrue(result)

    def test_print_maker(self):
        result = Dealership1.printer_makers()
        self.assertTrue(result)

    def test_print_cars(self):
        result = Dealership1.printer_car_dealership()
        self.assertTrue(result)

    def test_print_not_available(self):
        result = Dealership1.printer_not_available_car()
        self.assertTrue(result)

    def test_print_user(self):
        result = Dealership1.printer_users()
        self.assertTrue(result)

    def tearDown(self):
        Dealership1.break_connection()

if __name__ == '__main__':
    unittest.main()
