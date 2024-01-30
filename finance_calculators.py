#This programme is being written for a finance company 
#    to access two different types of financial calculators:
#    Investment calculator and Home loan repayment calculator

import math
print("------------------------------------------------------------------------------------")
print("  Investment - To calculate the amount of interest you'll earn on your investment")
print("  Bond       - To calculate the amount you'll have to pay on home loan")
print("------------------------------------------------------------------------------------")
print()
financial_calculator = input("Please enter either 'Investment' or 'Bond' from the menu above to proceed :    ")
financial_calculator = financial_calculator. upper()
print()
print()

#If the user selects "Investment":
#Request the user to input the amount they want to deposite, interest rate, 
#number of years they are planning to invest
#and also the type of interest they want to be generated.

if financial_calculator == "INVESTMENT": 
   
    deposit_money = float(input("Please enter the amount of money you are planning to deposit                   : £"))
    print ()
    interest_rate = float(input("Please enter the interest rate(enter the number only, not the '%'symbol)       : "))
    interest_rate = interest_rate / 100
    print ()
    number_of_years = int(input("Please enter the number of years you are planning on your investment           : "))
    print ()
    interest = input("Which type of interest do you want on your investment? Please enter 'simple' or 'compound': ")
    interest = interest. upper()
    print ()
    print ()

    #Calculate the total amount basing on the user's choice of interest type and print it out.
    #If it is simple use the formula: A = P(1 + r*t) 
    #where p -- principal amount, r -- interest rate % , t -- no.of years
    #If it is compound use the formula: A = P(1 + r)^t
    #where p -- principal amount, r -- interest rate % , t -- no. of months
    #If user's choice does not match the above print out a relevant statement.
   
    if interest == "SIMPLE" or interest == "COMPOUND":

        if interest == "SIMPLE":

            total_amount = round(deposit_money * (1 + interest_rate * number_of_years), 2)
        
        elif interest == "COMPOUND":

            total_amount = round(deposit_money * math.pow ((1 + interest_rate), number_of_years), 2)

        print(f"The amount to be deposited                              : £{deposit_money}")
        print()
        print(f"The interest rate                                       : {interest_rate * 100}%")
        print()
        print(f"The number of years                                     : {number_of_years}")
        print()
        print(f"The type of interest                                    : {interest}")
        print()
        print(f"The total amount to be received by the end of the period: £{total_amount}")
        print()
    
    else:
       
        print("Sorry, The interest type is not in our choice!")
        print()
    
#When the user's choice is "Bond":
#Request the user to enter present value of the house, interest rate
#and the number of months they are planning to repay the amount.
#Calculate the amount that needed to be paid in every month by the formula:
#repayment = (i*p)/(1-(1+i)^-n)
#where p -- present value of the house, i -- monthly interest(interest rate to be divided by 12),
#n -- no.of months

elif financial_calculator == "BOND":

    house_value = float(input("Please enter the present value of the house on which you want to take a loan          : £"))
    print ()
    interest_rate = float(input("Please enter the interest rate (Please enter the number only not '%' symbol)          : "))
    interest_rate = interest_rate / 100
    monthly_interest_rate = interest_rate / 12
    print ()
    number_of_months = int(input ("Please enter the number of months in which you are planning to repay the total amount : "))
    monthly_repayment = round((monthly_interest_rate * house_value) 
                               / (1 - (1 + monthly_interest_rate) ** (-number_of_months)), 2)
    print()
    print()
     
    print(f"The present value of the house                         : £{house_value}")
    print()
    print(f"The interest rate                                      : {interest_rate * 100}")
    print()
    print(f"The number of months being planned to repay the amount : {number_of_months}")
    print()
    print(f"The amount to be paid in every month                   : £{monthly_repayment}")
    print()

# If the user's choice does not match with any of the 'Investment' or 'Bond',
# print out a relevant statement.

else:

    print("Sorry, We cannot help you! Your selection is not in our menu.")
    print()