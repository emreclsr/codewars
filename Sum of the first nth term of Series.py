def series_sum(n):
    a=0
    for i in range(n):
        a = a + 1/(3*i+1)
    return "{:.2f}".format(round(a,2))