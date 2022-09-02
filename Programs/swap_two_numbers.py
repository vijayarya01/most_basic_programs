num1 = input("Enter your first number")
num2 = input("Enter your second number")

print("Value of num1 before swapping:",num1)
print("Value of num2 before swapping:",num2)

# approach 1
temp = num1 # first number is assigned to temp

num1 = num2 # original num2 value is now num1
num2 = temp # assigned num1 value to temp will be in num2 now.

print("Value of num1 after swapping:",num1)
print("Value of num2 after swapping:",num2)
'''

# approach 2 - without using third variable .

num1,num2 = num2,num1

print("Value of num1 after swapping:",num1)
print("Value of num2 after swapping:",num2)
'''

