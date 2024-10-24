#Как и написано в основном файле, все функции перенесены в отдельный файл для удобства.
#Для работы всех функций нам понадобятся следующие библиотеки:
import math
import random
from time import sleep as sl


#Первая функция. Преобразование и проверка ввода значений длин сторон.
def check_side(number):
    while number != float:
        try:
            number = float(number)
            if number < 0 or number == 0:
                number = input("Значение стороны треугольника не может "
                          "быть отрицательным или равняться 0!\n")
            else:
                return float(number)
        except:
            number = input('Введите числовое значение!\n')


def check_angle(number):
    while number != float:
        try:
            number = float(number)
            if number > 180 or number == 180:
                number = input('Значение градуса угла не может превышать 180 '
                          'или равняться 180!\n')
            elif number < 0 or number == 0:
                number = input('Значение градуса угла не может быть отрицательным '
                          'или равняться 0!\n')
#Если нам удалось преобразовать str во float, и значение соответсвует двум условиям, то мы возвращаем значение.
            else:
                return float(number)
        except:
            number = input('Введите числовое значение!\n')


def example():
    side_one = round(random.uniform(0.001, 100), 2)
    side_two = round(random.uniform(0.001, 100), 2)
    angle = round(random.uniform(0.001, 179.001), 2)
    print('\nВ первую очередь мы задаем значение длинны первой стороны.\n'
          'При этом важно учесть, что ее значение не может быть отрицательным или равным 0!\n'
          f'В нашем случае, выберем значение {side_one}', flush = True)
    sl(3)
    print('\nТеперь зададим значение для второй стороны.\n'
          'Ограничения те же.\n'
          f'Давайте выберем значение {side_two}', flush = True)
    sl(2)
    print('\nТеперь давайте введем значение угла между этими двумя сторонами.\n'
          'При этом важно учесть, что его значение не может быть отрицательным или равняться 0, \n'
          'а также не может равняться 180 или превышать это значение.\n'
          f'Давайте остановимся на варианте {angle}', flush = True)
    sl(4)
    print('\nПосле этого программа проводит вычисления по установленной формуле и выводит ответ.')
    angle = math.radians(angle)
    answer = round(math.sqrt(side_one ** 2 + side_two ** 2 - 2 * side_one * side_two * math.cos(angle)), 2)
    answer = str(answer).rstrip('0').rstrip('.')
    return print(f'Вот он: {answer}\n')


def transition_check(option):
    while option not in ['y', 'n', 'e', 'p']:
        option = input('Выберите из предложенного!\n'
                  'Введите "Y", чтобы продолжить выполнение программы.\n'
                  'Введите "N", чтобы завершить выполнение программы.\n'
                  'Введите "E", чтобы посмотреть пример выполнения программы.\n'
                  'Введите "P", чтобы посмотреть прошлые ответы.\n').lower()
    else:
        return option


def calculate_answer():
    side_one = input('\nВведите значение длинны первой стороны:\n')
    side_one = check_side(side_one)
    side_two = input('Введите значение длинны второй стороны:\n')
    side_two = check_side(side_two)
    angle = input('Введите значение градуса угла между ними:\n')
    angle = check_angle(angle)
    angle = math.radians(angle)
    side_three = round(math.sqrt(side_one ** 2 + side_two ** 2 - 2 * side_one * side_two * math.cos(angle)), 2)
    side_three = str(side_three).rstrip('0').rstrip('.')
    print(f'\nЗначение длинны третьей стороны: {side_three}\n')
    return side_three
