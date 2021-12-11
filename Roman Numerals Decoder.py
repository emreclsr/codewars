def solution(roman):

    number = 0

    dict1 = {"IV" : 4,
             "IX" : 9,
             "XL" : 40,
             "XC" : 90,
             "CD" : 400,
             "CM" : 900}

    dict2 = {"I" : 1,
             "V" : 5,
             "X" : 10,
             "L" : 50,
             "C" : 100,
             "D" : 500,
             "M" : 1000}

    for i in range(len(list(dict1.keys()))):
        if list(dict1.keys())[i] in roman:
            number += list(dict1.values())[i]
            roman = roman.replace(list(dict1.keys())[i], "")

    for i in range(len(list(dict2.keys()))):
        count = roman.count(list(dict2.keys())[i])
        number += count*list(dict2.values())[i]
        roamn = roman.replace(list(dict2.keys())[i], "")


    return number