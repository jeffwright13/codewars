#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

def main():
    print regression_line([],[])

def regression_line(x, y):
    """ 
    Description
    ===========
    A linear regression line has an equation in the form Y = a + bX, where X is the explanatory variable and Y is the dependent variable. The parameter b represents the slope of the line, while a is called the intercept (the value of y when x = 0).

    For more details visit the related wikipedia page: http://en.wikipedia.org/wiki/Simple_linear_regression

    The function that you have to write accepts two arguments, both in the form of a list/array, x and y, both representing the coordinates of the points to regress (so that, for example, the first point has coordinates (x[0], y[0]).

    Your function should return a tuple (in Python) or an array (any other language) of two elements: a (intercept) and b (slope) in this order.

    Formula Hint
    ============
    a =  [(Σx²)(Σy) - (Σx)(Σxy)]  /  [n(Σx²) - (Σx)²]
    b =  [n(Σxy) - (Σx)(Σy)] / [n(Σx²) - (Σx)²]
    """
    if len(x) != len(y):
        return 'Invalid input arrays'

    n = len(x)
    print "n=", n
    a = 0.0
    b = 0.0
    sum_x = 0.0
    sum_y = 0.0
    sum_x_sq = 0.0
    sum_xy = 0.0

    for i in range(n):
        sum_x += x[i]
        sum_y += y[i]
        sum_x_sq += x[i]**2
        sum_xy += x[0] * y[0]

    a = ((sum_x_sq * sum_y) - (sum_x * sum_xy)) / ((n * sum_x_sq) - sum_x**2)
    b = ((n * sum_xy) - (sum_x * sum_y)) / ((n * sum_x_sq) - sum_x**2)

    return (round(a, 4), round(b, 4))

def test_regression_line():
    assert regression_line([56,42,72,36,63,47,55,49,38,42,68,60], [147,125,160,118,149,128,150,145,115,140,152,155]) == (80.7777, 1.1380)
    assert regression_line([25,30,35,40,45,50], [78,70,65,58,48,42]) == (114.381, -1.4457)

if __name__ == "__main__":
    main()
