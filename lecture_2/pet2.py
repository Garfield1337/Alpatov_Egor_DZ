from time import sleep as sl
from func2 import pirnt_number

while True:
    number = input('Введите число от 1 до 99 или введите "N", '
                   'чтобы завершить выполнение программы.\n').lower()
    if number == 'n':
        print('\nЗавершение работы программы...\n', flush=True)
        sl(3)
        print('  /\_/\\\n / @ @ \\\n( ~~0~~ )', flush=True)
        sl(1)
        quit()
    else:
        print(f'\n{pirnt_number(number)}', end='\n\n')