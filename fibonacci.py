# This programme is intended to print fibonacci sequence
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Please enter how many values of the fibonacci series to be printed :    "))   
for i in range(0,num):
    print(fibonacci(i))
