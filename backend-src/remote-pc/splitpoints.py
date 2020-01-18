import math


def get_split_point(a, b, dist):
    """
    Helper function to get the point between a and b dist away from a

    Parameters:
    -----------
    a  b : tuple
        points on a line
    dist : float
        distance between a and returned point on line ab

    Return:
    -------
    x,y : floats
        point between a and b dist away from a

    """

    dx = b[0] - a[0]
    dy = b[1] - a[1]

    m = dy / dx
    c = a[1] - (m * a[0])

    x = a[0] + (dist**2 / (1 + m**2))**0.5
    y = m * x + c

    if not (a[0] <= x <= b[0]):
        x = a[0] - (dist**2 / (1 + m**2))**0.5
        y = m * x + c

    return x, y


def distance(a, b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
