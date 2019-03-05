# CUT THE FABRIC
# fabric is 1000" x 1000"

# One CLAIM per row in data
# Claim consists of:
#   (X,Y)-coordinates of top left corner
#   (X,Y)-coordinates of bottom right corner relative to top left corner. (Size)

#PROBLEM. many claims overlap. QUESTION. How many squares are occupied by two or more CLAIMS?

#Create the fabric matrix
fabric = []
for i in range(1000):
    fabric.append([0]*1000)

with open('input3.txt','r') as file:
    claims = file.readlines()
    for claim in claims:
        #determine coordinates to be covered
        topLeftX = int(claim.split()[2].split(",")[0])
        topLeftY = int(claim.split()[2].split(",")[1].strip(":"))
        bottomRightX = topLeftX + int(claim.split()[3].split("x")[0])
        bottomRightY = topLeftY + int(claim.split()[3].split("x")[1])

        # Now go through this square in the fabric and add 1 to the elements
        for i in range(topLeftX,bottomRightX):
            for j in range(topLeftY,bottomRightY):
                fabric[i][j] += 1
        # Now we have filled the fabric.
        # Count the 0 elements and subtract from the amount of squares

    twoOrMore = 0
    for i in range(1000):
        for j in range(1000):
            if fabric[i][j] >= 2:
                twoOrMore += 1

    print(twoOrMore)
