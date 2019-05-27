def count_elems(tup):
    new=()
    for i in tup:
        if type(i).__name__=="list" or type(i).__name__=="tuple" or type(i).__name__=="str":
            new+=(len(i),)
        else:
            new+=(1,)
    return new
