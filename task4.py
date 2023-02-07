friends = []
N = int(input('Enter N: '))
for i in range(N):
    name = input('Enter name of your friend: ')
    age = int(input('Enter age of your friend: '))
    friends.append({'name': name, 'age' : age})
sum = 0
maxlen = len(friends[0].get('name'))
for i in range(N):
    sum += friends[i].get('age')
    if len(friends[i].get('name')) > maxlen:
        maxlen = friends[i].get('name')
avg = sum / N
print(f'Avg is {round(avg, 2)}, max length-name is {maxlen}')
