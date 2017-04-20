# -*- coding: utf-8 -*-
#класс Lorry на базе класс Car, грузовик характеризуется: весовым ограничение перевозки
import Cars.Cars


class Lorry(Cars.Cars.Cars):
    def __init__(self, id, car_model, maker, year_production, engine, cost, weight_limit):
        super().__init__(id, car_model, maker, year_production, engine, cost)
        self.weight_limit = weight_limit

    def get_weight_limit(self):
        return self.weight_limit

    def set_weight_limit(self, new_limit):
        self.weight_limit = new_limit

    def printer(self):
        super().printer()
        print("Весовое ограничение перевозки (тонны):", self.weight_limit)
