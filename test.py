from random import randint

def interpolate(points, x):
    secretnumber = 0
    for c in range(0, len(points)):  # current point
        print "start outer loop. c is: "
        print c
        print "secretnumber is: "
        print secretnumber
        numerator = 1
        denominator = 1
        for o in range(0, len(points)):  # loop through other points
            if c != o:
                print "in inner loop. o is: "
                print o
                print "numerator and denominator are"
                print numerator
                print denominator
                numerator *= (-1) * points[o][0]  # get x of other point, multiply by -1
                denominator *= ((points[c][0]) - (points[o][0]))  # get (current x - other point x)
                print "after operations, numerator and denominator are:"
                print numerator
                print denominator
        print "exit inner loop"
        indicatorvalue = (numerator / denominator) * (points[c][1])  # multiply by current y value
        print "indicatorvalue is: "
        print indicatorvalue
        secretnumber += indicatorvalue
        print "secret number is "
        print secretnumber
    return secretnumber


polypoints = [(1, 24), (-3, -28), (-4, -71), (3, 62)]
interpolate(polypoints, 0)


