def multiply(num1, num2, number):
    
    if num2 == 1:
        return num1
    else:
        num1 = num1 + number
        return multiply(num1, num2-1, number) 
        
        

def main():
    
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    product = multiply(num1, num2, num1)
    print(num1, "x", num2, "= ", product)

if __name__ == '__main__':
    main()
