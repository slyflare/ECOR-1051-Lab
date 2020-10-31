# ECOR 1051 Lab 12 File: lab12-linearRegression.py

from typing import Set, Tuple
# See Practical Programming, Chapter 8, section Type Annotations For Lists,
# and Chapter 11, first paragraph of section Creating New Type Annotations. 

def get_points() -> Set[Tuple[float, float]]:
    """Return a set of (x, y) points.
    >>> get_points()
    {(3.5, 12.5), (2.0, 8.0), (1.0, 5.0)}
    >>> samples = get_points()

    >>> len(samples)  # How many tuples (points) are in the set?
    3
    >>> samples
    {(3.5, 12.5), (2.0, 8.0), (1.0, 5.0)}
    """
    return {(1.0, 5.0), (2.0, 8.0), (3.5, 12.5)}


def fit_line_to_points(points:Set[Tuple[float,float]]) -> Tuple[float,float]:
    """Takes a set of x,y coordinates and returns the gradient and y intersect of the line of best fit
    >>>fit_line_to_points({(3.5, 12.5), (2.0, 8.0), (1.0, 5.0)})
    3.0, 2.0
    >>>fit_line_to_points({(4.6,4.3,),(7.8,1.5)})
    -0.8749999999999962, 8.324999999999974
    """
    sumx = 0
    sumy = 0
    n = 0
    sumxy = 0
    sumxx = 0
    for i in points:
        sumx += i[0]
        sumy += i[1]
        n += 1
        sumxy += i[0]*i[1]
        sumxx += i[0]**2
    m = (sumx * sumy - n * sumxy)/(sumx * sumx - n * sumxx)
    c = (sumx * sumxy - sumxx * sumy)/(sumx * sumx - n * sumxx)
    return m, c


def best_line(file:str) -> str:
    """Returns the equation of the line of best fit using data read from a file"""
    x = input("Input file name:")
    (m, c) = fit_line_to_points(read_points(x))
    final = 'best line is y = ', str(m), 'x + ', str(c)
    return ''.join(final)


def read_and_print_lines() -> None:
    """Reads and prints data from a separate file"""
    infile = open('lab12-data.txt', 'r')
    for line in infile:
        print(line)
    infile.close()


def read_points(filename:str) -> Set[Tuple[float,float]]:
    """Reads data from a separate file and converts them into 2 float points"""
    infile = open(filename, 'r')
    points = {1}
    for line in infile:
        s = line.split()
        nums = (float(s[0]), float(s[1]))
        points.add(nums)
    infile.close()
    points.remove(1)
    return points


test = best_line('lab12-data.txt')
print(test)