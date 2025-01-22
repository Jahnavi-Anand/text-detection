import pytesseract
from PIL import Image

# Make sure the Tesseract executable is accessible
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'  # Update the path as needed

# Test OCR on an image
image = Image.open('example.png')  # Replace with your image file
text = pytesseract.image_to_string(image)
print(text)
