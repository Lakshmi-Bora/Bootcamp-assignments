'''
#This programme is intended to request a max. number of stars in a line from user 
# and print the following pattern:
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *


num_stars  = int(input(" Please enter the maximum no. of stars in a line \
you want to be printed in patteren :  "))'''

'''
stars_list = ""
index = num_stars 

for i in range(0,num_stars * 2):

    if i < num_stars:
        stars_list += "*"
        print(stars_list)
        
    else:
        index -= 1
        stars_list = stars_list [0:index]
        print(stars_list)

 '''
'''       
for i in range (0,num_stars*2):

    if i <= num_stars:
        stars_list = "*" * i
        print(stars_list)

    else:
        stars_list = stars_list[:-1]
        print(stars_list)
'''
'''
num_lines = int(input("Please enter the number of lines you want in the pattern : "))
spaces = " " * (num_lines)

for i in range(num_lines * 2 ):
    
    if i < num_lines:

        stars = (i * 2 + 1) * "*"
        spaces = spaces[:-1]

    else:

        spaces = spaces + " "
        stars = stars[:-2]
        
    stars_list = spaces + stars
    print (stars_list)
''' 

while True:
    try:
        num_lines = int(input("Please enter the number of lines you want in the pattern(5 or above): "))        
        if num_lines >= 5:

            left_spaces = " " * (num_lines)
            middle_spaces = " "
            index = 0

            for i in range(num_lines * 2):
                
                if i < num_lines:

                    stars = (i * 2 + 1) * "*"
                    left_spaces = left_spaces[:-1]
                    output_stars = stars

                    if i >= 3:

                        output_stars = stars[:3] + middle_spaces + stars[-3:]
                        middle_spaces += "  "
                    
                else:
                    stars = stars[:-2]
                    left_spaces = left_spaces + " "

                    if i == num_lines:
                            
                        middle_spaces = middle_spaces[:-4]
                        output_stars = stars[:3] + middle_spaces + stars[-3:]

                    elif i > num_lines and i < (num_lines * 2) - 4:
                        
                        middle_spaces = middle_spaces[:-2]
                        output_stars = stars[:3] + middle_spaces + stars[-3:]   

                    else:
                        output_stars = stars
                            
                output_lines = left_spaces + output_stars
                print (output_lines)
            break

        else:   
            print("sorry cannot print the desired output in less than 5 lines. Please choose 5 or above")

    except ValueError:
        print ("Is that a number? Please enter the valid input")