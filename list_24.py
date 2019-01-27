import random

string = input("Enter a word: ")
print("Jumble word:")
list = []
for i in string:
    list.append(i)
while list != []:
    lens = len(list)
    pops = random.randint(0, lens)
    print(list.pop(pops - 1).upper())