def override(l1,l2):
    a=[i[0] for i in l2]
    return sorted(l2+list(filter(lambda x: x[0] not in a,l1)),key=lambda y: y[0])
