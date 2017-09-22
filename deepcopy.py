def myDeepCopy(lst):
    
    copylist = []
    for i in lst:
        if isinstance(i, list):
            copylist.append(myDeepCopy(i))
        else:
            copylist.append(i)
    return copylist









lst = [3, 5, [6,7], [8,9,[10,11],12]]
print(lst)
print(myDeepCopy(lst))

