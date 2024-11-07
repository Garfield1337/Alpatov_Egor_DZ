def check_number(number):
    while True:
        try:
            number = int(number)
            if number < 2:
                number = input('Значение не может быть меньше 2!\n')
            else:
                return number
        except:
            number = input('Введите целочисленное значение!\n')


def prime_num(number):
    prime_list = []
    for i in range(2, number + 1):
        prime = True
        for i2 in range(2, int(i**0.5) +1):
            if i % i2 == 0:
                prime = False
                break
        if prime == True:
            prime_list.append(str(i))
    return prime_list

