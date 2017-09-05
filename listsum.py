def lsum(n,ls):
    '''
    objective: to compute the sum of a list entered by the user
    input parameters:
        n: the total numbers of members in a list
        ls[]: list of the numbers who's sum is to be calculated
    return vale: the function lsum() returns the computed sum
    variables:
        sum: used to store the computed sum of the list
    '''
    '''
    approach: all the members of the list can be accessed using a loop
              the value of the variable sum can be upadated simultaneously
    '''
    sum=0
    for i in range(0,n):
        sum+=ls[i]
    return sum


def main():
    '''
    objective: to compute the sum of a list entered by the user
    user inputs:
        n: the total numbers of members in a list
        ls[]: list of the numbers who's sum is to be calculated
    '''
    '''
    approach: function lsum(n,ls) is being called
    '''
    n= int(input('Enter the total number of members in the list: '))
    print('Enter the members of the list.')
    for i in range(0,n)
        ls[i]=int(input())


if __name__=='__main__':
    main()
    
