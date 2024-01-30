# This programme is to print squares of prime numbers upto a given number

max_num = int(input("Please enter a number upto which the prime numbers to be taken : "))

print("The Squares of the prime numbers upto the given number are : ")

for num in range(2, max_num + 1):
    is_prime = True
    '''
    All the numbers from 2 to the given maximum number are assigned as prime numbers intially.
    '''
    for factor in range(2, num):
        '''
        Each number is divided by the numbers from 2 to that number
        '''
        if num % factor == 0:
            is_prime = False
            break
            '''
            If number is divisible by any number from 2 to number-1, it cannot be a prime number.
            Then the number will be assigned as not prime and 
            the inner for loop will be stopped iterating here, and the outer loop iteration continues
            '''
        else: 
            is_prime = True
            '''
            Otherwise number will be assigned as prime.

            Here in each iteration the number is being assigned as prime number,
                 as it cannot be divisible by any of the numbers from 2 to number-1
            
            Hence, in each iteration the below if condition is returning true and performing
              the calculation given in that block and printing the result, 
              which leads to a logical error, printing the same result for number-2 times.
              For example: If the user's input is 7, instead of returning 3, 5, 7 once,
                its returning 3 --- once
                              5 --- 3 times
                              7 --- 5 times              
            '''
    
        if is_prime == True: 
            '''
             To prevent the logical error mentioned in the above docstring, 
             this if condition should be executed only after all the iterations of the inner for loop are completed.                
             Therefore, it should not be given in the inner for loop.
            '''
            sq_num = num ** num 
            '''
            Logic error: "**" were printed in the above expression instead of "*",
              which leads to a wrong mathematical operation: 
              number to the power of number is being returned instead of the number squared.
              For example: 7^7 is being returned instead of 7x7, 
              '''
            print (f"{sq_num}", end=" ")