#This program is to print the list of factors and their sum for a given number
num == int(input("Please enter a number for which the sum of factors to be calcualted: ")) 
#Compilation error due to using "==" instead of "=" for assigning a variable
sum = "0"    # Leads to runtime error in line 13, as 
            #  "0" must not be enclosed in quotes as we assigned it for the purpose of arithmetic calculations.
factors = []
for i in range(0,num): # runtime error because of division by zero, range must not include '0' to solve this
                       # Logical error even after started the range from 1, 
                       #          as the output will not include the number given itself,
                        #         "num + 1" should be given in the place of "num" in range to correct this
    if num % i == 0     # Compilation error because of not using ":" at the end of the if statement.
        factors.append(i)
    sum += i            # Logical error, as it is printing the sum of the "num+1" numbers 
                        #      instead of the sum of the factors of the "num" 
                        #   To correct this sum += i  should be given in the if condition block
print f"The factors list of the geiven number is : {factors}" #Compilation error as the statement or variable to be printed must be enclosed in parantheses. 
print(f"The sum of the factors is : {sum}")

