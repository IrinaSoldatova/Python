'''
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, где сумма
первых трех цифр равна сумме последних трех. Т.е. билет с номером
385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
программу, которая проверяет счастливость билета.

385916 -> yes
123456 -> no
'''

number_ticket = int(input('Введите номер билета: '))
first_number = number_ticket // 100000
second_number = number_ticket // 10000 % 10
third_number = number_ticket // 1000 % 10
fourth_number = number_ticket // 100 % 10
fifth_number = number_ticket // 10 % 10
sixth_number = number_ticket % 10
first_three_numbers = first_number + second_number + third_number
last_three_numbers = fourth_number + fifth_number + sixth_number
if first_three_numbers == last_three_numbers:
    result = 'yes'
elif len(str(number_ticket)) != 6:
    result = 'Надо ввести шестизначное число'
else:
    result = 'no'

print(result)