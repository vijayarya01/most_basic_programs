str = "Welcome to python programming"

# The find() method finds the first occurance of the specified value
# the find() method return -1 if the value is not found

sub_str = "python"

print(str.find(sub_str)) # 11, gives position of the sting

if (str.find(sub_str) == -1):
    print("Not found")
else:
    print("Found the Substring in here")