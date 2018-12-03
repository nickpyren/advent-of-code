filename = "../input"
value = 0
occurences = dict()
occurences[0] = 1
while not (2 in occurences.values()):
    with open(filename,'r') as file:
        for line in file:
            operator = line[0]
            operand = int(line[1::])

            if operator == '+':
                value += operand

            elif operator == '-':
                value -= operand

            if value in occurences:
                occurences[value] += 1
                if occurences[value] == 2:
                    break
            
            else:
                occurences[value] = 1

print(value)