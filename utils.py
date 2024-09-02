from PIL import Image
import os
import pytesseract



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
                with Image.open(image_path) as img:
                    text = pytesseract.image_to_string(img).strip()
                    timestamps[filename] = text
                    file.write(f"{filename}: {text}\n")
                    print(f"Extracted timestamp from {filename}: {text}")
    
    return timestamps
    # os.makedirs(output_text_folder, exist_ok=True)
    # current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    # output_file_path = os.path.join(output_folder, f"timestamps_{current_time}.txt")

    # timestamps = {}
    
    # with open(output_file_path, 'w') as file:
    #     for filename in os.listdir(output_folder):
    #         if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
    #             image_path = os.path.join(output_file_path)
    #             with Image.open(image_path) as img:
    #                 text = pytesseract.image_to_string(img).strip()
    #                 timestamps[filename] = text
    #                 file.write(f"{filename}: {text}\n")
    #                 print(f"Extracted timestamp from {filename}: {text}")
    
    # return timestamps

    # for filename in os.listdir(output_folder):
    #     if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
    #         image_path = os.path.join(output_folder, filename)
            
    #         # Open the cropped image
    #         with Image.open(image_path) as img:
    #             # Use pytesseract to extract text from the image
    #             text = pytesseract.image_to_string(img)
                
    #             # Store the extracted timestamp with the corresponding filename
    #             timestamps[filename] = text.strip()
                
    #             print(f"Extracted timestamp from {filename}: {text.strip()}")
    
    # return timestamps
