def maxAtIndex(lst, index, i=0):
    '''
    objective: to place heaviest element of the list till "index" at position "index" 
    parameters: -> lst: the original list which has to be modified
                -> index: the index at which maximum element has to be placed
                -> i=0: DEFAULT PARAMETER used to traverse through the list
    return value: none
    '''
    
    if i == index:
        return
    if lst[i] >= lst[i+1]:
        lst[i], lst[i+1] = lst[i+1], lst[i]
    return maxAtIndex(lst, index, i+1)
    
#-------------------------------Global area-----------------------------

lst = [45, 330, 20, 100, 875, 99, 30]
index = 3
if index >= len(lst):
    print("Index is out of range, enter index in range of size of list")
else:     
    print("Original list: ", lst)
    maxAtIndex(lst, index)
    print("List after modification: ", lst)
