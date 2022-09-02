# using function to calculate factorial of any number
'''
def factorial(n):
    if (n==0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)  # 5*4*3*2*1

num = 5

#print(factorial(5))

# other way of printing it.
print("Factorial of ",num,"is", factorial(num))

# using ternary operator or appraoch

def factorial(n):
    return 1 if (n==1 or n== 0) else n*factorial(n-1)
'''
# Basic approach

factorial = 1
num = 5

if num < 0:
    print("There is no factorial of given number")
elif num == 0:
    print("The fActorial of 0 is 1 ")
else:
    for i in range(1, num +1):
        factorial = factorial * i
    print("The factorial of number is " , factorial)
