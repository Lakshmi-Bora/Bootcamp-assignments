# This program is intended to generate appropriate statements according to the input age using if conditions
#Request the user to enter his/her age and cast it to an integer.
age = int (input ("Enter your age :    "))
print ()

#Check the age with the following conditions:
# if the age is above 100,
# or age is 65 or above,
# or age is 40 or above
# or age is 25,
# or age is less than 13,
# or age is other than the above,
# and print the related output.

if age > 100:

    print ("Sorry, you're dead!")

elif age >= 65:  
   
    print ("Enjoy your retirement!")

elif age >= 40:
    
    print ("You're over the hill.")

elif age == 21:
    
    print ("Congrats on your 21st!")

elif age < 13:
    
    print ("You qualify for the kiddie discount.")

else:
    
    print ("Age is but a number")
