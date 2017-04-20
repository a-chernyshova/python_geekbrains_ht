# -*- coding: utf-8 -*-
# класс Car_dealership, описывающий работу автосалона
import Cars.Cars
import Cars.Lorry


class CarDealership:
    Cars = {}  # array of cars
    Lorries = {}  # array of lorry cars
    N = 200  # max amount of cars
    car_amount = 1
    lorry_amount = 1

    def __init__(self, N):
        self.car_amount = 0
        self.lorry_amount = 0
        self.N = N
        for x in range(1, CarDealership.N):
            self.Cars[x] = Cars.Cars.Cars(0, "", "", 0, 0, 0)
        for x in range(1, CarDealership.N):
            self.Lorries[x] = Cars.Lorry.Lorry(0, "", "", 0, 0, 0, 0)

    # prints whole list of cars and lorries
    # @staticmethod
    def printer(self):
        print("Модельный ряд машин")
        for i in range(1, CarDealership.car_amount):
            print(CarDealership.Cars[i].car_model)
        print("Модельный ряд грузовиков")
        for i in range(1, CarDealership.lorry_amount):
            print(CarDealership.Lorries[i].car_model)

    #id, car_model, maker, year_production, engine, cost
    def add_car(self, new_car):
        if self.car_amount + self.lorry_amount < self.N:
            CarDealership.car_amount += 1
            if new_car.id > 0:
                if new_car.id not in CarDealership.Cars.values():
                    CarDealership.Cars[CarDealership.car_amount - 1].id = new_car.id
                else:
                    print("Не уникальный id")
                    return ValueError
            else:
                print('id не может быть отрицательным')
                return ValueError
            CarDealership.Cars[CarDealership.car_amount - 1].car_model = new_car.car_model
            CarDealership.Cars[CarDealership.car_amount - 1].maker = new_car.maker
            CarDealership.Cars[CarDealership.car_amount - 1].year_production = new_car.year_production
            CarDealership.Cars[CarDealership.car_amount - 1].engine = new_car.engine
            CarDealership.Cars[CarDealership.car_amount - 1].cost = new_car.cost
        else:
            print("Дилерский центр переполнен!")

    def add_lorry(self, new_lorry):
        if self.lorry_amount + self.car_amount < self.N:
            CarDealership.lorry_amount += 1
            CarDealership.Lorries[CarDealership.lorry_amount].id = new_lorry.id
            CarDealership.Lorries[CarDealership.lorry_amount].car_model = new_lorry.car_model
            CarDealership.Lorries[CarDealership.lorry_amount].maker = new_lorry.maker
            CarDealership.Lorries[CarDealership.lorry_amount].year_production = new_lorry.year_production
            CarDealership.Lorries[CarDealership.lorry_amount].engine = new_lorry.engine
            CarDealership.Lorries[CarDealership.lorry_amount].cost = new_lorry.cost
            CarDealership.Lorries[CarDealership.lorry_amount].weight_limit = new_lorry.weight_limit
        else:
            print("Дилерский центр переполнен!")

    def get_car(self, id):
        if id < 0 or id > CarDealership.car_amount:
            print("По запросу ничего не найдено")
        else:
            self.Cars[id].printer()

    def get_lorry(self, id):
        if id < 0 or id > CarDealership.lorry_amount:
            print("По запросу ничего не найдено")
        else:
            self.Lorries[id].printer()
