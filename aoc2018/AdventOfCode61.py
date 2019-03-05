#Function that returns all manhattan points of degree n
def manhattanPoints(x,y,d):

    points = []

    #The manhattan points will lie on a rhoumbus which can be fully included in a square with sides of size 2*n and (x,y) in center
    topLeftX = x - d
    topLeftY = y - d

    for j in range(2*d+1):
        for i in range(2*d+1):
            if abs((topLeftX + i) - x) + abs((topLeftY + j) - y) == d:
                point = [topLeftX + i,topLeftY + j]
                if not point in points:
                    points.append(point)

    return points

# Function that looks in point (x,y) in the 'space'-matrix and returns which non-None value is closest. If two are equally close, then a dot is returned
def closestCoordinate(x,y,space):
    d = 0 #Reset the distance to 0 after every search
    found = False
    pointValue = ''
    while not found:
        nPoints = 0
        for point in manhattanPoints(x,y,d):
            if space[point[0]][point[1]] != None:
                pointValue = space[point[0]][point[1]]
                nPoints += 1
        if nPoints == 0:
            None
        if nPoints == 1:
            found = True
            return pointValue
        if nPoints > 1:
            pointValue = '.'
            found = True
            return pointValue
        d += 1


#MAIN. Assumption: x outer loop. y is inner loop

#Start with creating the space and assigning the coordinates
import string

with open('input6.txt','r') as file:
    lines = file.readlines()
xx = []
yy = []
coordinates = []
for line in lines:
    xx.append(int(line.split()[0].strip(',')))
    yy.append(int(line.split()[1].strip(' ')))

#Create the space
space = []
for i in range(max(xx)+1):
    space.append([None]*(max(yy)+1))

#Fill space with coordinates
nCoordinate = 0
for i,j in zip(xx,yy):
    space[i][j] = string.ascii_letters[nCoordinate]
    nCoordinate += 1

# Go through each point in the matrix and check if there exists any non-None value in each Manhattan distance "cicle" with increasing distance.
# If two then tie, add a dot. If one, then add the corresponding letter
# Disqualify a letter if it borders to the edge. Count which letter has most appearances. That number is the largest area

# Run the function that returns the closest non-None pointValue
# For every point in the space
'''for i in range(len(space)):
    for j in range(len(space[0])):
        space[i][j] = closestCoordinate(i,j,space)'''


print(space[350][353]) #
print(closestCoordinate(0,0,space)) #SHOULD NOT BE CLOSE TO A. This is because negative list entries is allowed. FIX!!!
print(closestCoordinate(350,352,space)) #close to a
#WHY ARE THESE THE SAME?
