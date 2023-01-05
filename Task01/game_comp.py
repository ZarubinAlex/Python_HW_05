import random

def game(count):

    print(f'\nОсталось: {count} конфет')
    print('Сколько возьмешь (не более 28)?')

    randG = random.randint(0, 1)
    gamer = 'Игрок 1' if randG == 1 else 'Комп'

    while count > 0:
        
        if gamer == 'Комп':
            n = random.randint(1, 29)
            if n > count: n = count
            print(f'Комп: {n}')
        else:
            while True:
                n = int(input(f'{gamer}: '))
                if 1 <= n <= 28: break

        count -= n

        if count <= 0: break

        print(f'Осталось: {count} конфет\n')
        gamer = 'Комп' if gamer == 'Игрок 1' else 'Игрок 1'

    return gamer

