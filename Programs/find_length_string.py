# Approach 1 - using for loop

str = "welcome"
counter = 0
for i in str:
    counter = counter +1
print(counter)

# using while loop and slicing
counter = 0
while str[counter:]: # 0:6
    counter = counter+1
print(counter)

# using built in function len()
print(len(str))

# approach 4:: using join and count
random_str = "X"

print((random_str).join(str))  #wXeXlXcXoXmXe
print((random_str).join(str).count(random_str)) #  6
print((random_str).join(str).count(random_str)+1) # 7