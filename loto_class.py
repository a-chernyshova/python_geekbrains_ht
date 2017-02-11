# -*- coding: utf-8 -*-
#!/usr/bin/python3
"""Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).Каждая карточка содержит 3 строки по 9 клеток.
В каждой строке по 5 случайных цифр,расположенных по возрастанию.
Все цифры в карточке уникальны.
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода: Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать модуль random: http://docs.python.org/3/library/random.html"""
import random

class Generator:
    def __init__(self, count, _max):
        self.count = count
        self.base_list = list(range(1, _max+1))

    def create_list(self):
        generated_list = []
        for i in range(self.count):
            generated_list.append(random.choice(self.base_list))
            self.base_list.remove(generated_list[i])
        return generated_list

class Card:
    def __init__(self):
        self.positions_list1 = Generator(5, 9).create_list()
        self.positions_list2 = Generator(5, 9).create_list()
        self.positions_list3 = Generator(5, 9).create_list()
        self.numbers_on_card = sorted(Generator(15, 90).create_list())


    def show_card(self, name):
        layout1 = [' ']*9
        layout2 = [' ']*9
        layout3 = [' ']*9
        print(('-')*15 + name + " card-----------------")
        for i in self.positions_list1:
            layout1[i-1] = self.numbers_on_card[self.positions_list1.index(i)]
        for i in self.positions_list2:
            layout2[i-1] = self.numbers_on_card[self.positions_list2.index(i)+5]
        for i in self.positions_list3:
            layout3[i-1] = self.numbers_on_card[self.positions_list3.index(i)+10]

        print(' ', layout1[0], '  ', layout1[1], ' ', layout1[2], '  ', layout1[3], ' ', layout1[4], ' ',
            layout1[5], ' ', layout1[6], ' ', layout1[7], ' ', layout1[8])
        print(' ', layout2[0], ' ', layout2[1], ' ', layout2[2], ' ', layout2[3], ' ', layout2[4], ' ',
          layout2[5], ' ', layout2[6], ' ', layout2[7], ' ', layout2[8])
        print(' ', layout3[0], ' ', layout3[1], ' ', layout3[2], ' ', layout3[3], ' ', layout3[4], ' ',
          layout3[5], ' ', layout3[6], ' ', layout3[7], ' ', layout3[8])
        print(('-')*42)


    def __contains__(self, item):
        return item in self.numbers_on_card

class Loto:
    def __init__(self):
        card1 = Card()
        card2 = Card()
        self.computer = Player(card1)
        self.human = Human(card2)
        self.generator = Generator(1, 90)
        self.computer.card.show_card('Computer')
        self.human.card.show_card('Your')

    def step(self):
        move = self.generator.create_list()[0]
        answer = self.human.ask(move)
        if self.computer.__contains__(move):
            self.computer.strike_number(move)
        if answer:
            if self.human.__contains__(move):
                self.human.strike_number(move)
                self.computer.card.show_card('Computer')
                self.human.card.show_card('Your')
            else:
                print('Looser!')
                quit()
        else:
            if self.human.__contains__(move):
                print('Looser!')
                quit()

    def game(self):
        for i in range(90):
            self.step()

class Player:
    def __init__(self, card):
        self.card = card
        self.guess = 0

    def __contains__(self, move):
        return self.card.__contains__(move)

    def strike_number(self, move):
        index = self.card.numbers_on_card.index(move)
        self.card.numbers_on_card[index] = '-'
        self.guess += 1
        if self.guess == 15:
            print('Computer wins!')
            quit()

class Human(Player):
    def __init__(self, card):
        self.card = card
        self.guess = 0

    def ask(self, move):
        answer = input('Is ' + str(move) + ' in your card ?(y/n)')
        return answer is 'y'

    def strike_number(self, move):
        index = self.card.numbers_on_card.index(move)
        self.card.numbers_on_card[index] = '-'
        print('Good job!')
        self.guess += 1
        if self.guess == 15:
            print('Congratulations! You are winner!')
            quit()

if __name__ == '__main__':
    start_loto = Loto()
    start_loto.game()