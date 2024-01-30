# This program is to ask the user to enter numbers continuously
#  and find the average of them until the user enters -1.

sum = 0
count = 0
num = float(input("Please enter a number :   "))

while num != -1:
    sum += num
    count += 1
    num = float(input("Please enter a number :   "))

avg = round(sum / count, 2)
print(f"The average of your numbers is {avg}")