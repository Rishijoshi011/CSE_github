import numpy as np

# ! Linear search (Commented out for now)

size = int(input("Enter size of an Array: "))
arr = np.array([int(input()) for _ in range(size)])

x = int(input("Enter element to find: "))
flag = False
for i in range(size):
    if(arr[i] == x):
        print(x, ":found at location", i)
        flag = True
        
if(flag == False):
    print("Element not found")

# ! Binary search
arr.sort()  

x = int(input("Enter element to find: "))
low = 0
high = size - 1
flag = False

while(low <= high):  
    mid = (low + high) // 2
    if arr[mid] == x:
        print(x, ": found at location", mid)
        flag = True
        break
    elif arr[mid] > x:
        high = mid - 1  
    else:
        low = mid + 1 
        
if not flag:
    print("Element not found")
