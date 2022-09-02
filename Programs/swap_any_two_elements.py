#swap any two elements in a list based on their positions

# Approach -Simple swap
mylist = [23,65,19,90]
print(mylist)

#swap position 1 and 3 elements with each other
pos1 = 1
pos2  = 3

mylist[pos1],mylist[pos2] = mylist[pos2],mylist[pos1]

print("after swaping the list is" , mylist)

# approach 2 - using inbuilt -in pop function

pos1,pos2 = 1,3
first_element = mylist.pop(pos1)  # 65,it will delete element on pos1, then only 3 element will remain and index will reduce
second_element = mylist.pop(pos2-1) # 23,19,90

mylist.insert(pos1,second_element)
mylist.insert(pos2,first_element)
print("after swaping the list is" , mylist)

# approach 3 - using tuple

get = (pos1, pos2)

mylist[pos2],mylist[pos1] = get
print("after swaping the list is" , mylist)
