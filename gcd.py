def GCD(num1, num2):
    '''
    objective: to calculate GCD of 2 input numbers
    parameters: num1 -> first number input by user
                num2 -> second number input by user
    return value: -> GCD of the two numbers passed to this function
    '''
    'approach: using long division method in recursive way'

    if num2==0:
        return num1
    else:
        return GCD(num2, num1%num2)
    

def main():
    '''
    objective: to calculate GCD of 2 input numbers
    user inputs: num1 -> 1st user input number
                 num2 -> 2nd user input number
    '''
    'approach: using function gcd() to cacluate GCD of the two numbers'

    num1 = int(input("Enter the 1st number: "))
    num2 = int(input("Enter the 2nd number: "))
    gcdValue=GCD(num1,num2)
    print ("GCD of the two input numbers: ", gcdValue)

if __name__=='__main__':
    main()
    
