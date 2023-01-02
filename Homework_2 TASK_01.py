# Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

print('Чтобы получить сумму цифр в числе введите в число N:')
str_N = input('N = ')

import re
str_N1 = re.sub(r'[.,]', '', str_N)
int_N = int(str_N1)

sum = 0

while int_N > 0:
    sum = sum + int_N % 10
    int_N = int_N // 10

print(f'Сумма чисел введенного Вами числа {str_N} -> {sum}')