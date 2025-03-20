import os
from PIL import Image
from prac_2_gen_csv import data

desired_size = (128, 128)
def resize_image(image_path, output_path, desired_size):
    with Image.open(image_path) as img:
        resized_img = img.resize(desired_size)
        resized_img.save(output_path)

os.makedirs('resized_images', exist_ok = True)
    
for idx, row in data.iterrows():
    image_path = row['image_path']
    label = row['labels']
    output_path = f"resized_images/{os.path.basename(image_path)}"
    resize_image(image_path, output_path, desired_size)
    print (f"Resized {image_path} and saved to {output_path}")