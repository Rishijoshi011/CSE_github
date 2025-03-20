import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import random as rand
data = pd.read_csv("data.csv")

# ! Print the first few rows of the data
# print(data.head())

# ! Getting the random image  
last = data.iloc[-1]
random_number = rand.randint(0, last.name)
first_img_path = data.loc[random_number, 'image_path']
label = data.loc[random_number, 'labels']

# # ! opeing and showing the image 
image = Image.open(first_img_path)
plt.imshow(image)
plt.title(f"Label: {label}")
plt.axis('off')
plt.show()  # Display the image
