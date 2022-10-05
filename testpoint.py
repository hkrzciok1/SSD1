def testpoint():
    xcor = 3
    ycor = 5
    test = Point()
    test.set(xcor)
    test.set(ycor)

    assert test.getx() == xcor
    assert test.gety() == ycor


