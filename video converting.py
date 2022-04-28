# convert video into jpeg file for input into ML model through Pandas
# jpeg can then be added to an array

import cv2
import math

count = 0
videoFile = "C:/Users/mjos0003/Documents/FYP/TrackMonitorML/30_sec_video_1.mp4" # file path
cap = cv2.VideoCapture(videoFile)   # capturing the video from the given path
frameRate = cap.get(5) #frame rate
x=1

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0): # print 1 frame per second
        filename ="frame%d.jpg" % count;count+=1
        print(filename) # print filename
        writeStatus = cv2.imwrite(filename, frame)
        if writeStatus is True:
          print("image written")
        else:
          print("problem") # or raise exception, handle problem, etc.
cap.release()
print ("Done!")

