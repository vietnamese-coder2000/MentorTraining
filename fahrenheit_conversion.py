celsius = float(input('Enter the temperature in Celsius'))
print(str(celsius) + ' (C) = ', end='')
def convert(celsius):
    return celsius * 1.8 + 32
print(str(convert(celsius)) + ' (F)')
