from Geometry import Point
from Distance import Distance
from minDistance import calcMinDist

def testMinDist():
	listOfPoints = []

	distance = 0
	start = None
	end = None

	p1 = Point()
	p1.setX(1)
	p1.setY(1)

	p2 = Point()
	p2.setX(1)
	p2.setY(2)

	p3 = Point()
	p3.setX(4)
	p3.setY(4)

	listOfPoints.append(p1)
	listOfPoints.append(p2)
	listOfPoints.append(p3)
	
	
	for point in listOfPoints:
		print(point)
	distance,start,end = calcMinDist(listOfPoints)
	assert (distance == 1)
	assert(start == p1)
	assert(end == p2)
