import pytesseract
from PIL import Image
import cv2
import numpy as np

def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Cannot read image at {image_path}")
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    processed = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    text = pytesseract.image_to_string(processed)
    return text.strip()
