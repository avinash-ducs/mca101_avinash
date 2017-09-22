
def minOfList(lst, start, end):
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
    if start == end:
        return end
    elif lst[end] > lst[start]:
        return minOfList(lst, start, end-1)
    else:
        return minOfList(lst, start+1, end)
    
		
    

def SelectionSort(lst, index=0):
    '''
    objective: to implement selection sort using recursive function minOfList()
    parameters: -> lst: list which has to be sorted
                -> index: DEFAULT PARAMETER used to traverse the list
    return value: none
    '''

    'approach: finding the minimum element and swapping one by one'
    
    if index == len(lst):
        return
    
    min_index = minOfList(lst, index, len(lst)-1)
    lst[index],lst[min_index] = lst[min_index], lst[index]
    return SelectionSort(lst, index+1)
    

    
lst = [50,10,30,0,40,100,90,0]
print("\nInitial list: ", lst)
SelectionSort(lst)
print("\nSorted list: ", lst)


