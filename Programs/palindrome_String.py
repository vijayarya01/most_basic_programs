# Approach 1  -- First check ... find reverse of string , check if reverse and orignal are same or not

s = input("enter a string")

print(s[:]) # same output # abcde
print(s[0:5]) # same output # abcde
print(s[0:5:1]) # same output # abcde
print(s[::]) # same output

reverse_str = (s[::-1]) # reverse edcba

if reverse_str == s:
    print("Palindrome")
else:
    print("Not Palindrome")