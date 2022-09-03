
# using list in ascending order and print first and last elements in list
mylist = [34,5,89,65]

mylist.sort()
print(mylist)

print("smallest element", mylist[0])
print("largest element",mylist[-1])

# using min and max() methods

print("smallest element", min(mylist))
print("largest element",max(mylist))