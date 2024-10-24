from func import example, calculate_answer, transition_check
from time import sleep as sl

def complex_menu():
    list_otvetov = []
    print('\nДавайте рассчитаем значение длины стороны треугольника по теореме косинусов!\n')
    while True:
        option = input('Введите "Y", чтобы продолжить выполнение программы.\n'
                       'Введите "N", чтобы завершить выполнение программы.\n'
                       'Введите "E", чтобы посмотреть пример выполнения программы.\n'
                       'Введите "P", чтобы посмотреть прошлые ответы.\n').lower()
        option = transition_check(option)
        if option == 'y':
            side_three = calculate_answer()
            list_otvetov.append(side_three)
            otvet_number = len(list_otvetov)
            str_otvetov = '\n'.join(list_otvetov)


        if option == 'n':
            print('\nЗавершение работы программы...\n', flush=True)
            sl(3)
            print('  /\_/\\\n / @ @ \\\n( ~~0~~ )', flush=True)
            sl(1)
            quit()

        if option == 'e':
            example()

        if option == 'p':
            if not list_otvetov:
                print('\nПока ответов не было.\n')
            else:
                print(f'\nКоличество ответов: {otvet_number}\nПрошлые ответы: \n{str_otvetov}\n')


complex_menu()