#Create a variable to store the original string
string = "The!quick!brown!fox!jumps!over!the!lazy!dog."

#Replace "!" in the original string with one empty space and print it out.

new_string = string.replace ("!"," ")
print ("The new string is :    ", new_string)
print ()

#Print the new string in upper case.
print ("The new string in upper case is :    ", new_string.upper())
print ()
 
#Print the new string in reverse order.
print ("The new string in reverse is :    ", new_string[::-1])