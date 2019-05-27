def sort_grades(records):
    return tuple(sorted(sorted(sorted(records,key=lambda x: x[1]),key=lambda y: y[0]),key=lambda z:sum(z[2])//len(z[2]),reverse=True))
