#The most important factor because of which most of the computer vision tasks fail is Noise
#OpenCV provides a function called fastNIMeansDenoising() that smoothens the images in order to reduce the image noise.
#what i did is taking the output of the binarization output as input here so that it will remove the noise in that image
#Enhancednoise reduction
import cv2
import matplotlib.pyplot as plt

# Read the binary thresholded image
img = cv2.imread('binary_otsu_thresholded.png', cv2.IMREAD_GRAYSCALE)  # Ensure it is read in grayscale

# Apply image denoising
dst = cv2.fastNlMeansDenoising(img, None, 10, 7, 21)  # Adjust parameters as needed

# Plot original and denoised image
titles = ["Original Image", "Denoised Image"]
images = [img, dst]

plt.figure(figsize=(10, 5))  # Adjusted for better visualization

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(images[i], 'gray', vmin=0, vmax=255)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()  # Show the plot

# Save only the denoised image
output_dir = r'C:\Users\K NIKHIL RAJ\OneDrive\Desktop\jsonformatextract'  # Specify the directory
output_filename = 'denoised_image.png'
output_path = f"{output_dir}/{output_filename}"

# Ensure the output directory exists
if not cv2.os.path.exists(output_dir):
    cv2.os.makedirs(output_dir)

cv2.imwrite(output_path, dst)  # Save the denoised image
print(f"Denoised image saved as {output_path}")
