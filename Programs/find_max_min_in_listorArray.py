arr = [10,2,30,4,5]

#finding the maximum element
max= arr[0]
n = len(arr)

for i in range(1,n):
    if arr[i]> max:
        max = arr[i]

print(max)

# finding the minimum element
arr_min = [30,32,9,87,3]
min = arr[0]
n = len(arr_min)

for i in range(1,n):
    if arr_min[i] < min:
        min = arr_min[i]
print(min)