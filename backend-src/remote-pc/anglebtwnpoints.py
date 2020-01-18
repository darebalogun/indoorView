import numpy
import splitpoints


def getangle(a, b):
    x = (a[1] - b[1])/(splitpoints.distance(a, b))
    if (b[0] >= a[0]):
        return numpy.arcsin(x)
    else:
        return numpy.pi - numpy.arcsin(x)
