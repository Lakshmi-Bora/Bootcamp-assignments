#Request the user to enter a sentence.
str_manip = input ("Enter a sentence :    ")
print()

#calculate and print the length of a string.
str_length = len (str_manip)
print (f"The length of your sentence is {str_length}.")
print ()

#Find the last character and replace every occurence of that character with '@',
#and print the new string.
str_manip1 = str_manip
last_char = str_manip[str_length - 1]

for position in range (0,str_length):

    if str_manip1[position] == last_char:
        str_manip1=str_manip1.replace (str_manip1[position],"@")

print ("Your new sentence after replacing characters is :   ", str_manip1)
print ()

#print the last 3 characters of the original string in reverse order.
print ("Last 3 charcaters of your sentence in reverse order is :  ", str_manip[str_length:str_length-4:-1])
print ()

#Add the first 3 characters and last 2 charcters of the string to make new word and print it. 
word = str_manip[0:3] + str_manip[str_length-2 : str_length]
print ("The new word formed with 1st 3 characters and last 2 characters is :   ",word)
print()