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

# def extract_timestamp(image_path):

# # Open the image

# img = Image.open(image_path)

# # (Optional) Preprocess the image: Convert to grayscale and crop

# img = img.convert('L') # Convert to grayscale

# # You may need to crop the image to the area where the timestamp is

# # img = img.crop((left, top, right, bottom))

# # Perform OCR to extract the text

# text = pytesseract.image_to_string(img)

# # Clean up the extracted text

# text = text.strip()

# return text

# # Path to the folder containing screenshots

# folder_path = 'pics'

# timestamps = []

# # Loop through all files in the folder

# for filename in os.listdir(folder_path):

# if filename.endswith(".png") or filename.endswith(".jpg"):

# image_path = os.path.join(folder_path, filename)

# timestamp = extract_timestamp(image_path)

# timestamps.append(timestamp)

# # Print all extracted timestamps

# for timestamp in timestamps:

# print(timestamp)
