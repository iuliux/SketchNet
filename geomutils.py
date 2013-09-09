import math


def line_angle(line):
    '''Returns the angle of @line relative to OX axis.'''
    p1, p2 = line
    xDiff = p2[0] - p1[0]
    yDiff= p2[1] - p1[1]
    return math.degrees(math.atan2(yDiff, xDiff))


def line_len(line):
    l = math.sqrt((line[0][0] - line[1][0])**2 + (line[0][1] - line[1][1])**2)
    return l
