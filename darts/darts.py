from math import sqrt


def score(x, y):
    lugar_dardo = sqrt(x * x + y * y)

    if lugar_dardo <= 1.0:
        return 10
    elif lugar_dardo <= 5.0:
        return 5
    elif lugar_dardo <= 10.0:
        return 1
    else:
        return 0
