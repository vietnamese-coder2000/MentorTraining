import math
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
def solve(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "All Real Number"
            else:
                return "No Solution"
        else:
            if c == 0:
                return "x = 0"
            else:
                return "x = " + str(-c / b)
    else:
        delta = b * b - 4 * a * c
        if delta < 0:
            return "No Solution"
        elif delta == 0:
            return ("x1 = x2 = " + str((-b / (2 * a))))
        else:
            return ("x1 = " + str((-b + math.sqrt(delta))/(2 * a)) + '\n' + "x2 = " + str((-b - math.sqrt(delta))/(2 * a)))

print(solve(a, b, c))