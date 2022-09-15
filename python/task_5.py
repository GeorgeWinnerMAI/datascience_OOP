def list_even(ls):
    return ls[::2]


def list_bigger(ls):
    return [ls[i+1] for i in range(len(ls)-1) if ls[i+1] > ls[i]]


def swap_minmax(ls):
    ls[ls.index(max(ls))], ls[ls.index(min(ls))] = ls[ls.index(min(ls))], ls[ls.index(max(ls))]
    return ls