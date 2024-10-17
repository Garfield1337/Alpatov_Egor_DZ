from func2 import pirnt_number
while True:
    number = input('Введите число от 1 до 99. Или введите "N", чтобы завершить программы\n').lower()
    if number == 'n':
        quit(1)
    else:
        print(f'\n{pirnt_number(number)}', end='\n\n')
