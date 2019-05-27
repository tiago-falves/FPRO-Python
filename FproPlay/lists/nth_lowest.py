def nth_lowest(lnum, n):

    for i in range(n-1):
        lnum.remove(min(lnum))
    return min(lnum)
