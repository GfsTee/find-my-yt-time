from PIL import Image
import cv2
import os
from utils import extract_timestamps, crop_and_save_images
from datetime import datetime


# Path to the Tesseract executable



input_folder = 'pics'
output_folder = 'timestamps'
output_text_folder = 'save' 

# Define the crop box as percentages (left, top, right, bottom)
crop_box_percent = (0.0, 0.72, 0.3, 0.8)  # Adjust based on your timestamp location

crop_and_save_images(input_folder, output_folder, crop_box_percent)

# extract_timestamps(output_folder, output_text_folder)

current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = os.path.join(output_folder, f"timestamps_{current_time}.txt")

timestamps = extract_timestamps(output_folder, output_file)


# def extract_timestamp(image_path):
#     # Open the image
#     img = Image.open(image_path)
    
#     # (Optional) Preprocess the image: Convert to grayscale and crop
#     img = img.convert('L')  # Convert to grayscale
    
#     # You may need to crop the image to the area where the timestamp is
#     # img = img.crop((left, top, right, bottom))
    
#     # Perform OCR to extract the text
#     text = pytesseract.image_to_string(img)
    
#     # Clean up the extracted text
#     text = text.strip()
    
#     return text

# # Path to the folder containing screenshots
# folder_path = 'pics'
# timestamps = []

# # Loop through all files in the folder
# for filename in os.listdir(folder_path):
#     if filename.endswith(".png") or filename.endswith(".jpg"):
#         image_path = os.path.join(folder_path, filename)
#         timestamp = extract_timestamp(image_path)
#         timestamps.append(timestamp)

# # Print all extracted timestamps
# for timestamp in timestamps:
#     print(timestamp)
