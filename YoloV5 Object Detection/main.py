# Import Libraries.
import time
import torch
import cv2 as cv
import numpy as np

class Detector:
    
    def __init__(self):
        
        # Load Pretrained Model.
        self.model = self.load_model()
        
        # Load Classes From Pretrained Model.
        self.classes = self.model.names
        
        # Decide Device.
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'


    def load_model(self):
        
        # Load YOLOv5 Model From PyTorch Hub. 
        torch_model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        
        # Return Trained PyTorch Model.
        return torch_model


    def score_frame(self, frame):
        
        # Connect Model to CUDA or CPU.
        self.model.to(self.device)
        
        # Convert Frame to NumPy/List/Tuple Format.
        frame = [frame]
        
        # Run Model on Frame, Then Store Results.
        results = self.model(frame)
        
        # Collect Labels and Their Coordinates of Objects Detected by Model in the Frame.
        labels, coordinates = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        
        # Return Labels and Coordinates.
        return labels, coordinates

    def plot_boxes(self, results, frame):
        
        # Distribute Labels and Their Coordinates.
        labels, coordinate = results
        
        # Store Width and Height of Frame.
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        
        # Loop in Detected Labels by Model.
        for i in range(len(labels)):
            row = coordinate[i]
            if row[4] >= 0.2:
                # Find Coordinates of Detected Object.
                x1, y1, x2, y2 = int(row[0]*x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape)
                
                # Draw Rectangle Around Detected Object.
                cv.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                
                # Find The Label Name From Classes According to Label Number.
                label_name = self.classes[int(labels[i])]
                
                # Put Label Name to Detected Object.
                cv.putText(frame, label_name, (x1, y1), cv.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        
        # Return Frame After Draw Rectangle and Put Label Name to All Detected Objects.
        return frame


    def __call__(self):
        
        # Create Camera Object to Connect Device Camera.
        camera = cv.VideoCapture(0)
        
        # Run Loop While Camera is Opened.
        while camera.isOpened():
            
            # Start Time to Calculate FPS.
            start_time = time.perf_counter()
            
            # Read Frame and Camera Feedback.
            ret, frame = camera.read()
            
            # If Feedback Positive Continue Program, Else Break.
            if ret:
                
                # Take Labels and Coordinates of Detected Objects.
                results = self.score_frame(frame)
                
                # Plot Boxes and Put Label Names to Detected Objects.
                frame = self.plot_boxes(results, frame)
                
                # Stop Time to Calculate FPS.
                end_time = time.perf_counter()
                
                # Calculate FPS.
                fps = 1 / np.round(end_time - start_time, 3)
                
                # Show FPS.
                cv.putText(frame, f'FPS: {int(fps)}', (20,70), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 1, cv.LINE_AA)
                
                # Show Frame.
                cv.imshow("Detector", frame)
            else:
                break
            
            # Press ESC to Exit From Program.
            if cv.waitKey(1) & 0xFF == 27:
                break
        
        # Close The Camera.
        camera.release()
        
        # Destroy All Windows.
        cv.destroyAllWindows()


# Create A New Detector Object.
detection = Detector()

# Run Object.
detection()