import random

def game(count):

    print(f'\nОсталось: {count} конфет')
    print('Сколько возьмешь (не более 28)?')

    randG = random.randint(0, 1)
    gamer = 'Игрок 1' if randG == 1 else 'Игрок 2'

    while count > 0:
        
        while True:
            n = int(input(f'{gamer}: '))
            if 1 <= n <= 28: break

        count -= n

        if count <= 0: break

        print(f'Осталось: {count} конфет\n')
        gamer = 'Игрок 2' if gamer == 'Игрок 1' else 'Игрок 1'

    return gamer

