'''
Задача 2:
Найдите сумму цифр трехзначного числа.
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
'''

n = int(input('Введите трехзначное число: '))
first = n//100
second = n // 10 % 10
last = n % 10
res = first + second + last
print(f'{res} ({first} + {second} + {last})')