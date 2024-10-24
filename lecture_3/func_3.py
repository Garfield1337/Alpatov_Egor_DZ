def check_temp(temp):
    while True:
        try:
            float(temp[:-1])
            if temp[-1] not in ('c', 'f'):
                temp = input('Введите значение в градусах (C) или фаренгейтах (F)!\n').lower()
            else:
                return temp
        except:
            temp = input('Введите значение в градусах (C) или фаренгейтах (F)!\n').lower()


def temp_switch(temp):
    temp = check_temp(temp)
    if temp[-1] == 'f':
        f_formula = (float(temp[:-1])-32)/1.8
        return str(round(f_formula, 2)).rstrip('0').rstrip('.') + 'C°'
    elif temp [-1] == 'c':
        c_formula = float(temp[:-1])*9/5+32
        return str(round(c_formula, 2)).rstrip('0').rstrip('.') + 'F°'
