def zero(x = None): #your code here
    if x == None:
        return 0
    elif x[0] == "+":
        return x[1]+0
    elif x[0] == "-":
        return 0-x[1]
    elif x[0] == "*":
        return x[1]*0
    elif x[0] == "//":
        return 0//x[1]

def one(x = None): #your code here
    if x == None:
        return 1
    elif x[0] == "+":
        return x[1]+1
    elif x[0] == "-":
        return 1-x[1]
    elif x[0] == "*":
        return x[1]*1
    elif x[0] == "//":
        return 1//x[1]

def two(x = None): #your code here
    if x == None:
        return 2
    elif x[0] == "+":
        return x[1]+2
    elif x[0] == "-":
        return 2-x[1]
    elif x[0] == "*":
        return x[1]*2
    elif x[0] == "//":
        return 2//x[1]

def three(x = None): #your code here
    if x == None:
        return 3
    elif x[0] == "+":
        return x[1]+3
    elif x[0] == "-":
        return 3-x[1]
    elif x[0] == "*":
        return x[1]*3
    elif x[0] == "//":
        return 3//x[1]

def four(x = None): #your code here
    if x == None:
        return 4
    elif x[0] == "+":
        return x[1]+4
    elif x[0] == "-":
        return 4-x[1]
    elif x[0] == "*":
        return x[1]*4
    elif x[0] == "//":
        return 4//x[1]

def five(x = None): #your code here
    if x == None:
        return 5
    elif x[0] == "+":
        return x[1]+5
    elif x[0] == "-":
        return 5-x[1]
    elif x[0] == "*":
        return x[1]*5
    elif x[0] == "//":
        return 5//x[1]

def six(x = None): #your code here
    if x == None:
        return 6
    elif x[0] == "+":
        return x[1]+6
    elif x[0] == "-":
        return 6-x[1]
    elif x[0] == "*":
        return x[1]*6
    elif x[0] == "//":
        return 6//x[1]

def seven(x = None): #your code here
    if x == None:
        return 7
    elif x[0] == "+":
        return x[1]+7
    elif x[0] == "-":
        return 7-x[1]
    elif x[0] == "*":
        return x[1]*7
    elif x[0] == "//":
        return 7//x[1]

def eight(x = None): #your code here
    if x == None:
        return 8
    elif x[0] == "+":
        return x[1]+8
    elif x[0] == "-":
        return 8-x[1]
    elif x[0] == "*":
        return x[1]*8
    elif x[0] == "//":
        return 8//x[1]

def nine(x = None): #your code here
    if x == None:
        return 9
    elif x[0] == "+":
        return x[1]+9
    elif x[0] == "-":
        return 9-x[1]
    elif x[0] == "*":
        return x[1]*9
    elif x[0] == "//":
        return 9//x[1]

def plus(x): #your code here
    return "+",x
def minus(x): #your code here
    return "-",x
def times(x): #your code here
    return "*",x
def divided_by(x): #your code here
    return "//",x