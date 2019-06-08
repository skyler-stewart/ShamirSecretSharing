# Skyler Stewart
# skmastew@ucsc.edu
# CS 42 Winter 2019
# Secret Sharer

import random
from fractions import Fraction

# val is the secret (the value when x = 0).
# n is the number of points to distribute.
# k is the number of points needed to reconstruct the polynomial.
# Return a list of n random points such that x != 0 for every point.
def split(val, n, k):
    polynomial = []  # creates a list to store the coefficents of the polynomial
    for i in range(1, k-1):
        coefficient = random.randint(1, 10000)
        polynomial.append(coefficient)
    polynomial.append(val)  # append secret value to the end

    shares = []
    xvalues = random.sample(range(1, 10000), n)  # generates x values for shares (no repeating xs)
    for j in range(0, n):
        newpoint = calculatePoint(polynomial, xvalues[j])
        shares.append(newpoint)
    return shares


# points is a list of shares.
# x is the x-coordinate in which to compute the secret at.
# Return the computed secret value.
def interpolate(points, x):
    secretnumber = 0
    for c in range(0, len(points)):  # current point
        indicatorFraction = Fraction(1, 1)
        for o in range(0, len(points)):  # loop through other points
            if c != o:
                updatedFraction = Fraction(indicatorFraction.numerator*(x - points[o][0]), # get (current x - other point x)
                                        indicatorFraction.denominator*((points[c][0]) - (points[o][0])))  # subtract x of other point from x
                indicatorFraction = updatedFraction
        finalFraction = indicatorFraction * (points[c][1]) # multiply by current y value
        secretnumber += finalFraction
    return secretnumber


# poly is the polynomial (coefficients) we want to evaluate
# xvalue is what the polynomial is evaluated at
def calculatePoint(poly, xvalue):
    temp = poly[-1]
    for i in range(1, len(poly)):
        temp = temp * xvalue + poly[i]
    point = (xvalue, temp)
    return point


