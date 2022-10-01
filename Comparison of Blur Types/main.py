"""
@Project_Description:
    Observe difference between blur types on same image.

@Author:
    Can Ali Ates
"""

# Import Libraries.
import os
import cv2

# Read and Reshape Image.
image = cv2.imread("Media/Rocket.jpg")
image = cv2.resize(image, (480, 640))

# Create 3 Window to Display Blur Types.
cv2.namedWindow("Blur", cv2.WINDOW_AUTOSIZE)
cv2.moveWindow("Blur", 100, 100)

cv2.namedWindow("Median Blur", cv2.WINDOW_AUTOSIZE)
cv2.moveWindow("Median Blur", 600, 100)

cv2.namedWindow("Gaussian Blur", cv2.WINDOW_AUTOSIZE)
cv2.moveWindow("Gaussian Blur", 1100, 100)

# Blur the Image.
blur = cv2.blur(image, (15, 15))
median_blur = cv2.medianBlur(image, 15)
gaussian_blur = cv2.GaussianBlur(image, (15,15), 0)

# Open Images in Related Windows.
cv2.imshow("Blur", blur)
cv2.imshow("Median Blur", median_blur)
cv2.imshow("Gaussian Blur", gaussian_blur)

# Create A Directory to Save Blurred Images.
if not os.path.isdir("Output"):
    os.mkdir("Output")

# Save Blurred Images.
cv2.imwrite("Output/Blur.jpg", blur)
cv2.imwrite("Output/MedianBlur.jpg", median_blur)
cv2.imwrite("Output/GaussianBlur.jpg", gaussian_blur)

# Close All Windows.
cv2.waitKey(0)
cv2.destroyAllWindows()
