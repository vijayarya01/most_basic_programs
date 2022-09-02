# Using temporary variable

mylist = [12,35,5,56,24]

size = len(mylist)
temp = mylist[0]
mylist[0] = mylist[size-1]
mylist[size-1] = temp

print("list after swapping",mylist)

# Appraoch 2
mylist[0],mylist[-1] = mylist[-1],mylist[0]
print("list after swapping",mylist)
# Approach 3, using tuple

get = (mylist[-1],mylist[0]) # packing

mylist[0],mylist[-1] = get
print("list after swapping",mylist)

# Approach 4 using *operand
start,*middle,end = mylist
# print(start)
# print(middle)
# print(end)

mylist=[end,*middle,start]
print("list after swapping",mylist)

# Approach 5 using pop()
first = mylist.pop(0)
last = mylist.pop(-1)

mylist.insert(0,last)
mylist.append(first)
print("list after swapping",mylist)
