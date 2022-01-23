def parse_int(string):

    dict = {"zero":0,"one":1, "two":2, "three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,
            "ten":10, "eleven":11, "twelve":12, "thirteen":13, "fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19,
            "twenty":20, "thirty":30,"forty":40,"fifty":50,"sixty":60,"seventy":70,"eighty":80,"ninety":90,
            "hundred":100, "thousand":1000, "million":1000000}

    if " and " in string:
        string = string.replace(" and ", " ")
    string = string.replace("-", " ")

    string = string.split(" ")

    n = 0

    if "million" in string:
        return dict["million"]


    if "thousand" in string:
        a = string.index("thousand")

        string1 = string[:a]

        n1 = 0
        if "hundred" in string1:
            b = string1.index("hundred")
            string2 = string[:b]

            b1 = [dict[string2[x]] for x in range(len(string2))]
            b1 = sum(b1)

            n1 = 100*b1

            for i in range(len(string2)):
                string1.pop(i)

            string1.pop(string1.index("hundred"))

        for i in range(len(string1)):
            n1 += dict[string1[i]]

        n += n1*1000

        string = string[a+1:]

    if "hundred" in string:
        a = string.index("hundred")

        n += dict[string[a-1]]*100

        string = string[a+1:]

    for i in range(len(string)):
        n += dict[string[i]]

    return n


print(parse_int("one million"))