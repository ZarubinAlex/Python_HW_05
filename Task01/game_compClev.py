import random


def randN(count):
    if 84 < count <= 112: 
        n = count - 85
    elif 56 < count <= 84: 
        n = count - 57
    elif 28 < count <= 56: 
        n = count - 29
    elif count <=28: 
        n = count
    else:
        n = random.randint(1, 29)

    if n == 0: n = 1
    return n


def game(count):

    print(f'\nОсталось: {count} конфет')
    print('Сколько возьмешь (не более 28)?')

    randG = random.randint(0, 1)
    gamer = 'Игрок 1' if randG == 1 else 'Комп'

    while count > 0:
        
        if gamer == 'Комп':
            n = randN(count)
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

