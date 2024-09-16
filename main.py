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
crop_box_percent = (0.05, 0.75, 0.15, 0.79)  # Adjust based on your timestamp location

crop_and_save_images(input_folder, output_folder, crop_box_percent)

# extract_timestamps(output_folder, output_text_folder)

current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = os.path.join(output_folder, f"timestamps_{current_time}.txt")

timestamps = extract_timestamps(output_folder, output_file)
