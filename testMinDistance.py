from Geometry import Point
from Distance import Distance
from minDistance import calcMinDist

def testMinDist():
	listOfPoints = []

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

	listOfPoints.append(start)
	listOfPoints.append(end)
	listOfPoints.append(p1)
	listOfPoints.append(p2)
	listOfPoints.append(p3)
	
	for point in listOfPoints:
		print(point)

	assert (calcMinDist(listOfPoints) == 1)
	assert(listOfPoints[0] == p1)
	assert(listOfPoints[1] == p2)
