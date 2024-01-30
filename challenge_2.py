#Request the user to enter his/her favourite restaurant's name and favorite integer.
string_fav = input ("Enter your favourite restaurant's name :    ")
int_fav = int (input("Enter your favourite number :    "))

#Print the above as 2 seperate statements.
print (f"Your favourite restaurant's name is {string_fav}")
print (f"Your favourite number is {int_fav}")

#Now cast string_fav to an integer.
string_fav = int (string_fav)
print (f"{string_fav}")

#It is giving value error as the string_fav contains alphabets.
#int() cannot be used on characters other than numerical value.
#Showing the output without error only if the number is given as input.