def unique(atuple):
    tup=()
    for i in atuple:
        if i not in tup:
            tup+=(i,)
    return tuple(sorted(tup,key=None))
