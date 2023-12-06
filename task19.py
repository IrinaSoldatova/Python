# Задача №19.
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

#1 вариант

list_numbers = [1, 2, 3, 4, 5]
k = int(input('k = '))

for i in range(k):
    tmp = list_numbers[0]
    for i in range(len(list_numbers)-1):
        list_numbers[i] = list_numbers[i+1]
    list_numbers[-1] = tmp
print(list_numbers)

#2 вариант

lst = [1, 2, 3, 4, 5]
lst2 = []
k = 3

for i in lst:
    lst2.append(lst[i-k])

print(lst2)

#3 вариант

lst = [1, 2, 3, 4, 5]

lst_shifted = []
shift = 3
for i in range(len(lst)):
    lst_shifted.append(lst[(i + shift) % len(lst)])
print(lst_shifted)

#4 вариант

my_list = [1, 2, 3, 4, 5]
k = 3
shifted_list = my_list[k:] + my_list[:k]

print(shifted_list)