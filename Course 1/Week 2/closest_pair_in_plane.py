import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dist(p1, p2):
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

def bruteForce(array):
    min_dist = float('inf')
    point1 = None
    point2 = None
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if dist(array[i], array[j]) < min_dist:
                min_dist = dist(array[i], array[j])
                point1 = array[i]
                point2 = array[j]
    
    return min_dist, point1, point2

def splitClosestPair(stripArray):
    print(len(stripArray))
    if len(stripArray) > 8:
        print("Breaking the Laws of Math. Killing Programme")
        return
    min_dist = float('inf')
    point1 = None
    point2 = None
    stripArray.sort(key = lambda point:point.y)
    for i in range(len(stripArray) - 1):
        if dist(stripArray[i], stripArray[i + 1]) < min_dist:
            min_dist = dist(stripArray[i], stripArray[i + 1])
            point1 = stripArray[i]
            point2 = stripArray[i + 1]
    
    return min_dist, point1, point2

def closestPairRecur(arrayX, arrayY):
    numPoints = len(arrayX)
    if numPoints <= 3:
        return bruteForce(arrayX)
    else:
        mid = numPoints // 2

        minDistInLeft, leftPoint1, leftPoint2 = closestPairRecur(arrayX[:mid], arrayY)
        minDistInRight, rightPoint1, rightPoint2 = closestPairRecur(arrayX[mid:], arrayY)

        minDistInHalf = min(minDistInLeft, minDistInRight)
        strip = []
        midPoint = arrayX[mid]
        for i in range(numPoints):
            if abs(arrayX[i].x - midPoint.x) < minDistInHalf:
                strip.append(arrayX[i])

        minDistSplit, splitPoint1, splitPoint2 = splitClosestPair(strip)

        if minDistSplit < minDistInHalf:
            return minDistSplit, splitPoint1, splitPoint2
        elif minDistInLeft <= minDistInRight:
            return minDistInLeft, leftPoint1, leftPoint2
        else:
            return minDistInRight, rightPoint1, rightPoint2


def closestPair(arrayOfPoints):
    arrangedByX = sorted(arrayOfPoints, key = lambda point: point.x)
    arrangedByY = sorted(arrayOfPoints, key = lambda point: point.y)

    closestPairDist, point1, point2 = closestPairRecur(arrangedByX, arrangedByY)
    return "Points: " + "(" + str(point1.x) + "," + str(point1.y) + ") and (" + str(point2.x) + "," + str(point2.y) + "). Distance: " + str(closestPairDist)

p = [Point(25,3), Point(12,30), Point(40,50), Point(1,1), Point(12,10),
Point(10,4), Point(15,20), Point(25,18), Point(40,35),
Point(90,4), Point(17,12), Point(49,9), Point(11,21)]
print(closestPair(p))