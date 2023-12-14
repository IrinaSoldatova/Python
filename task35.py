# Задача №35.
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes
def is_prime(n):

    if n < 2:
        return "no"

    for i in range(2, n):
        if n % i == 0:
            return 'no'
    return 'yes'

n = 1000003
print(is_prime(n))



def is_prime(number: int) -> bool:
    if number <= 3:
        return True
    if not number % 2:
        return False
    for i in range(3, int(number**0.5), 2):
        if not number % i:
            return False
    return True


print(is_prime(1000003))