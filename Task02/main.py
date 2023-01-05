# Создайте программу для игры в ""Крестики-нолики"".

import libr
import random

array = [   ['*','*','*'],
            ['*','*','*'],
            ['*','*','*']]


libr.printArr(array)
print('Игра против компьютера, Вы играете крестиком. Право первого хода - случайным образом')
print('------------------------------------------------------------------------------------')

randG = random.randint(0, 1)
gamer = 'X' if randG == 1 else 'O'
key = 1

while libr.check(array) == None:

    if key > 9: break
    if gamer == 'O':
        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if array[y][x] == '*': break
        print(f'Ход компьютера: ')
        array[y][x] = 'O'
    else:
        while True:
            n = libr.inputCoord()
            x = n[1]
            y = n[0]
            if array[y][x] == '*': 
                break
            else: print('Клетка занята!')
        array[y][x] = 'X'

    libr.printArr(array)
    gamer = 'O' if gamer == 'X' else 'X'
    key += 1

if libr.check(array) == None:
    print('!!!!!!   Ничья   !!!!!!!')
else:
    print(f'!!!!!!  {libr.check(array)}   !!!!!!!')