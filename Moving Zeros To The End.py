def move_zeros(array):
    
    if len(array) > 0:
        a=0
        for i in range(len(array)):
            if array[i] == 0:
                a +=1

        array = [x for x in array if x != 0]

        for i in range(a):
            array.append(0)
    
    return array