"""
Implement the function unique_in_order which takes as argument a sequence 
and returns a list of items without any elements with the same value next
to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""

def unique_in_order(iterable):

    if len(iterable) == 1:
        return list(iterable)

    elif len(iterable) > 0:
        x = list(iterable)
        s = []
        

        for i in range(len(x)-1):
            if x[i] != x[i+1]:
                s.append(x[i])

        s.append(x[-1])
        return s
    else:
        return []

    
    
print(unique_in_order("ABBCcAD"))
