"""
@Project_Description:
    Distribute images according to image width after delete
    detected multiple copies of same image.

@Author:
    Can Ali Ates
"""

# Import Libraries.
import os
import cv2
import numpy

# Determine File Suffixes to Detect Images.
suffixes = (".jpg", ".jpeg", ".png")

# Create a List to Store Image Objects.
images = []

# Iterate Over Images File
for filename in os.listdir("Images"):

    # Detect Image Files.
    if filename.endswith(suffixes):
        # Read Image.
        image = cv2.imread(f"Images/{filename}")

        # Add Image File Name and Pixel Array to Images List.
        images.append([filename, image])

# Create a Set to Store Duplicate Images.
duplicate_images = set()

# Iterate Over Image Objects.
for i in range(len(images)):
    for j in range(i + 1, len(images)):

        # Check Image Shapes First to Boost Performance.
        if images[i][1].shape == images[j][1].shape:

            # Determine Center Pixels of Images.
            cY, cX = int(images[i][1].shape[0] / 2), int(images[i][1].shape[1] / 2)

            # Crop 10x10 Pixel Array From Center Of Images.
            image_1 = images[i][1][cY - 5: cY + 5, cX - 5: cX + 5]
            image_2 = images[j][1][cY - 5: cY + 5, cX - 5: cX + 5]

            # Compare ROI's of Images.
            if numpy.equal(image_1, image_2).all():
                duplicate_images.add(images[i][0])

# Delete Duplicate Images From Images.
for image in duplicate_images:
    os.remove(f"Images/{image}")


# Categorize Images According to Width.
def categorize_images(filename, file_path, image_path):
    name = f"{filename[:-4]}.jpg"
    source = f"{file_path}\Images\{filename}"
    destination = f"{image_path}\{name}"
    os.rename(source, destination)


# Create a Directory to Save Results.
if not os.path.isdir("Output"):
    os.mkdir("Output")

# Iterate Over Updated Images List.
for filename in os.listdir("Images"):

    # Detect Image Files.
    if filename.endswith(suffixes):

        # Find Shape of Image.
        image_shape = cv2.imread(f"Images/{filename}").shape[1]

        # Create an Image Path.
        image_path = f"Output/{image_shape}"

        # If Image Path Exists, Add Image to That Path.
        if os.path.isdir(image_path):
            categorize_images(filename, os.getcwd(), image_path)

        # If Image Path Not Exists Create a Path, Then Add Image to That Path.
        else:
            os.makedirs(image_path)
            categorize_images(filename, os.getcwd(), image_path)
