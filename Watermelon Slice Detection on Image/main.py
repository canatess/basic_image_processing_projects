"""
@Project_Description:
    Detect watermelon slice contour, then fill the contour with red
    colour after extract watermelon from image.

@Author:
    Can Ali Ates
"""

# Import Libraries.
import os
import cv2
import numpy

# Read Image.
image = cv2.imread('Media/Watermelon.jpg')

# Convert Image to GrayScale.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Threshold to GrayScaled Image.
ret, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Create 9x9 Kernel.
kernel = numpy.ones((9, 9), numpy.uint8)

# Create Morphological Mask.
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# Copy Image to Extract Watermelon.
result = image.copy()

# Convert Copied Image to BGR-A Format.
result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)

# Apply Mask to Alpha Channel of Image.
result[:, :, 3] = mask

# Create Directory to Save Outputs of Detector.
if not os.path.isdir("Output"):
    os.mkdir("Output")

# Save Watermelon Slice as Image.
cv2.imwrite("Output/Watermelon_Slice.png", result)

# Create Edge on GrayScaled Image.
edged = cv2.Canny(gray, 30, 200)

# Find Contours.
contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Fill Contour with Red Color.
cv2.drawContours(image, contours, -1, (0, 0, 255), -1)

# Save Coloured Contour of Original Image.
cv2.imwrite('Output/Coloured_Contour.jpg', image)

# Close All Windows.
cv2.waitKey(0)
cv2.destroyAllWindows()
