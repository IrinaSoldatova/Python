# Задача №17.
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

#1 вариант

list_numbers = [1, 1, 2, 0, -1, 3, 4, 4]
new_list = set(list_numbers)
print(list_numbers)
print(f'В заданном списке {len(new_list)} различных чисел')

#2 вариант решения (пользователь вводит значения самостоятельно)

list_numbers = []
n = int(input('Введите количество элементов в списке: '))
for i in range(n):
    i = int(input('Введите элемент списка: '))
    list_numbers.append(i)
print(list_numbers)
new_list = set(list_numbers)
print(f'В заданном списке {len(new_list)} различных чисел')

#3 вариант

list_numbers = [1, 1, 2, 0, -1, 3, 4, 4]
new_list = []

for i in list_numbers:
    if i not in new_list:
        new_list.append(i)


print(f'В заданном списке {len(new_list)} различных чисел')

#4 вариант

nums = [1, 2, 2, 3, 4, 5, 5, 5]

count = 0
for i in range(len(nums)):
    if nums[i - 1] != nums[i]:
        count += 1

print(count)