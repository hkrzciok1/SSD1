from Geometry import Point
def testdistance():
	point1 = Point()
	point2 = Point()
	point1.setX(0)
	point1.setY(3)
	point2.setX(4)
	point2.setY(0)
	
	assert Distance(point1, point2) == 5
	
	point1.setX(2)
	point1.setY(-3)
	point2.setX(-4)
	point2.setY(0)
	
	assert Distance(point1, point2) == 3.61
	# we are planning on using 2 places after decimal in our distance function
	
	point1.setX(2.5)
	point1.setY(-3)
	point2.setX(-4)
	point2.setY(6.8)

	assert Distance(point1, point2) == 4.09
