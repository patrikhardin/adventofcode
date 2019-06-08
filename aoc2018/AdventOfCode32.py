# CUT THE FABRIC
# fabric is 1000" x 1000"

# One CLAIM per row in data
# Claim consists of:
#   (X,Y)-coordinates of top left corner
#   (X,Y)-coordinates of bottom right corner relative to top left corner. (Size)

# PROBLEM. many claims overlap. QUESTION. How many squares are occupied by two or more CLAIMS?

# Create the fabric matrix
fabric = []
for i in range(1000):
    fabric.append([0] * 1000)

with open('input3.txt', 'r') as file:
    claims = file.readlines()
    for claim in claims:
        # determine coordinates to be covered
        topLeftX = int(claim.split()[2].split(",")[0])
        topLeftY = int(claim.split()[2].split(",")[1].strip(":"))
        bottomRightX = int(claim.split()[2].split(",")[0]) + int(claim.split()[3].split("x")[0])
        bottomRightY = int(claim.split()[3].split("x")[1]) + int(claim.split()[2].split(",")[1].strip(":"))

        # Now go through this square in the fabric and add 1 to the elements
        for i in range(topLeftX, bottomRightX):
            for j in range(topLeftY, bottomRightY):
                fabric[i][j] += 1

    # Now look through the fabrics one by one and see which is still only coordinates
    for claim in claims:
        # determine coordinates to be covered
        topLeftX = int(claim.split()[2].split(",")[0])
        topLeftY = int(claim.split()[2].split(",")[1].strip(":"))
        bottomRightX = int(claim.split()[2].split(",")[0]) + int(claim.split()[3].split("x")[0])
        bottomRightY = int(claim.split()[3].split("x")[1]) + int(claim.split()[2].split(",")[1].strip(":"))

        fabricSum = 0
        for i in range(topLeftX, bottomRightX):
            for j in range(topLeftY, bottomRightY):
                fabricSum += fabric[i][j]
        if fabricSum == (topLeftX - bottomRightX) * (topLeftY - bottomRightY):
            print(claim)
        else:
            fabricSum = 0
