import numpy as np

arr = [5,3,8,7,1]
arr = np.random.randint(0,1000,10) #Uncommment this line to generate an array of random integers

print('arr before sorting:', arr)

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

print('arr after sorting:', arr)