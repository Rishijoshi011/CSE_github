
# ! Lab-1 Basic Python programs.[ NumPy, Panda, Matplotlib]

# * 1 creating blank array with predefined data

import numpy as np

arr = np.array([551, 285, 234, 206, 206, 205, 200, 175, 97, 74])
print("Question 1: ", arr)

# * 2 slicing and updating elements

print("Question 2: ", arr[0]) # accessing the first element
print("Question 2: ", arr[9]) # accessing the last element
print("Question 2: ", arr[3:7]) # accessing through the 3 to 6 element

arr = np.append("Question 2: ", arr, [62, 58]) # adding 62 and 58 numbers
arr = np.delete("Question 2: ", arr, 3) # deleting element by index
arr = np.delete("Question 2: ", arr, 4) # deleting element by index
arr = np.where("Question 2: ", arr == 58, 57, arr)
print("Question 2: ", arr)

# * 3 reshape array

arr = arr.reshape(5, 2)
print(arr)

# * 4 looping in numpy

for i in np.nditer(arr):
    print(i, end = " ")

# * 5 read csv file in numpy

import kagglehub
import os
import numpy as np

# Step 1: Download the dataset from Kaggle
path = kagglehub.dataset_download("tamber/steam-video-games")

# Print the path to the downloaded dataset
print("Path to dataset files:", path)

# Step 2: Check the downloaded files
dataset_dir = os.path.join(path, 'versions', '3')  # Check within version '3' or similar subdirectory
files = os.listdir(dataset_dir)
print("Files in the dataset directory:", files)

# Assuming the file is named 'steam_games.csv' or use the correct file name
csv_file_path = os.path.join(dataset_dir, 'steam_games.csv')  # Update with the correct file name if needed

# Step 3: Read the CSV file using NumPy
arr = np.genfromtxt(csv_file_path, delimiter=',', dtype=None, names=True, encoding='utf-8')

# Display the data
print("Data from the CSV file using NumPy:")
print(arr)
