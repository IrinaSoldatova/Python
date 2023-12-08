# import random
#
# print(random.randint(-50, 50))

s = input()
m = s[::-1]
print(m)
if s == m:
    print('YES')
else:
    print('NO')