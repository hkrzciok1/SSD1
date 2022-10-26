# import this function into the test


import math
from Geometry import Point

def Distance(pt1, pt2):
	# finds distance between two points, rounded to 2 decimal points
	x1=pt1.getX()
	y1=pt1.getY()
	x2=pt2.getX()
	y2=pt2.getY()

	result = math.sqrt((x2-x1)**2+(y2-y1)**2)
	return round(result, 2)
