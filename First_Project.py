import math
from Geometry import Point
my_list = []
count = 0
addPoint = ""

while addPoint.lower() != 'no':

    pointInput = input('Enter X'+str(count)+',Y'+str(count)+': ')
    point = Point()
    point.setX(pointInput.split(',')[0])
    point.setY(pointInput.split(',')[1])

    if count >0:
        addPoint = input('Do you want more?')

    try:
        my_list.append(point)
    except ValueError:
        print('Invalid number.')
        continue
    count += 1



print(my_list)

