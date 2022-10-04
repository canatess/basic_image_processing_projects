import cv2 as cv

camera = cv.VideoCapture(0)

tomato_cascade = cv.CascadeClassifier('pen.xml')

while camera.isOpened():
    
    ret, frame = camera.read()
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    tomatoes = tomato_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in tomatoes:
        cv.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
        cv.putText(frame, "Pen", (x - 10, y - 10), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv.LINE_AA)
        
    cv.imshow("Frame", frame)
    if cv.waitKey(1) & 0xFF == 27:
        break

camera.release()
cv.destroyAllWindows()