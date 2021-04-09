import Telecomunication


def findCoordinats(area):
    for i in range(len(area)):
        for j in range(len(area)):
            if area[i][j] != 0:
                return i, j


def nextPoint(area, xPoint, yPoint):
    for i in range(len(area)):
        if area[xPoint][i] != 0 and i != yPoint:
            yPoint = i


    for i in range(len(area)):
        if area[i][yPoint] != 0 and i != xPoint:
            xPoint = i
    return xPoint, yPoint

def printCoordinates(area):
    x,y = findCoordinats(area)
    print(x,y,end='')
    x,y = nextPoint(area,x,y)
    while x and y!=findCoordinats(area):
        print(x,y, end=' ')
        x,y = nextPoint(area,x,y)
