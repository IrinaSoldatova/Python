"""
Задача №5. Решение в группах
Вагоны в электричке пронумерованы натуральными
числами, начиная с 1 (при этом иногда вагоны
нумеруются от «головы» поезда, а иногда – с
«хвоста»; это зависит от того, в какую сторону едет
электричка). В каждом вагоне написан его номер.
Витя сел в i-й вагон от головы поезда и обнаружил,
что его вагон имеет номер j. Он хочет определить,
сколько всего вагонов в электричке. Напишите
программу, которая будет это делать или сообщать,
что без дополнительной информации это сделать
невозможно.
Input: 3 4(ввод на разных строках)
Output: 6
"""
vagon_number_i = int(3)
vagon_number_j = int(4)
if vagon_number_i != vagon_number_j:
    vagon_total = vagon_number_i + vagon_number_j - 1
    result = vagon_total

else:
    result = 'Не хватает данных'
print(result)
