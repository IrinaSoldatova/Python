# Задача №21.
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит


list_dicts = [{"V":"S001"}, {"V":"S002"}, {"VI":"S001", 4:"key"}, {"VI":"S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]
new_list = set()

for i in list_dicts:
    for j in i.keys():
        new_list.add(i[j])

print(new_list)
print()

#2 вариант

data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
        {"VI": "S005"}, {"VII": "S005", 4: 'new_key'}, {" V ":"S009"}, {" VIII":"S007 "}]
keys = set()
values = set()
for dct in data:
    for key, value in dct.items():
        keys.add(key)
        values.add(value)
print(keys)
print(values)