def solution(n):
    dic = {"I":1, "IV":4, "V":5, "IX":9, "X":10, "XL":40, "L":50, "XC":90, "C":100, "CD":400, "D":500, "CM":900, "M":1000}
    letter = list(dic.keys())
    number = list(dic.values())

    a = n//1000
    b = (n-a*1000)//100
    c = (n-a*1000-b*100)//10
    d = (n-a*1000-b*100-c*10)//1

    num = [a*1000, b*100, c*10, d]

    s = []

    for i in range(a):
        s.append(letter[number.index(1000)])

    if b == 9:
        s.append(letter[number.index(900)])
    if b >= 5 and b < 9:
        s.append(letter[number.index(500)])
    if b > 5 and b < 9:
        for i in range(b-5):
            s.append(letter[number.index(100)])
    if b == 4:
        s.append(letter[number.index(400)])
    if b > 0 and b < 4:
        for i in range(b):
            s.append(letter[number.index(100)])
        
    if c == 9:
        s.append(letter[number.index(90)])
    if c >= 5 and c < 9:
        s.append(letter[number.index(50)])
    if c > 5 and c < 9:
        for i in range(c-5):
            s.append(letter[number.index(10)])
    if c == 4:
        s.append(letter[number.index(40)])
    if c > 0 and c < 4:
        for i in range(c):
            s.append(letter[number.index(10)])

    if d == 9:
        s.append(letter[number.index(9)])
    if d >= 5 and d < 9:
        s.append(letter[number.index(5)])
    if d > 5 and d < 9:
        for i in range(d-5):
            s.append(letter[number.index(1)])
    if d == 4:
        s.append(letter[number.index(4)])
    if d > 0 and d < 4:
        for i in range(d):
            s.append(letter[number.index(1)])
    
    
        
    s = "".join(s)


    return s