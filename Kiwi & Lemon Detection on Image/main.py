"""
@Project_Description:
    Detect kiwi and lemon while iterating over pixels with
    custom function, then apply threshold on detected objects.

@Author:
    Can Ali Ates
"""

# Import Libraries.
import os
import cv2


# Fruit Detection Function.
def fruit_finder(image, lower, upper, color="Blue"):

    # Control Workflow.
    x1_found, y1_found = False, False

    # Color Codes Arranged According to OpenCV BGR Format.
    if color == "Blue":
        color_code = 0
    elif color == "Green":
        color_code = 1
    else:
        color_code = 2

    # Find Object's X1 and X2 Position.
    for x in range(0, image.shape[1]):
        for y in range(0, image.shape[0]):
            if lower < image[y, x, color_code] < upper:
                if x1_found:
                    x2 = x
                else:
                    x1 = x
                    x1_found = True

    # Find Object's Y1 and Y2 Position.
    for y in range(0, image.shape[0]):
        for x in range(0, image.shape[1]):
            if lower < image[y, x, color_code] < upper:
                if y1_found:
                    y2 = y
                else:
                    y1 = y
                    y1_found = True

    # Return Borders of Object.
    return x1, x2, y1, y2


# Read Kiwi Image.
kiwi = cv2.imread("Media/Kiwi.jpg")

# Determine Borders of Kiwi Object.
x1, x2, y1, y2 = fruit_finder(kiwi, 120, 180, "Green")

# Draw Rectangle Around Kiwi Object.
cv2.rectangle(kiwi, (x1, y1), (x2, y2), (0, 0, 255), 3)

# Find ROI of Kiwi Object.
kiwi_roi = kiwi[y1:y2, x1:x2]

# Convert Object to GrayScale.
kiwi_gray = cv2.cvtColor(kiwi_roi, cv2.COLOR_BGR2GRAY)

# Apply Threshold to Kiwi Object.
_, kiwi_threshold = cv2.threshold(kiwi_gray, 200, 255, cv2.THRESH_BINARY_INV)

# Show Detected Kiwi Object.
cv2.imshow("Detected Kiwi", kiwi)

# Read Lemon Image.
lemon = cv2.imread("Media/Lemon.jpg")

# Determine Borders of Lemon Object.
x1, x2, y1, y2 = fruit_finder(lemon, 180, 255, "Red")

# Draw Rectangle Around Lemon Object.
cv2.rectangle(lemon, (x1, y1), (x2, y2), (0, 0, 255), 3)

# Find ROI of Lemon Object.
lemon_roi = lemon[y1:y2, x1:x2]

# Convert Lemon Object to GrayScale.
lemon_gray = cv2.cvtColor(lemon_roi, cv2.COLOR_BGR2GRAY)

# Apply Threshold to Lemon Object.
_, lemon_threshold = cv2.threshold(lemon_gray, 185, 255, cv2.THRESH_BINARY)

# Show Detected Lemon Object.
cv2.imshow("Detected Lemon", lemon)

# Create A Directory to Save Detector Results.
if not os.path.isdir("Output"):
    os.mkdir("Output")

# Save Detector Results.
cv2.imwrite("Output/Kiwi_Threshold.jpg", kiwi_threshold)
cv2.imwrite("Output/Kiwi_Detected.jpg", kiwi)

cv2.imwrite("Output/Lemon_Threshold.jpg", lemon_threshold)
cv2.imwrite("Output/Lemon_Detected.jpg", lemon)

# Close All Windows.
cv2.waitKey(0)
cv2.destroyAllWindows()
