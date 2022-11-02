from Geometry import Point
from Distance import Distance

"""
calcMinDist function passes in a list of points and
returns the distance, start and end point of the minimum distance.
"""
def calcMinDist(Points):

	startIndex = 0
	endIndex = 1
	minDist = Distance(Points[0],Points[1])

	for i in Points:
		for j in Points:
			if(i != j):
				tempDist = Distance(i,j)
				if(tempDist < minDist):
					minDist = tempDist
					startIndex = i
					endIndex = j

	return minDist,Points[startIndex],Points[endIndex]
