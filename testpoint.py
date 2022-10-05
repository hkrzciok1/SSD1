def testpoint():
    xcor = 3
    ycor = 5
    test = Point()
    test.setX(xcor)
    test.setY(ycor)

    assert test.getX() == xcor
    assert test.getY() == ycor


