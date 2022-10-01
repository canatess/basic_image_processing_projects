"""
@Project_Description:
    Assign random pixel values while iterating over original
    pixel values, this implementation creates static noise
    on image.

@Author:
    Can Ali Ates
"""

# Import Libraries.
import os
import cv2
import random

# Read Image.
image = cv2.imread("Media/Towers.jpg")

# Show Original Image Before Apply Static Noise.
cv2.namedWindow("Original Image", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Original Image", image)

# Assign Random Pixel Values to Original Pixels.
for i in range(0, image.shape[0]):
    for j in range(0, image.shape[1]):
        image[i][j] = random.randint(0, 255)

# Show Prickled Image After Apply Static Noise.
cv2.namedWindow("Prickled Image", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Prickled Image", image)

# Create an Output Folder if Not Exist.
if not os.path.isdir("Output"):
    os.mkdir("Output")

# Save Result to Output Folder.
cv2.imwrite("Output/Static_Noised_Towers.jpg", image)

# Close All Windows.
cv2.waitKey(0)
cv2.destroyAllWindows()
