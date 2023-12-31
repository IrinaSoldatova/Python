# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def power(a, b):
    if b < 0:
        return (1/a) * power(a, b+1)
    if b > 0:
        return a * power(a, b-1)
    else:
        return 1

a = int(input('Введите основание степени (а): '))
b = int(input('Введите показатель степени (b): '))
print(f'Число {a} в степени {b} равно: {power(a, b)}')