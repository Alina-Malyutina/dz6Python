english_dict = {}
list = []
N = int(input('Enter amount of words that you want to add: '))
for i in range(N):
    word = input('Enter word on english: ')
    translate = input('Enter translates in english separated by a space: ').split()
    list.append({word : translate})
print (list)