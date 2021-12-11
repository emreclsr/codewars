def unique_in_order(iterable):

    if len(iterable) == 1:
        return list(iterable)

    elif len(iterable) > 0:
        x = list(iterable)
        s = []
        

        for i in range(len(x)-1):
            if x[i] != x[i+1]:
                s.append(x[i])

        s.append(x[-1])
        return s
    else:
        return []