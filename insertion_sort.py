import numpy as np

arr = [5,3,8,7,1]
#arr = np.random.randint(0,1000,10) #Uncommment this line to generate an array of random integers

print('arr before sorting:', arr)

#====================================================
#Write your insertion sort here

for i in range(0, len(arr)):
    if i > 0:
        if arr[i] < arr[i-1]:
            val = arr[i-1]
            del arr[i-1]
            arr.insert(i+1, val)


#====================================================

print('arr after sorting:', arr)