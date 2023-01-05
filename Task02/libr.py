def check(array):
    if array[0][0] == array [1][0] == array[2][0] != '*':
        return f'выиграли {array[0][0]}'
    elif array[0][1] == array [1][1] == array[2][1] != '*':
        return f'выиграли {array[0][1]}'
    elif array[0][2] == array [1][2] == array[2][2] != '*':
        return f'выиграли {array[0][2]}'

    elif array[0][0] == array [0][1] == array[0][2] != '*':
        return f'выиграли {array[0][0]}'
    elif array[1][0] == array [1][1] == array[1][2] != '*':
        return f'выиграли {array[0][0]}'
    elif array[2][0] == array [2][1] == array[2][2] != '*':
        return f'выиграли {array[2][0]}'

    elif array[0][0] == array [1][1] == array[2][2] != '*':
        return f'выиграли {array[0][0]}'
    elif array[2][0] == array [1][1] == array[0][2] != '*':
        return f'выиграли {array[2][0]}'


def printArr(array):
    
    print('')
    print('\t\tA\tB\tC')
    print('\t--------------------------')
    
    for i in range(3):
        print(f'\t{i+1}:', end = '')
        for j in range(3):
            print(f'\t{array[i][j]}', end = '')
        print('\n')


def inputCoord():

    while True:
        n = input('Введите координаты через пробел (например, A 3): ').split()
        if len(n) > 1:
            if n[1].isdigit():
                y = int(n[1]) - 1
        if n[0].lower() == 'a':
            x = 0
        elif n[0].lower() == 'b': 
            x = 1
        elif n[0].lower() == 'c': 
            x = 2
        else: x = -1

        if 0 <= x <= 2 and 0 <= y <= 2: break

    return [y,x]

