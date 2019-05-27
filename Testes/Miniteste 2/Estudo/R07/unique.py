def unique(atuple):
    atuple=list(atuple)
    s=()
    for i in atuple:
        if i not in s:
            s+=(i,)
    s=tuple(sorted(s))
    return s
