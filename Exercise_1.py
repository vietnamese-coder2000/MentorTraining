name = ['ST', 'BD', 'BTL', 'CG', 'DD', 'HBT']
population = [150300, 247100, 333300, 266800, 420900, 318000]
def find_max_index(list):
    max_ind = 0
    max = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
            max_ind = i
    return max_ind


def find_min_index(list):
    min_ind = 0
    min = list[0]
    for i in range(len(list)):
        if list[i] < min:
            min = list[i]
            min_ind = i
    return min_ind

area = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
def pop_den():
    list = []
    for i in range(len(area)):
        list.append(population[i] / area[i])
    return list