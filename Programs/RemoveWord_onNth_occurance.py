mylist = ["geeks","for","geeks"]
word = "geeks"
n = 2 # remove the element in 2nd occurance

count = 0

for i in range(1,len(mylist)):
    if (mylist[i]) == word:
        count = count+1
        if(count == n):
            del mylist[i]

print("updated list",mylist)
