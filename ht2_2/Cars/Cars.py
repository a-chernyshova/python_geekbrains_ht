# -*- coding: utf-8 -*-
# класс Car, автомобиль описывается следующими параметрами: уникальный идентификатор,
# марка автомобиля, страна-производитель, год выпуска, объем двигателя, стоимость


class Cars:
    def __init__(self, id, car_model, maker, year_production, engine, cost):
        self.id = id
        self.car_model = car_model
        self.maker = maker
        self.year_production = year_production
        self.engine = engine
        self.cost = cost

    def get_id(self):
        return self.id

    def get_car_model(self):
        return self.car_model

    def get_maker(self):
        return self.maker

    def get_year_production(self):
        return self.year_production

    def get_engine(self):
        return self.engine

    def get_cost(self):
        return self.cost

    def set_id(self, new_id):
        self.id = new_id

    def set_car_model(self, new_model):
        self.car_model = new_model

    def set_maker(self, new_maker):
        self.maker = new_maker

    def set_year_production(self, new_year):
        self.year_production = new_year

    def set_engine(self, new_engine):
        self.engine = new_engine

    def set_cost(self, new_cost):
        self.cost = new_cost

    def printer(self):
        print("Информация о модели:\n", self.id, self.car_model, ", производитель:",
              self.maker, ", год выпуска:", self.year_production, ", объем двигателя:",
              self.engine, ", цена: $", self.cost)
