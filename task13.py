'''
Задача №13.
Уставшие от необычно теплой зимы, жители решили узнать,
действительно ли это самая длинная оттепель за всю историю
наблюдений за погодой. Они обратились к синоптикам, а те, в
свою очередь, занялись исследованиями статистики за
прошлые годы. Их интересует, сколько дней длилась самая
длинная оттепель. Оттепелью они называют период, в
который среднесуточная температура ежедневно превышала
0 градусов Цельсия. Напишите программу, помогающую
синоптикам в работе.
Пользователь вводит число N – общее количество
рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
располагается N целых чисел.
Каждое число – среднесуточная температура в
соответствующий день. Температуры – целые числа и лежат в
диапазоне от –50 до 50
Input: 6 -> -20 30 -40 50 10 -10
Output: 2
'''
'''
import random
number_days = int(input("Enter days number: "))
i = 0
count = 0
mx = 0

while i < number_days:
    day1 = random.randint(-10,50)
    print(day1, end=' ')
    if day1 > 0 :
        count += 1
    else:
        if mx < count:
            mx = count
        count = 0
    i += 1
if mx < count:
    mx = count
print()
print(f"Max warm days = {mx}")
'''
import random

user_num = int(input("Please input your amount of days: "))
sum_ = 0
max_ = 0

for _ in range(user_num):
    day_temp = random.randint(-50, 50)
    print(day_temp, end=' ')
    if day_temp > 0:
        sum_ += 1
        if max_ < sum_:
            max_ = sum_
    else:
        sum_ = 0
print()
print(f"Number >0 days: {max_}")














