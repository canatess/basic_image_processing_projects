"""
@Project_Description:
    Create Screw Datasets And Extract Features From These
    Datasets For Different Convolutional Networks After Save
    The Cropped Detected Screws From Original Image.

@Author:
    Can Ali Ates
"""

# Import Libraries
import os
import cv2
import numpy
from PIL import Image

# Read Image as PIL Object to Crop Easily.
image = Image.open("Media/Screw.jpeg")

# Read Image as OpenCV Object.
img = cv2.imread("Media/Screw.jpeg", cv2.IMREAD_COLOR)

# Convert OpenCV Image to GrayScale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur The GrayScaled Image With 13x13 Kernel.
gray_blurred = cv2.medianBlur(gray, 13)

# Apply HoughCircles Transform to Blurred Image.
detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=1, maxRadius=40)

if not os.path.isdir("Output"):
    os.mkdir("Output")

# Check The Existence of Detected Circles.
if detected_circles is not None:

    # Create Directory to Save Screws Separately.
    if not os.path.isdir("Output/Screws"):
        os.mkdir("Output/Screws")

    # Convert to Circle Parameters to Center Coordinates And Radius as Integer.
    detected_circles = numpy.uint16(numpy.around(detected_circles))

    # Take All Detected Circles Information One by One.
    for count, points in enumerate(detected_circles[0, :]):

        # Separate Center And Radius Coordinates.
        x, y, r = points[0], points[1], points[2]

        # Draw Circle Around The Screws.
        cv2.circle(img, (x, y), r, (0, 0, 255), 5)

        # Calculates Borders From Circle's Information to Crop as Rectangle.
        x1, x2, y1, y2 = x - r - 10, x + r + 10, y - r - 10, y + r + 10

        # Crop Image as Rectangle.
        cropped_image = image.crop((x1, y1, x2, y2))

        # Save Cropped Screws to Screws Folder.
        cropped_image.save(f"Output/Screws/Screw_{count}.jpg")

# Save Image of Detected Screws on Original Image.
cv2.imwrite("Output/Detected Screws.jpg", img)

# Create Dataset Folder to Save All Datasets.
if not os.path.isdir("Output/Datasets"):
    os.mkdir("Output/Datasets")

# Iterate Over Backgrounds.
for background in os.listdir("Media/Default Backgrounds"):

    # Ask User to Conversion to GrayScale.
    print(f"\nBackground Shape: {background[11:14]} x {background[11:14]}")
    gray_scale = input("Convert Output to GrayScale (Y|N): ")

    # Determine Dataset Path.
    dataset_path = f"Output/Datasets/{background[11:14]}_Dataset"

    # Read Background.
    background_image = cv2.imread(f"Media/Default Backgrounds/{background}")

    # Check Existence Of Dataset Path.
    if not os.path.isdir(dataset_path):
        os.mkdir(dataset_path)

    # Iterate Over Cropped Screws.
    for count, filename in enumerate(os.listdir("Output/Screws")):

        # Check the JPG File.
        if filename.endswith(".jpg"):

            # Copy Background to Paste Screw.
            copy_background = background_image.copy()

            # Read Screw Image.
            screw = cv2.imread(f"Output/Screws/{filename}")

            # Separate Screw Shape Information.
            height, width, channel = screw.shape

            # Calculate X and Y Range to Center Image.
            y = int((background_image.shape[0] - height) / 2)
            x = int((background_image.shape[1] - width) / 2)

            # Create a Roi from Original Background.
            roi = background_image[y: y + height, x: x + width]

            # Convert Screw Image to GrayScale.
            gray_screw = cv2.cvtColor(screw, cv2.COLOR_BGR2GRAY)

            # Apply Threshold to GrayScaled Image For Create Mask.
            ret, mask = cv2.threshold(gray_screw, 10, 255, cv2.THRESH_BINARY)

            # Take Inverted Mask.
            mask_inv = cv2.bitwise_not(mask)

            # Take Black-Out Area of Background.
            img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)

            # Take Region of Foreground.
            img2_fg = cv2.bitwise_and(screw, screw, mask = mask)

            # Put Screw in ROI.
            dst = cv2.add(img1_bg, img2_fg)

            # Modify the Background.
            copy_background[y: y + height, x: x + width] = dst

            # Check GrayScale Situation of Output.
            if gray_scale == "Y" or gray_scale == "y":
                copy_background = cv2.cvtColor(copy_background, cv2.COLOR_BGR2GRAY)

            # Save the Data Into Screw Dataset Folder.
            cv2.imwrite(f"{dataset_path}/data_{count}.jpg", copy_background)

# Check Existence of Features Folder.
if not os.path.isdir("Output/Features"):
    os.mkdir("Output/Features")

# Iterate Over Dataset Folder.
for dataset in os.listdir("Output/Datasets"):

    # Check Existence of Feature File.
    if not os.path.isdir(f"Output/Features/{dataset[0:3]}_Features"):
        os.mkdir(f"Output/Features/{dataset[0:3]}_Features")

    # Determine Feature File Path.
    feature_path = f"Output/Features/{dataset[0:3]}_Features"

    # Iterate Over Dataset.
    for count, data in enumerate(os.listdir(f"Output/Datasets/{dataset}")):

        # Read Data.
        screw = cv2.imread(f"Output/Datasets/{dataset}/{data}")

        # Determine Center of Image.
        half_y = int(screw.shape[0] / 2)
        half_x = int(screw.shape[1] / 2)

        # Cut The Image Into 4 Piece.
        upper_left = screw[0:half_y, 0:half_x]
        upper_right = screw[0:half_y, half_x:]
        lower_left = screw[half_y:, 0:half_x]
        lower_right = screw[half_y:, half_x:]

        # Save Features.
        cv2.imwrite(f"{feature_path}/upper_left {count}.jpg", upper_left)
        cv2.imwrite(f"{feature_path}/upper_right {count}.jpg", upper_right)
        cv2.imwrite(f"{feature_path}/lower_left {count}.jpg", lower_left)
        cv2.imwrite(f"{feature_path}/lower_right {count}.jpg", lower_right)

# Close All Windows.
cv2.waitKey(0)
cv2.destroyAllWindows()
