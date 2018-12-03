filename = "../input"
value = 0

with open(filename,'r') as file:
    for line in file:
        operator = line[0]
        operand = int(line[1::])

        if operator == '+':
            value += operand

        elif operator == '-':
            value -= operand

print(value)