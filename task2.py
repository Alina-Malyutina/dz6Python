dictFruit = {}
amount = int(input("amount of fruit: "))
for i in range(amount):
    name = input("Name fruit: ")
    amountFruit = int(input("Amount: "))
    dictFruit[name] = amountFruit
    
for name, amountFruit in dictFruit.items():
        print(name, amountFruit)

print(dictFruit)