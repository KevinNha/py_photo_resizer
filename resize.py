from PIL import Image
import os

BASE_WIDTH = 300 # This will calculate the height of resized image
INPUT_IMAGE_PATH = "Documents/photos" # Change this to the image path you want
OUTPUT_IMAGE_PATH = "Documents/resized_photos" # Change this to the image path you want

def lower_resolution(input_image_path, output_image_path):
    with Image.open(input_image_path) as img:
        w_percent = (BASE_WIDTH / float(img.size[0]))
        h_size = int((float(img.size[1]) * float(w_percent)))

        img = img.resize((BASE_WIDTH, h_size), Image.Resampling.LANCZOS)
        img.save(output_image_path)

def process_images(source_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(source_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            input_path = os.path.join(source_folder, filename)
            output_path = os.path.join(output_folder, filename)
            lower_resolution(input_path, output_path)

# Define the source and output folders
source_folder = os.path.join(os.path.expanduser('~'), INPUT_IMAGE_PATH)
output_folder = os.path.join(os.path.expanduser('~'), OUTPUT_IMAGE_PATH)

# Process the images
process_images(source_folder, output_folder)
