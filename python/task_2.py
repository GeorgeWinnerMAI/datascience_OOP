def cmp2(x, y):
    return min(x, y)


def cmp3(x, y, z):
    return min(x, y, z)


def copies(x, y, z):
    a = (x == y) + (x == z) + (y == z)
    if a == 1:
        return 2
    return a


print(cmp3(1, 7, 12))
