def array_diff(a, b):
    c=[]
    if len(b) > 0:
        for i in range(len(b)):
            a = [x for x in a if x != b[i]]
    else:
        a

    return a