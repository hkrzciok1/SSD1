from Geometry import Point
from Distance import Distance

"""
calcMinDist function passes in a list of points whos first 2 items are
place holders for the start and end point of the minimum distance.
"""
def calcMinDist(Points):

	minDist = Distance(Points[2],Points[3])
	Points[0] = Points[2]
	Points[1] = Points[3]

	for i in Points[2:]:
		for j in Points[2:]:
			if(i != j):
				tempDist = Distance(i,j)
				if(tempDist < minDist):
					minDist = tempDist
					Points[0] = i
					Points[1] = j
	return minDist
