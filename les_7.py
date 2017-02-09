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

# class Card:
#     def __init__(self):
#         self.row = 3
#         self.column = 9
#
#     def generate_card(self):
#         genereted_card = []
#         for i in self.row:
#             genereted_card.append([])
#             for x in self.column:
#                 genereted_card[i].append(random.randint(1, 90))
#         return genereted_card
#
#     def draw_card(card):
#         print("--"*22)
#         for i in range(3):
#             print("|", random.randint(1,10), "|", random.randint(11,20), "|", random.randint(21,30), "|", random.randint(31,40),
#                   "|", random.randint(41,50), "|", random.randint(51,60), "|", random.randint(61,70), "|", random.randint(71,80),
#                   "|", random.randint(81,90), "|")
#             print("--"*22)
#
#     def strike_number(self):
#         pass
#
#     def check_availability(self):
#         pass
#
# class User:
#     def get_card(self):
#         pass
#
#     def move(self):
#         pass
#
# class Computer(User):
#     def get_card(self):
#         pass
#
#     def move(self):
#         pass
#
# class Loto:
#     # user
#     # computer
#     def move(self):
#         pass
def generate_places():
    place = []
    for i in range(3):
        column = [1,2,3,4,5,6,7,8,9]
        for a in range(5):
            x = random.choice(column)
            place.append(x-1)
            column.remove(x)
    row0 = sorted(place[:5])
    row1 = sorted(place[5:10])
    row2 = sorted(place[10:])
    return row0, row1, row2

def generate_card():
    row1 = [' ']*9
    row2 = [' ']*9
    row3 = [' ']*9
    numbs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,
                 51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]
    place = generate_places()
    gen_numbs=[]
    for i in range(15):
        num = random.choice(numbs)
        gen_numbs.append(num)
        numbs.remove(num)
    gen_numbs = sorted(gen_numbs)
    for i in range(5):
        row1[place[0][i]] = gen_numbs[i]
        row2[place[1][i]] = gen_numbs[i+5]
        row3[place[2][i]] = gen_numbs[i+10]
    return row1, row2, row3

def get_card():
    fields = generate_card()
    print('__________________Card__________________')
    #print('------------------------------------------')
    print(' ', fields[0][0],'  ',fields[0][1],' ',fields[0][2],'  ',fields[0][3],' ',fields[0][4],' ',
          fields[0][5],' ',fields[0][6],' ',fields[0][7],' ',fields[0][8])
    print('---------------------------------------')
    print(' ', fields[1][0],' ',fields[1][1],' ',fields[1][2],' ',fields[1][3],' ',fields[1][4],' ',
          fields[1][5],' ',fields[1][6],' ',fields[1][7],' ',fields[1][8])
    print('---------------------------------------')
    print(' ', fields[2][0],' ',fields[2][1],' ',fields[2][2],' ',fields[2][3],' ',fields[2][4],' ',
          fields[2][5],' ',fields[2][6],' ',fields[2][7],' ',fields[2][8])
    print('________________________________________')
    return fields

def get_number():
    numbs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,
                 51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]
    # for i in range(90):
    #     num = random.choice(numbs)
    #     numbs.remove(num)
    #     print(num)
    num = random.choice(numbs)
    numbs.remove(num)
    print(num)
    return num

def remove_num_from_card(num, card):
    for i in [0, 1, 2]:
        if num in card[i]:
            card[i].remove(num)

def check_number_in_card(num, card):
    for i in [0, 1, 2]:
        if num in card[i]:
            return True

print('Start to play LOTO')
print('Your card')
your_card = get_card()
print("Computer's card")
computers_card = get_card()
for i in range(90):
    step = get_number()
    amount_of_erasing_yours = 0
    amount_of_erasing_comp = 0
    if check_number_in_card(step, computers_card):
        remove_num_from_card(step, computers_card)
        amount_of_erasing_yours += 1
        if amount_of_erasing_yours == 15:
            print('Congratulations, Computer finished before you!')
            quit()
    ask = input('Remove number from your card or continue?(y/n)')
    if ask == 'y' or ask == 'Y':
        if check_number_in_card(step, your_card):
            remove_num_from_card(step, your_card)
            amount_of_erasing_yours += 1
            if amount_of_erasing_yours == 15:
                print('Congratulations, dude! You are win!Your remove all numbers from your card!')
                quit()
        else:
            print("You are lost, because this number", step, "isn't in your card")
            quit()