def ips_between(start, end):

    start = start.split(".")
    end = end.split(".")

    dif = [int(end[x]) - int(start[x]) for x in range(len(start))]

    return dif[0]*(256**3) + dif[1]*(256**2) + dif[2]*(256) + dif[3]

    print(start, end, dif)

    return

print(ips_between("10.0.0.0", "10.0.0.50"))

