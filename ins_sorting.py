def insert_list(lst, ele, i=0):
    '''
    objective: to insert an element into a sorted list using recursion
    parameters: -> lst: original list in which element has to be inserted
                -> ele: element to insert into list
                -> i=0: default parameter index
    return value: none
    '''
    
    if i == len(lst):
        lst.append(ele)
    else:
        if lst[i] >= ele:
            lst.insert(i,ele)
        else:
            i = i+1
            insert_list(lst, ele, i)
    return lst


def sortList(lst, sorted_index=1, participant=1):

        flag = 0
        for i in range(0, sorted_index):
            if lst[i] > lst[participant]:
                flag = 1
                break
        if flag == 1:
            lst = insert_list(lst[:sorted_index], lst[participant]) + lst[sorted_index+1:]

        sorted_index += 1
        participant += 1
        if participant < len(lst):
            return sortList(lst, sorted_index, participant)
        return lst



lst = [4,2,10,3,5,0,11,9,0,100]
print(sortList(lst))

    
