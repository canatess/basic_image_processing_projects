"""
@Project_Description:
    Detection of specified color using trackbars.

    @Author_Note:
    ---> Base color values arranged to red.

@Author:
    Can Ali Ates
"""

# Import Library.
import cv2


# Create an Empty Function to Callback.
def Nothing(i):
    pass


# Read and Resize Image.
image = cv2.imread("Media/Red.jpg")
image = cv2.resize(image, (640, 480))

# Create and Resize Empty Windows.
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image", 640, 600)

cv2.namedWindow("Color Detection", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Color Detection", 640, 480)

# Create Trackbar for RGB Color Values.
cv2.createTrackbar("R", "Image", 0, 255, Nothing)
cv2.createTrackbar("G", "Image", 0, 255, Nothing)
cv2.createTrackbar("B", "Image", 0, 255, Nothing)

# Arrange Base Color of Red.
base_color = (0, 0, 50)

# Run The Detector.
while True:

    # Read RGB Color Values from Trackbar.
    red = cv2.getTrackbarPos("R", "Image")
    green = cv2.getTrackbarPos("G", "Image")
    blue = cv2.getTrackbarPos("B", "Image")

    # Arrange Color Masking Values.
    created_color = (red, green, blue)

    # Create a Mask.
    mask = cv2.inRange(image, base_color, created_color)

    # Extract Colored Object from Original Image with Using Mask.
    target = cv2.bitwise_and(image, image, mask=mask)

    # Show the Original Image and Extracted Object According to Color.
    cv2.imshow("Image", image)
    cv2.imshow('Color Detection', target)

    # Press ESC to Exit from Detector.
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Close All Windows.
cv2.waitKey(0)
cv2.destroyAllWindows()
