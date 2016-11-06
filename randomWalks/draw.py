import random

def drawSegment( matrix, shapeLength):
    random.seed()
    height = len(matrix)
    width = len(matrix[0])
    i,j = random.randint(0, height-1),  random.randint(0, width-1)
    while shapeLength>0:
        x = random.randint(-1,1)
        y = random.randint(-1,1)
        if i+x<0 or i+x> height-1:
            x *= -1
        if j+y<0 or j+y> width-1:
            y *= -1
        i,j = i+x, j+y
        matrix[i][j] = '*'
        shapeLength -= 1

def drawLine( matrix, lineLength):
    i,j = 15,15
    segLength = 8
    segNumber = lineLength/segLength
    while segNumber>0:
        direction = random.randint(0,4)
        i,j = drawLineSegment(matrix, i, j, direction, segLength) 
        segNumber -= 1

#TODO fix index out of bounds.
def drawLineSegment( matrix, i, j, direction, segLength):
    #direction = random.randint(0,4)
    while segLength>0:
        x = random.randint(-1, 1)
        if direction == 0:
            i,j = i+1, j+x
        elif direction == 1:
            i,j = i-1, j+x
        elif direction == 2:
            i,j = i+x, j+1
        elif direction == 3:
            i,j = i+x, j-1
        matrix[i][j] = '*'
        segLength -= 1
    return i,j

def createMatrix(length, height):
    return [[' ' for i in range(length)] for k in range (height)]


def printMatrix(matrix):
    for i in matrix:
        print ''.join(i) 


matrix = createMatrix(30, 30)
drawLine(matrix, 50)
printMatrix(matrix)

