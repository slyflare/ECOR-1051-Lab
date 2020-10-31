import math


# excersise 1

def area_of_disk(radius):
    """Return the area of a disk with the specified non-negative radius
    >>> area_of_disk(5)
    78.53981633974483
    >>> area_of_disk(11)
    380.132711084365
    >>>area_of_disk(0)
    0
    """
    return math.pi * radius ** 2


area = area_of_disk(5)
print(area)
area = area_of_disk(5.0)
print(area)


# excersise 2

def distance(x1, y1, x2, y2):
    """Return the distance between 2 points with the difference between the x values and the y values of the 2 points
    >>> distance(4,5,1,1)
    5.0
    >>> distance(3,2,4,6)
    4.123105625617661
    >>> distance(6,7,1,2)
    7.0710678118654755
    >>>distance(1,1,0,0)
    1.4142135623730951
    """
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


test = distance(5, 4, 0, 0)
print(test)


# excersise 3

def area_of_circle(x1, y1, x2, y2):
    """Returns the area of a circle with a radius given by the distance between 2 points.
    >>>area_of_circle(4,5,1,1)
    78.53981633974483
    >>>area_of_circle(1,2,3,4)
    25.132741228718345
    >>>area_of_circle(6,7,1,2)
    157.07963267948966
    >>>area_of_circle(1,1,1,1)
    0
    """
    return math.pi * ((x1 - x2) ** 2 + (y1 - y2) ** 2)


test = area_of_circle(8, 2, 7, 1)
print(test)


# excersise 4

def height(ladder, angle):
    """ Returns the vertical height that the ladder covers when placed against the wall using the length of the ladder
    in meters and the angle from the floor to the ladder in degrees.
    >>>height(math.sqrt(2),45)
    1
    >>>height(1.3,34)
    0.726950774511971
    >>>height(2.4,66)
    2.192509098342242
    >>>height(1.9,87)
    1.8973961160336903
    """
    return ladder * math.sin(math.radians(angle))


test = height(1.3, 57)
print(test)
