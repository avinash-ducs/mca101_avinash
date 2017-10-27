import pdb
pdb.set_trace()
def merging(lst1, lst2, i=0, j=0,newlist=[]):
    ''' 
    objective: to merge two sorted lists passed to this function
    parameters: -> lst1: 1st list passed
                -> lst2: 2nd list passed
                -> i=0: DEFAULT PARAMETER used to traverse through list1
                -> j=0: DEFAULT PARAMETER used to traverse through list2
                -> newlist=[]: DEFAULT PARAMETER which stores the merged list
    return value: -> newlist: the newly created list by merging the 2 lists sent as input
    ''' 
    
    if i == len(lst1):
        newlist = newlist + lst2[j:]
        return newlist
        
    if j == len(lst2):
        newlist= newlist + lst1[i:]
        return newlist
    
    if lst1[i] < lst2[j]:
        newlist.append(lst1[i])
        i = i+1
    elif lst1[i] > lst2[j]:
        newlist.append(lst2[j])
        j = j+1
    return merging(lst1, lst2, i,j,newlist)
        
#-----------------Global area----------------
        
list1 = [10,12,14,16,18,100]
list2 = [11,13,15]
print("List1: ", list1)
print("List2: ", list2)
print("Merged list: ", merging(list1,list2))
