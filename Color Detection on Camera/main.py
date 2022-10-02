"""
@Project_Description:
    Detect a color from camera in real time.

@Author:
    Can Ali Ates
"""

# Import Libraries.
import cv2
import numpy


# Empty Function to Callback.
def nothing():
    pass


# Create Camera Object.
camera = cv2.VideoCapture(0)

# Create An Empty Window to Show Camera Frame.
cv2.namedWindow("Specify Color", cv2.WINDOW_NORMAL)
cv2.namedWindow("HSV Frame", cv2.WINDOW_NORMAL)

# Create Trackbars for HSV Values.
cv2.createTrackbar("H1", "Specify Color", 0, 359, nothing)
cv2.createTrackbar("S1", "Specify Color", 0, 255, nothing)
cv2.createTrackbar("V1", "Specify Color", 0, 255, nothing)
cv2.createTrackbar("H2", "Specify Color", 0, 359, nothing)
cv2.createTrackbar("S2", "Specify Color", 0, 255, nothing)
cv2.createTrackbar("V2", "Specify Color", 0, 255, nothing)

# Check Camera Status.
while camera.isOpened():

    # Read Frame From Camera.
    _, frame = camera.read()

    # Change Frame Color Values to HSV.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Take HSV Values From Trackbars.
    H1 = int(cv2.getTrackbarPos("H1", "Specify Color") / 2)
    S1 = cv2.getTrackbarPos("S1", "Specify Color")
    V1 = cv2.getTrackbarPos("V1", "Specify Color")
    H2 = int(cv2.getTrackbarPos("H2", "Specify Color") / 2)
    S2 = cv2.getTrackbarPos("S2", "Specify Color")
    V2 = cv2.getTrackbarPos("V2", "Specify Color")

    # Arrange Upper and Lower Values of Color.
    lower = numpy.array([H1, S1, V1])
    upper = numpy.array([H2, S2, V2])

    # Create Mask For Specified Color.
    mask = cv2.inRange(hsv, lower, upper)

    # Apply Mask to Frame.
    target = cv2.bitwise_and(frame, frame, mask=mask)

    # Show Frame and Color Detection Frame.
    cv2.imshow("Specify Color", frame)
    cv2.imshow("HSV Frame", target)

    # Exit the Program with ESC.
    if cv2.waitKey(1) == 27:
        break

# Close All Windows
camera.release()
cv2.destroyAllWindows()
