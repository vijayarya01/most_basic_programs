
# using traversal
mylist= [3,2,4]

result = 1

for x in mylist:
    result = result * x  # 24

print(result)

# using numpy.prod()  -- install numpy package
import numpy
print(numpy.prod(mylist))

