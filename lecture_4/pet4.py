from func_4 import check_number, prime_num

while True:
    num = check_number(input('Введите целочисленное значение, начиная с 2.\n'))
    print('\n'.join(prime_num(num)))