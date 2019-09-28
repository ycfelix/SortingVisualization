import numpy as np
import cv2
from cv2 import VideoWriter, VideoWriter_fourcc
import os
width = 1280
height = 720
FPS = 24
seconds = 10
fourcc = VideoWriter_fourcc(*'MP42')
video = VideoWriter('./noise.avi', fourcc, float(FPS), (width, height))
white_square=np.full((10,10,3), 255)
for e in range(FPS*seconds):
    frame = np.ones((height,width,3),dtype=np.uint8)
    frame[10+e:20+e,30:40,:]=white_square
    video.write(frame)
video.release()

cap = cv2.VideoCapture('noise.avi')
if (cap.isOpened() == False):
    print("Error opening video stream or file")

# Read until video is completed
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:

        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release the video capture object
cap.release()

os.remove("noise.avi")
# Closes all the frames
cv2.destroyAllWindows()