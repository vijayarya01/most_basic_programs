# Approach 1  - clear method
mylist = [4,5,2,3,9]

print("my list before clear",mylist)

mylist.clear()
print("my list after clear",mylist)

# approach 2 : initialize th list with no values
mylist = [4,5,2,3,9]

print("my list before clear",mylist)

mylist = []
print("my list after clear",mylist)

# Approach 3 - Using *=0 this method removes all elements of the list and makes it emplty
mylist = [4,5,2,3,9]

print("my list before clear",mylist)

mylist *=0 # deletes list
print("my list after clear",mylist)

# Approach 4 - Using del
mylist = [4,5,2,3,9]

print("my list before clear",mylist)

del mylist[:] # 0
print("my list after clear",mylist)