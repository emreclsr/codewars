"""
Create a function that takes a Roman numeral as its argument 
and returns its value as a numeric decimal integer. You don't 
need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal 
digit of the number to be encoded separately, starting with 
the leftmost digit and skipping any 0s. So 1990 is rendered 
"MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered 
"MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, 
"MDCLXVI", uses each letter in descending order.

solution('XXI') # should return 21

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
"""
#%%
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


    print(number)

solution("MDCLXVI")

    




