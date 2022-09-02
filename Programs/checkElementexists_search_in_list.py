# Approach 1 - using loops

mylist = [4,5,9,2]
ele = 4

flag = 0

for i in mylist:
    if(i == ele):
        print("Element found")
        flag = 1
        break
if(flag ==0):
    print("Element not found")


# Using in operator
if (ele in mylist):
    print("element found")
else:
    print("element not found")