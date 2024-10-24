from func_3 import temp_switch


while True:
    temp_input = input('Введите значение температуры в градусах (C) или фаренгейтах (F).\n').lower()
    print(temp_switch(temp_input))