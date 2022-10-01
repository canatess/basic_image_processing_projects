"""
@Project_Description:
    Apply threshold to image for detect the specified object.

@Author:
    Can Ali Ates
"""

# Import Libraries.
import os
import cv2

# Read Images as GrayScale.
moon = cv2.imread("Media/Moon.jpg", 0)
ball = cv2.imread("Media/Ball.jpg", 0)

# Blur Images to Determine Specified Objects.
moon_median = cv2.medianBlur(moon, 45)
ball_median = cv2.medianBlur(ball, 49)

# Apply Multiple Blurring to Determine Tennis Ball Clearly.
for i in range(45):
    ball_median = cv2.medianBlur(ball_median, 49)

# Apply Threshold to Put Color Values Into 0 to 1 Range.
_, moon_threshold = cv2.threshold(moon_median, 30, 255, cv2.THRESH_BINARY)
_, ball_threshold = cv2.threshold(ball_median, 65, 255, cv2.THRESH_BINARY)

# Show Threshold Images.
cv2.imshow("Moon", moon_threshold)
cv2.imshow("Ball", ball_threshold)

# Create Directory to Save Threshold Images.
if not os.path.isdir("Output"):
    os.mkdir("Output")

# Save Threshold Images.
cv2.imwrite("Output/Moon_Threshold.jpg", moon_threshold)
cv2.imwrite("Output/Ball_Threshold.jpg", ball_threshold)

# Close All Windows.
cv2.waitKey(0)
cv2.destroyAllWindows()
