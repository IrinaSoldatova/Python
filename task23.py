# Задача №23.
# Дан список, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

#1 вариант

list_ = [0, -1, 5, 2, 3]
count = 0
for i in range(len(list_)):
    if list_[i] > list_[i-1]:
        count += 1
print(count)

#2 вариант

import random

lenlst = int(input("Введите длину списка: "))
count = 0
lst = []

for i in range(lenlst):
    lst.append(random.randint(1, 10))
    if lst[i] > lst[i-1]:
        count += 1

print(lst)
print(count)