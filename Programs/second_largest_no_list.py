
# Approach 1 - indexing
mylist = [10,34,2,44,5]
mylist.sort()
print(mylist)

print("Second largest number is ",mylist[-2])

# Approach 2 - using set
new_list = set (mylist)

new_list.remove(max(new_list)) # remove the largest element

print(new_list) # left with second largest

print(max(new_list))