"""
@Project_Description:
    Detection of eye and mouth on frontal faces on image
    with using HaarCascade XML files.

@Author:
    Can Ali Ates
"""

# Import Libraries.
import os
import cv2

# Import XML Files.
eye_cascade = cv2.CascadeClassifier('Files/eye_recognition.xml')
mouth_cascade = cv2.CascadeClassifier('Files/mouth_recognition.xml')

# Read Image.
image = cv2.imread("Media/Friends.jpg")

# Convert Image to Gray Scale.
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect Eyes and Mouth.
eyes = eye_cascade.detectMultiScale(gray_image, 1.3, 7)
mouth = mouth_cascade.detectMultiScale(gray_image, 1.5, 37)

# Draw Rectangle Around Eyes.
for(ex, ey, ew, eh) in eyes:
    cv2.rectangle(image, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 3)

# Draw Rectangle Around Mouth.
for(mx, my, mw, mh) in mouth:
    cv2.rectangle(image, (mx, my), (mx+mw, my+mh), (255, 0, 0), 3)

# Show Detection Results.
cv2.imshow("Eyes & Mouth Detection", image)

# Save Results.
if not os.path.isdir("Output"):
    os.mkdir("Output")

cv2.imwrite("Output/Eye_Mouth_Detected.jpg", image)

# Close All Windows.
cv2.waitKey(0)
cv2.destroyAllWindows()
