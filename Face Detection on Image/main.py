"""
@Project_Description:
    Observe HaarCascade Face Recognition Classifier
    performance on basic to complex images.

@Author:
    Can Ali Ates
"""

# Import Libraries.
import os
import cv2

# Import Classifier.
faceCascade = cv2.CascadeClassifier("Files/face_recognition.xml")

# Create a Directory to Save Results.
if not os.path.isdir("Output"):
    os.mkdir("Output")

# Arrange Suffixes to Detect Images.
suffixes = (".png", ".jpg", ".jpeg")

# Iterate Over Media Files.
for file in os.listdir("Media"):

    # Check Image File.
    if file.endswith(suffixes):

        # Read Image.
        image = cv2.imread(f"Media/{file}")

        # Convert Image to Gray Scale.
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Arrange HaarCascade Face Classifier Parameters.
        faces = faceCascade.detectMultiScale(gray,  scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

        # Print Count of Detected Faces.
        image = cv2.putText(image, f"Face Count: {len(faces)}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)

        # Draw Rectangle Around Face(s).
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Show Face Detected Images.
        cv2.imshow("Face Recognition", image)

        # Save Result.
        cv2.imwrite(f"Output/{file}", image)

        # Arrange Image Duration to 1 second.
        cv2.waitKey(1500)

# Close All Windows.
cv2.waitKey(0)
cv2.destroyAllWindows()
