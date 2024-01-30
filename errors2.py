# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"
'''
Runtime error, as "Lion" is being treated as an undefined variable. 
It must be enclosed in quotes to be treated as a string value.
'''

animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"
'''
Logical error, as the output is not as expected.
"f" should be given in front of the value statement to print the values instead of variables,
and also the variables "number_of_teeth" and "animal_type" should be interchanged the places
     to achieve the desired output
'''

print (full_spec)
'''
Syntax error, as the statement to be printed must be enclosed in parantheses.
'''
