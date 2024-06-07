# Extracting-data-in-an-images-with-the-help-of-OCR
This project demonstrates a pipeline for processing images and extracting text using OpenCV and Tesseract OCR. The main functionalities include:
Otsu's Thresholding: Converts images to grayscale and applies Otsu's thresholding to binarize the image.
Image Denoising: Reduces noise using Non-Local Means Denoising to enhance text extraction quality.
Text Extraction: Utilizes Tesseract OCR to extract text from the processed images.
Information Extraction: Extracts specific information such as names, dates, and other details using regular expressions.
Output: Saves the extracted information in JSON format.
**Prerequisites:**
OpenCV
Tesseract OCR
PIL (Python Imaging Library)
Python 3.x
