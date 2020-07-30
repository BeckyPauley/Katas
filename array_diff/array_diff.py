def array_diff(a, b):
    thislist = []
    [thislist.append(i) for i in a if i not in b]
    return thislist