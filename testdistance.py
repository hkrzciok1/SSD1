from Geometry import Point
def testdistance():
	point1 = Point()
	point2 = Point()
	point1.setX(0)
	point1.setY(3)
	point2.setX(4)
	point2.setY(0)
	
	assert Distance(point1, point2) == 5
	
	
