# using for loop with range()
mylist = [4,8,98,3,7]

total = 0

for i in range(0,len(mylist)):
    total = total + mylist[i]

print("sume of all  elements in a given list" , total)

# using sum() method
total = sum(mylist)
print("sum of all  elements in a given list" , total)