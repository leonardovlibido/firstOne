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
    random.seed()
    i,j = len(matrix)-1,15
    segLength = 5
    segNumber = lineLength/segLength
    while segNumber>0:
        direction = random.randint(0,4)
        i,j = drawLineSegment(matrix, i, j, "up", segLength) 
        segNumber -= 1


#TODO copy-pasted from up, needs sorting out
def drawLineSegmentLeft( matrix, i, j, segLength):
    height = len(matrix)
    width = len(matrix[0])
    while segLength>0:
        x = random.randint(-1,1)
        y = random.randint(-1,1)
        if i == height:
            break
        if j+y<0 or j+y>width:
            y *= -1
        i += 1
        j += y
        if y == -1:
            matrix[i][j] = '/'
        elif y == 1:
            matrix[i][j] = '\\'
        else:
            matrix[i][j] = '|'
        segLength -= 1
    return i,j

#TODO copy-pasted from up, needs sorting out
def drawLineSegmentRight( matrix, i, j, segLength):
    height = len(matrix)
    width = len(matrix[0])
    while segLength>0:
        x = random.randint(-1,1)
        y = random.randint(-1,1)
        if i == height:
            break
        if j+y<0 or j+y>width:
            y *= -1
        i += 1
        j += y
        if y == -1:
            matrix[i][j] = '/'
        elif y == 1:
            matrix[i][j] = '\\'
        else:
            matrix[i][j] = '|'
        segLength -= 1
    return i,j

#TODO this is the best function, all the others should look like this one.
def drawLineSegmentUp( matrix, i, j, segLength):
    height = len(matrix)
    width = len(matrix[0])
    while segLength>0:
        x = random.randint(-1,1)
        y = random.randint(-1,1)
        if i == 0:
            break
        if j+y<0 or j+y>width:
            y *= -1
        if y == -1:
            matrix[i][j] = '\\\\'
        elif y == 1:
            matrix[i][j] = '//'
        else:
            matrix[i][j] = '||'
        segLength -= 1
        i -= 1
        j += y
    return i,j

#TODO changed i,j moving should be tested
def drawLineSegmentDown( matrix, i, j, segLength):
    height = len(matrix)
    width = len(matrix[0])
    while segLength>0:
        x = random.randint(-1,1)
        y = random.randint(-1,1)
        if i == height:
            break
        if j+y<0 or j+y>width:
            y *= -1
        if y == -1:
            matrix[i][j] = '/'
        elif y == 1:
            matrix[i][j] = '\\'
        else:
            matrix[i][j] = '|'
        segLength -= 1
        i += 1
        j += y
    return i,j

#TODO add right and left calls after they are implemented, enumerate direction
def drawLineSegment( matrix, i, j, direction, segLength):
    #direction = random.randint(0,4)
    if direction == "up":
        i,j = drawLineSegmentUp(matrix, i, j, segLength)
    elif direction == "down":
        i,j = drawLineSegmentDown(matrix, i, j, segLength)

    elif direction == "right":
        x=1
        #drawLineSegmentRight()
    elif direction == "left":
        x=1
        #drawLineSegmentLeft()
    return i,j


#TODO add checks for index overfow,
def drawLineSegmentv0( matrix, i, j, direction, segLength):
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
drawLine(matrix, 25)
printMatrix(matrix)

