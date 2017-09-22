
def minOfList(lst, start=0, end=1):
    '''
    objective: to find index of minimum element in the list passed to this function
    parameters: -> lst: list whose minimum has to be found
                -> start: starting index from where min has to be calculated
                -> end: last index upto which min has to be calculated 
    return value: index of smallest element of the list
    '''

    'approach: updating min_element using comparision in recursion and returning its index after traversing completely'
    '''
    if i == 0:
        i = start
        j = start
    
    if i == (end+1):
        return j
    else:
        if lst[i] < lst[j]:
            min_element = lst[i]
            j = i
        i = i+1    
        return minOfList(lst,start, end, i, j)
    '''
    if end == len(lst)-1:
        return start
    elif lst[end] > lst[start]:
        return minOfList(lst, start, end+1)
    else:
        return minOfList(lst, end, end+1)
    


lst = [50,10,30,40,100,0,90]
print(minOfList(lst))
