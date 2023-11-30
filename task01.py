"""
Задача №1. Общее обсуждение
За день машина проезжает n километров. Сколько
дней нужно, чтобы проехать маршрут длиной m
километров? При решении этой задачи нельзя
пользоваться условной инструкцией if и циклами.
Input:
n = 700
m = 750
Output:
2
"""
import math
per_day = int(input('Введите сколько машина проезжает за день: '))
total = int(input('Введите сколько машина проезжает всего: '))

days = (total + per_day - 1) // per_day
print(days)
# или
print(math.ceil((total + per_day) // per_day))
# или
days = total//per_day + bool(total % per_day != 0)
print(days)
