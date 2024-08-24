import numpy as np
import matplotlib.pyplot as plt

# ! A
# TODO: Extracting odd numbers

list_ = np.array([11, 12, 13, 14, 15])
index = np.where(list_ % 2 != 0)[0]

for i in index:
    print(list_[i], end = " ")
    
# ! B
# TODO: replacing with -1

new_array = list_[::]
for i in index:
      new_array[i] = -1
      
print(f"\n{new_array}") 

# ! C
# TODO: convert 1D to 2D array with 2x5    
array_ = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

new_array2 = array_.reshape(2, 5)
for i in range(len(new_array2)):
    for j in range(len(new_array2[0])):
        print(f"{new_array2[i][j]}", end = " ")
    print()
    
# ! D
# TODO: common elements between two array

array_1 = np.array([1,2,3,2,3,4,3,4,5,6])
array_2 = np.array([7,2,10,2,7,4,9,4,9,8])

print(np.intersect1d(array_1, array_2))

# ! E
# TODO: matrix multiplication

array_3 = np.array([[1, 2], [3, 4]])
array_4 = np.array([[4, 3], [2, 1]])
result = np.dot(array_3, array_4)
print(result)

# ! F
# TODO: generate bar plots 

dataSet = [10, 20, 30, 40, 50]
dataSet2 = [20, 10, 12, 4, 24]

plt.bar(dataSet, dataSet2, color = "aqua", width = 1.0)

plt.ylabel("in Rs.1000s")
plt.xlabel("in 1000 units")
plt.title("temp")
plt.show()
