# Approach 1- using reg
import re

str = "welcome@@2To%%Python**Programming@!#$*&^"

regex = re.compile('[@!#$%^&*()_+~]')

if (regex.search(str) == None): # regex return None if match is not found by default.
    print("No special char in string")
else:
    print("str contain special character")