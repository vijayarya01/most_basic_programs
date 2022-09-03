str = " Welcome to python programming"

words = str.split(" ") # split by space
print(words)

words = words[-1::-1]
print(words)

output_str = " ".join(words)
print(output_str)