import random
list = ["Queen", "Random", "Champion", "Unity", "Pretty"]
def print_random(string):
    list = []
    for i in string:
        list.append(i)
    while list != []:
        lens = len(list)
        pops = random.randint(0, lens)
        print(list.pop(pops - 1).upper(), end = "")
print_random(list[random.randint(0, len(list) - 1)])