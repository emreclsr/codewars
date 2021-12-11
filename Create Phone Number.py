def create_phone_number(n):
    n = [str(x) for x in n]
    a = "".join(n[:3])
    b = "".join(n[3:6])
    c = "".join(n[6:])

    return '(' + str(a) + ") " + str(b) + "-" + str(c)