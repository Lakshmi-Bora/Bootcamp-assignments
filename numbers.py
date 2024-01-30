#Request the user to enter 3 different integers.
int1 = int (input ("Enter your first integer :    "))
int2 = int (input ("Enter your second integer :   "))
int3 = int (input ("Enter your third integer :    "))

#Calculate the sum of all the above integers and print it.
sum_int = int1 + int2 + int3
print (f"The sum of your integers :   {sum_int}")

#Subtract the 2nd number from the 1st number and print it.
remaining_int = int1 - int2
print (f"The value remained after subtracting the 2nd integer from the 1st integer :   {remaining_int}")

#Multiply the third number by the first number and print the product.
product_int = int3 * int1
print(f"The product of the 3rd integer multiplied by the 1st integer :   {product_int}") 

# Divide the sum of the above 3 integers by the 3rd integer and print it.
division_int = round (sum_int / int3, 2)
print (f"The value after dividing the sum of your integers by the third number :   {division_int}")
print()