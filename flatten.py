def flatten(lst, copylist=[]):
    '''
    objective: to flatten the nested list passed to this function and save it in a new list "copylist"
    parameters: -> lst: the original list which has to be flattened
                -> copylist=[]: the DEFAULT PARAMETER which stores the flattened list
    return value: copylist: the flattened new list
    '''
    
    if len(lst) == 0:
        return copylist
    
    if isinstance(lst[0], list):
        flatten(lst[0], copylist)
    else:
        copylist.append(lst[0])
    return flatten(lst[1:], copylist)
                    
#-------------------------------Global area-----------------------------

print("Case 1: ")
lst = [[[[]]], [[[4]]], 6]
print("Original list: ", lst)
flat_list = flatten(lst)
print("Flattened list: ", flat_list)

print("Case 2: ")
lst = [3, 5, [6,7], [8,9,[10,11],12]]
print("Original list: ", lst)
flat_list = flatten(lst)
print("Flattened list: ", flat_list)
