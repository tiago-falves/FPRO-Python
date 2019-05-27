#1. Flatten

def flatten(alist):
    if isinstance(alist, list):
        if len(alist) == 0:
            return []
        first, rest = alist[0], alist[1:]
        return flatten(first) + flatten(rest)
    else:
        return [alist]