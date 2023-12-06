# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
#
# 1 2 3 4 5
# 3
# -> 1

#1 вариант

list_1 = [1, 2, 3, 4, 5, 3, 3, 3]
k = 3
count_ = list_1.count(k)
print(f'Элемент {k} повторяется {count_} раза')

#2 вариант
import random
lenlst = int(input("Введите длину списка: "))
k = 3
lst = []
cnt = 0
for i in range(lenlst):
    lst.append(random.randint(1, 10))
    if lst[i] == k:
        cnt += 1
print(lst)
print(cnt)
count_ = lst.count(k)
print(f'Элемент {k} повторяется {count_} раза')

#3 вариант

lenlst = int(input("Введите длину списка: "))
k = 3
lst = []
cnt = 0
for i in range(lenlst):
    lst.append(random.randint(1, 10))
    if lst[i] == k:
        cnt += 1
print(lst)
print(f'Элемент {k} повторяется {cnt} раза')
