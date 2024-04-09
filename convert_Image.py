import base64
from PIL import Image
from io import BytesIO
import os
import cv2

async def base64_to_image(base64_string, output_directory):
    # Decode the base64 string
    decoded_data = base64.b64decode(base64_string)
    
    # Open the image using PIL
    image = Image.open(BytesIO(decoded_data))
    
    # Save the image to the specified directory
    image_path = os.path.join(output_directory, "captured_image.jpg")  # Change the file extension as needed
    image.save(image_path)
    # img = cv2.imread("images/captured_image.jpg")
    # gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # cv2.imwrite("images/captured_image.jpg",gray_img)
    return image_path

# Example base64 string (replace this with your actual base64 encoded string)
# base64_string = "YOUR_BASE64_ENCODED_STRING_HERE"
# output_directory = "path/to/your/directory"

# # Convert base64 string to image and save it to the specified directory
# saved_image_path = base64_to_image(base64_string, output_directory)

# print("Image saved to:", saved_image_path)
