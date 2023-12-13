# Задача №27.
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов или символами конца строки.Определите,
# сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore; The shells
# that she sells are sea shells I'm sure. So if she sells sea
# shells on the sea shore, I'm sure that the shells are sea
# shore shells.
# Output: 13

line = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
line = line.lower().replace('.', ' ').split()
words = set()
for i in line:
    words.add(i)
print(len(words))