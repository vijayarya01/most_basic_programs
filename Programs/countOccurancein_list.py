# approach 1 - using loop

mylist= [15,6,30,4,7,12,7,4,7]
x= 7
count = 0

for elem in mylist:
    if(elem ==x):
        count = count +1
print("{} has {} times".format(x,count))

# Approach 2 - Using the count method

x = 4
print("{} has {} times".format(x,mylist.count(x)))

# Approach 3 - Using counter()
from collections import Counter
x= 7
dict = Counter(mylist)
print(dict)