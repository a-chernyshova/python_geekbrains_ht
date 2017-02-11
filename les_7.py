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

def generate_places():
    place = []
    for i in range(3):
        column = list(range(1, 10))
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
    numbs = list(range(1, 91))
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
    print(' ', fields[0][0], '  ', fields[0][1], ' ', fields[0][2], '  ', fields[0][3], ' ', fields[0][4], ' ',
          fields[0][5], ' ', fields[0][6], ' ', fields[0][7], ' ', fields[0][8])
    print('---------------------------------------')
    print(' ', fields[1][0],' ',fields[1][1],' ',fields[1][2],' ',fields[1][3],' ',fields[1][4],' ',
          fields[1][5],' ',fields[1][6],' ',fields[1][7],' ',fields[1][8])
    print('---------------------------------------')
    print(' ', fields[2][0],' ',fields[2][1],' ',fields[2][2],' ',fields[2][3],' ',fields[2][4],' ',
          fields[2][5],' ',fields[2][6],' ',fields[2][7],' ',fields[2][8])
    print('________________________________________')
    return fields

numbs = []
for i in range(90):
    numbs.append(i)

def get_number():
    num = random.choice(numbs)
    numbs.remove(num)
    print(num)
    return num

def remove_num_from_card(num, card):
    for i in [0, 1, 2]:
        if num in card[i]:
            card[i][card[i].index(num)] = ' '

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
            print('__________________Card__________________')
            print(' ', your_card[0][0],'  ',your_card[0][1],' ',your_card[0][2],'  ',your_card[0][3],' ',your_card[0][4],' ',
					your_card[0][5],' ',your_card[0][6],' ',your_card[0][7],' ',your_card[0][8])
            print('---------------------------------------')
            print(' ', your_card[1][0],' ',your_card[1][1],' ',your_card[1][2],' ',your_card[1][3],' ',your_card[1][4],' ',
					your_card[1][5],' ',your_card[1][6],' ',your_card[1][7],' ',your_card[1][8])
            print('---------------------------------------')
            print(' ', your_card[2][0],' ',your_card[2][1],' ',your_card[2][2],' ',your_card[2][3],' ',your_card[2][4],' ',
					your_card[2][5],' ',your_card[2][6],' ',your_card[2][7],' ',your_card[2][8])
            print('________________________________________')
            amount_of_erasing_yours += 1
            if amount_of_erasing_yours == 15:
                print('Congratulations, dude! You are win!Your remove all numbers from your card!')
                quit()
        else:
            print("You are lost, because this number", step, "isn't in your card")
            quit()