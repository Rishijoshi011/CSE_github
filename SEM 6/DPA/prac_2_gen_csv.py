import os
import pandas as pd
dataset_path = 'C:/personal_documents/CSE/CSE_github/SEM 6/DPA/archive/caltech-101'

images_path = []
labels = []

for category in os.listdir(dataset_path):
    category_path = os.path.join(dataset_path, category)
    if os.path.isdir(category_path):    
        for image_name in os.listdir(category_path):
            if image_name.endswith(".jpg"):
                images_path.append(os.path.join(category_path,image_name))
                labels. append (category)

data = pd.DataFrame({
    'image_path' : images_path,
    'labels' : labels
})

data.to_csv('data.csv', index = False)