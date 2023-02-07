friends = []
N = int(input('Enter N: '))
for i in range(N):
    name = input('Enter name of your friend: ')
    age = int(input('Enter age of your friend: '))
    friends.append({'name': name, 'age' : age})
minn = friends[0].get('age')
for i in range(N):
    if friends[i].get('age') < minn:
        minn = friends[i].get('age')
for i in range(N):
    if friends[i].get('age') == minn:
        print(friends[i].get('name'))
        

