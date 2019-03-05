
sum = 0
with open('input1.txt','r') as file:
    for line in file:
        sum += int(line)
    print(sum)
