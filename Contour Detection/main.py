"""
@Project_Description:
    Detect contours of specified objects on images.

@Author:
    Can Ali Ates
"""

# Import Libraries.
import os
import cv2

# Read Images.
ellipse_image = cv2.imread("Media/Ellipses.png")

# Convert Images to Gray Scale.
ellipse_gray = cv2.cvtColor(ellipse_image, cv2.COLOR_BGR2GRAY)

# Find Edges on Images.
ellipse_edged = cv2.Canny(ellipse_gray, 30, 200)

# Detect Contours on Edges.
ellipse_contours = cv2.findContours(ellipse_edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]

# Create a Directory to Save Detection Results.
if not os.path.isdir("Output"):
    os.mkdir("Output")

# Iterate Over Ellipse Image to Detect Ellipses Separately.
for count, contour in enumerate(ellipse_contours):

    # Store Information of Contour.
    x, y, w, h = cv2.boundingRect(contour)

    # Crop Ellipse According to Contour Information.
    crop_image = ellipse_image[(y-5):(y+h+5), (x-5):(x+w+5)]

    # Save Cropped Ellipse.
    cv2.imwrite(f'Output/Ellipse_{count + 1}.jpg', crop_image)

# Draw Contours on Original Images.
cv2.drawContours(ellipse_image, ellipse_contours, -1, (0, 0, 255), 7)

# Show Contoured Images.
cv2.imshow('Ellipse Contours', ellipse_image)

# Save Original Images with Draw Contours.
cv2.imwrite("Output/Detected_Ellipses.jpg", ellipse_image)

# Close All Windows.
cv2.waitKey(0)
cv2.destroyAllWindows()
