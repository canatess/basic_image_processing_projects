"""
@Project_Description:
    Detect and count faces on camera in real time.

@Author:
    Can Ali Ates
"""

# Import Library.
import cv2

# Read XML File to Detect Frontal Faces.
faceCascade = cv2.CascadeClassifier("Files/face_recognition.xml")

# Create Camera Object.
camera = cv2.VideoCapture(0)

# Check Camera Status.
while camera.isOpened():

    # Read Camera Frame.
    ret, frame = camera.read()

    # Terminate Program with ESC.
    if cv2.waitKey(1) & 0xFF == 27:
        break

    # Frame Can Read From Camera.
    if ret:

        # Convert Frame to Gray Scale.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect Faces On Frame.
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

        # Draw Rectangle Around Faces.
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Show Face Count on Frame.
        frame = cv2.putText(frame,  f"Face Count: {len(faces)}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        # Show Frame on Screen.
        cv2.imshow("Screen", frame)

    # Frame Can't Read From Camera.
    else:
        print("Frame Can't Read From Camera.")
        break

# Close All Windows.
camera.release()
cv2.destroyAllWindows()