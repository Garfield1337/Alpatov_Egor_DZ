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


def pirnt_number(number):
    number = check_number(number)
    one_to_nine = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
    ten_to_nineteen = ['одиннадцать', 'двеннадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    twenty_to_ninety = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    if 1 <= number <= 10:
        return str(one_to_nine[number - 1]).title()
    elif 11 <= number <= 19:
        second_part = int(str(number)[1])
        return str(ten_to_nineteen[second_part - 1]).title()
    elif 20 <= number <= 99:
        first_part = int(str(number)[0])
        second_part = int(str(number)[1])
        if second_part == 0:
            return str(f'{twenty_to_ninety[first_part - 2]}').title()
        else:
            return str(f'{twenty_to_ninety[first_part - 2].title()} {one_to_nine[second_part - 1]}')