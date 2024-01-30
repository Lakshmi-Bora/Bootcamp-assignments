# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") 
'''
Syntax error, as the statement to be printed should be enclosed in parantheses.
'''
print ("\n") 
'''
Syntax error, because of unnecessary indentation.
Syntax error, as the statement to be printed should be enclosed in parantheses.
'''

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24 years old"     
'''
Syntax error, due to unnecessary indentation. 
Runtime error, as "==" is a wrong operator to assign a variable, must be "=".
Runtime error, as the value in the string should be a numerical to cast to an integer type.
'''

for word in age_Str.split():    
    '''Used split() to seperate the numerical and alphabetic words into a list'''   
                            
    if word.isdigit():         
        '''Used the isdigit() to bring out the number from the above list'''
        age_Str = word

age = int(age_Str)  
'''
Syntax error, due to unnecessary indentation.
Runtime error, due to casting the non numerical string value to an integer.
'''

print("I'm" , age , "years old.")   
'''
Syntax error, due to unnecessary indentation.
Runtime error, as '+' was used in between the string and integer types, must be a ','
'''
    # Variables declaring additional years and printing the total years of age
years_from_now = "3.5" 
'''
Synatax Error, due to unnecessary indentation.
Logical error, as the expected output cannot be obtained with the value "3", must be "3.5"
'''

total_years = age + float(years_from_now)   
'''
Syntax error, due to unnecessary indentation.
Runtime error, as the two variables to be added are different types, 
    the "years_from_now" must be casted to a float type.
'''

print ("The total number of years:", total_years) 
'''
Syntax error, due to missing parantheses.
Logical error, as the output is not as expected, the variable should not be enclosed in quotes.
Runtime error, as the variable "answer_years" was not defined earlier,must be "total_years". 
Runtime error, as there is "+" in between different types of variables, must be a ",".
'''

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12  
'''
Runtime error, as the variable "total" was not defined, must be the "total_years"
'''

print ("In 3 years and 6 months, I'll be " , total_months , " months old") 
'''
Syntax error, due to missing parantheses.
Runtime error, as "+" was used in between the string and integer types, must be a ",".
'''

#HINT, 330 months is the correct answer