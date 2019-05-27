def formal(name):
    name=name.split()
    s=name[len(name)-1]+","
    for i in range(len(name)-1):
        s+=" "+ name[i][0]+"."
    return s
