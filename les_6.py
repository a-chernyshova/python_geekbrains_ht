# -*- coding: utf-8 -*-
from math import sqrt
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определть методы позволяющие вычислить: Площадь, высоту и периметр фигуры
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_square(self):
        square = sqrt((self.a[1] - self.a[0])**2 + (self.b[1] - self.b[0])**2 + (self.c[1] - self.c[0])**2)
        return square

    def hight(self):
        pass

    def calc_perimeter(self):
        perimeter = sqrt((self.a[0]-self.b[0])**2+(self.a[1]-self.b[1])**2)
        perimeter += sqrt((self.b[0]-self.c[0])**2+(self.b[1]-self.c[1])**2)
        perimeter += sqrt((self.c[0]-self.a[0])**2+(self.c[1]-self.a[1])**2)
        return perimeter

t1 = Triangle([1,1],[1,2],[3,5])
print('ABC:', t1.a, t1.b, t1.c, 'perimeter: ', t1.calc_perimeter(), 'square: ', t1.calc_square())

# Задача-2: Написать Класс Равнобочная трапеция, заданной координатами 4-х точек.
#  Предусмотреть в классе методы: проверка, является ли фигура равнобочной трапецией;
#  вычисления: длины сторон, периметр, площадь.
class Isosceles_trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def check_isosceles(self):
        ac = sqrt((self.a[0] - self.c[0])**2 + (self.a[1] - self.c[1])**2)
        bd = sqrt((self.b[0] - self.d[0])**2 + (self.b[1] - self.d[1])**2)
        return ac==bd

    def calc_length_arm(self):
        ab = sqrt((self.a[0]-self.b[0])**2+(self.a[1]-self.b[1])**2)
        bc = sqrt((self.b[0]-self.c[0])**2+(self.b[1]-self.c[1])**2)
        cd = sqrt((self.c[0]-self.d[0])**2+(self.c[1]-self.d[1])**2)
        da = sqrt((self.d[0]-self.a[0])**2+(self.d[1]-self.a[1])**2)
        return ab, bc, cd, da

    def calc_perimeter(self):
        arms = self.calc_length_arm()
        perimeter = sum(list(arms))
        #perimeter += [arm for arm in arms] - почему не работает через генератор?
        # perimeter += [arm for arm in arms]
        # TypeError: unsupported operand type(s) for +=: 'int' and 'list'
        return perimeter

    def calc_square(self):
        arms = self.calc_length_arm()
        if arms[0] == arms[2]:
            square = (arms[1] + arms[3])/2*sqrt(arms[0]**2 - ((arms[1] - arms[3])**2)/4)
        elif arms[1] == arms[3]:
            square = (arms[0] + arms[2])/2*sqrt(arms[1]**2 - ((arms[0] - arms[2])**2)/4)
        else:
            print('Задана не равнобедренная трапеция')
        return square

tr1 = Isosceles_trapeze([0,0],[1,4],[3,4],[4,0])
print('Is it Isosceles trapeze? ', tr1.check_isosceles(),'\nThere are lengths arms: ', tr1.calc_length_arm())
print('There is a perimeter: ', tr1.calc_perimeter(), ', Square:', tr1.calc_square())
