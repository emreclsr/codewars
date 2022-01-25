def validBraces(string):

    par = (")", "]", "}")
    antipar = {")":"(", "]":"[", "}":"{"}

    while True:
        dic = {x: string.find(x) for x in par if x in string}
        if len(dic.items()) == 0:
            return False
        mini = min(dic, key=dic.get)
        if string[dic[mini]-1] == antipar[mini]:
            string = string[:dic[mini]-1] + string[dic[mini]+1:]
        else:
            return False
        if len(string) == 0:
            return True

