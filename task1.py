from random import randint
list = []
for i in range(1,6):
    list.append(randint(1, 10))
print(list)

del list[0:5]
print(list)