#count amount of boxes that have the same letter appearing twice
#count amount of boxes that have the same letter appearing thrice
#multiply these two counted numbers


lineFound = False
lineFinal = []

with open('input2.txt','r') as file:
    lines = file.readlines()
    for line in lines:
        for line2 in lines:
            nErrs = 0
            for i in range(len(line)-1):
                if line[i] != line2[i]:
                    nErrs += 1

            if nErrs == 1:
                lineFound = True

                for j in range(len(line)):
                    if line[j] == line2[j]:
                        lineFinal.append(line[j])

                print(''.join(lineFinal))
                break

            if lineFound:
                break
