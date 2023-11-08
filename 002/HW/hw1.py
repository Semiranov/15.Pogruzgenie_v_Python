HEX = 16

num = 0
result = ''
num2 = num

while num2 > 0:
    new_num = num2 % HEX
    if new_num == 10:
        result = 'A' + result
    elif new_num == 11:
        result = 'B' + result
    elif new_num == 12:
        result = 'C' + result
    elif new_num == 13:
        result = 'D' + result
    elif new_num == 14:
        result = 'E' + result
    elif new_num == 15:
        result = 'F' + result
    else:
        result = str(new_num) + result
    num2 //= HEX
print(f'Шестнадцатеричное представление числа: {result}')
print(f'Проверка результата: {hex(num)}')
