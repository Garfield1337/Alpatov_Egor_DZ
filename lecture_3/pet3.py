from func_3 import temp_switch


while True:
    temp_in = input('Введите значение температуры в градусах (C) или фаренгейтах (F).\n').lower()
    print(temp_switch(temp_in))