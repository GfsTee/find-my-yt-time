from PIL import Image
import os
import pytesseract
import cv2
import numpy as np

def crop_and_save_images(input_folder, output_folder, crop_box_percent):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_folder, filename)
            
            # Open the image
            with Image.open(image_path) as img:
                width, height = img.size
                
                # Convert percentage crop box to pixel values
                left_percent, top_percent, right_percent, bottom_percent = crop_box_percent
                left = int(left_percent * width)
                top = int(top_percent * height)
                right = int(right_percent * width)
                bottom = int(bottom_percent * height)
                
                # Crop the image
                cropped_img = img.crop((left, top, right, bottom))
                
                # Save the cropped image to the output folder
                output_path = os.path.join(output_folder, filename)
                cropped_img.save(output_path)
                
                print(f"Saved cropped image: {output_path}")

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_timestamps(output_folder, output_file):
    timestamps = {}
    
    with open(output_file, 'w') as file:
        for filename in os.listdir(output_folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(output_folder, filename)
                
                # Preprocess the image before extracting text
                # processed_img = preprocess_image(image_path)
                
                # Extract text using pytesseract
                # text = pytesseract.image_to_string(processed_img).strip()
                text = pytesseract.image_to_string(image_path).strip()
                timestamps[filename] = text
                file.write(f"{filename}: {text}\n")
                print(f"Extracted timestamp from {filename}: {text}")
    
    return timestamps


output_folder = 'timestamps'


def preprocess_image(image_path):
    # Read the image using OpenCV
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    img = cv2.equalizeHist(img)

    # Optionally, apply sharpening using a kernel
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    img = cv2.filter2D(img, -1, kernel)

    # debug start
    # Extract filename and extension from the original image path
    filename = os.path.basename(image_path)
    filename_no_ext, file_extension = os.path.splitext(filename)
    
    # Create the new filename with _gs appended before the extension
    grayscale_save_path = os.path.join(output_folder, f"{filename_no_ext}_gs{file_extension}")
    
    # Save the grayscale image
    cv2.imwrite(grayscale_save_path, img)

    # debug end


    # Apply adaptive thresholding to improve text detection
    processed_img = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    
    # Convert processed image back to PIL format
    return Image.fromarray(processed_img)