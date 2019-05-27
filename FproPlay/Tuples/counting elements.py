def count_until(tup):
    for i in range(len(tup)-1):
        if type(tup[i+1]).__name__=="tuple":
            return i+1
    return -1
