def calcCosine(num):
    '''
    objective: to calculate cosine of an input number using the cosine sequence
    parameters: num -> user input number which has to be converted to cosine
    return value: totalSum -> cosine conversion of the number passed as parameter to this function
    '''
    'approach: using cosine sequence'

    currentTerm = 1
    totalSum = 0
    divFactor=1
    mulFactor = -num*num
    nextInSeq = 1
    epsilon = 0.0000001
    while abs(currentTerm) > epsilon:
        totalSum+=currentTerm
        divFactor=nextInSeq*(nextInSeq+1)
        currentTerm*=mulFactor/divFactor
        nextInSeq+=2
    return totalSum
        
        

def main():
    '''
    objective: to calculate cosine of an input number using the cosine sequence
    user inputs: number -> number input from user
    '''
    'approach: using function calcCosine() to find cosine of the number'

    number = float(input("Enter the number: "))
    cosine = calcCosine(number)
    print("Cosine of the given number = ", cosine)


if __name__ == '__main__':
    main()
        
    
    
