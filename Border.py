from PIL import Image, ImageOps
import os

dpi = 300
border_size = int(1/8 * dpi)

# Define the directory containing the images
image_folder = r"MYFILEPATHHERE" # Add your own file path here 

# Create a directory to save the images with the border
output_folder = os.path.join(image_folder, "bordered2")
os.makedirs(output_folder, exist_ok=True)

# Iterate over all files in the image folder
for filename in os.listdir(image_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):  # Adjust extensions as needed
        # Open an image file
        img_path = os.path.join(image_folder, filename)
        with Image.open(img_path) as img:
            # Add border
            bordered_img = ImageOps.expand(img, border=border_size, fill='black') # 1/8 inch border in pixels

            # Save the image with the border to the output folder
            output_path = os.path.join(output_folder, filename)
            bordered_img.save(output_path)

print("All images have been processed and saved with borders.")
