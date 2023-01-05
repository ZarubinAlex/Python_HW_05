# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# qqqqqeeettttttttttt

import libr

print('')
print('\t1. Сжатие данных\n\
\t2. Восстановление данных')

while True:
    n = input('Выберите действие: ')
    if n.isdigit(): 
        n = int(n)
        if 1<= n <= 2: break

txt = input('Введите строку: ')
if n == 1:    
    print(libr.encode(txt))
else:
    print(libr.code(txt))
