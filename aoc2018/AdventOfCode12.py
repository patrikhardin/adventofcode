
sum = 0
freqs = set()
with open('input1.txt','r') as file:
    ok = True
    lines = list(file.readlines())
    while ok:
        for l in lines:
            sum += int(l)
            if sum in freqs:
                print(sum)
                ok = False
                break
            freqs.add(sum)
