def check_number(number):
    while number != int:
        try:
            number = int(number)
            if  0 >= number or number > 99:
                number = input("Введите значение в диапазоне от 1 до 99\n")
            else:
                return number
        except:
            number = input('Введите целочисленное значение!\n')


def str_num_1(number):
    number = check_number(number)
    complex_list = [['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять'],
                    ['одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать'],
                    ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']]
    if 1 <= number <= 10:
        return complex_list[0][number - 1].title()
    elif 11 <= number <= 19:
        second_part = int(str(number)[1])
        return complex_list[1][second_part - 1].title()
    elif 20 <= number <= 99:
        first_part = int(str(number)[0])
        second_part = int(str(number)[1])
        if second_part == 0:
            return complex_list[2][first_part - 2].title()
        else:
            return complex_list[2][first_part - 2].title() + ' ' + complex_list[0][second_part - 1]