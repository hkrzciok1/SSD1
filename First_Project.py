import math
from Geometry import Point
from minDistance import calcMinDist

my_list = []
count = 0
addPoint = ""

while addPoint.lower() != 'no':

    pointInput = input('Enter X' + str(count) + ',Y' + str(count) + ': ')
    point = Point()
    point.setX(int(pointInput.split(',')[0]))
    point.setY(int(pointInput.split(',')[1]))

    if count > 0:
        addPoint = input('Do you want more?')

    try:
        my_list.append(point)
    except ValueError:
        print('Invalid number.')
        continue
    count += 1


MinD, pt1, pt2 = calcMinDist(my_list)
print('The smallest distance is ', str(MinD))
print('The first point is ', pt1.getX(), ',' , pt1.getY())
print('The second point is ', pt2.getX(), ',' , pt2.getY())
