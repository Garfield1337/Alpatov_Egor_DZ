from func2 import str_num_1

while True:
    number = input('Введите число от 1 до 99 или введите "N", '
                   'чтобы завершить выполнение программы.\n').lower()
    if number == 'n':
        quit()
    else:
        print(f'\n{str_num_1(number)}', end='\n\n')