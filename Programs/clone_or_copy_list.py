# Approach 1 -using slicing technique

mylist = [4,8,12,3,9]

mylist_copy = mylist[:]
print(mylist_copy)

# Approach 2 - using extend() method

mylist_copy = []
mylist_copy.extend(mylist)
print(mylist_copy)

# Using the list() method
mylist_copy = list(mylist)
print(mylist_copy)

# using copy method
mylist_copy = mylist.copy()
print(mylist_copy)

# using list comprehension

mylist_copy =[i for i in mylist]
print(mylist_copy)