def insert_list(lst, ele, index, i=0):
    '''
    objective: to insert an element into a sorted list using recursion
    parameters: -> lst: original list in which element has to be inserted
                -> ele: element to insert into list
                -> i=0: default parameter index
    return value: none
    '''
    
    if i > index:
        return lst
    if i == index:
        lst.insert(index, ele)
    if i == len(lst):
        lst.append(ele)
    else:
        if lst[i] > ele:
            lst.insert(i,ele)
        else:
            i = i+1
            insert_list(lst, ele, index, i)
    return lst


def sortList(lst, sorted_index=0): 
        '''
        flag = 0
        for i in range(0, sorted_index):
            if lst[i] > lst[participant]:
                flag = 1
                break
    
        if flag == 1:
           lst = insert_list(lst[:sorted_index], lst[participant]) + lst[sorted_index+1:]
        
        sorted_index += 1
        participant += 1
        i += 1
        if participant < len(lst):
            return sortList(lst, sorted_index, participant)
        return lst
        '''
        
        sorted_index = sorted_index + 1 
        if sorted_index == len(lst):
            return lst
        temp = lst[sorted_index]
        del lst[sorted_index]
        return sortList(insert_list(lst, temp, sorted_index), sorted_index)


lst = [4,2,10,3,5,0,11,9,0,100]
print("\nOriginal list: ", lst)
print("\nSorted list: ", sortList(lst))

    
