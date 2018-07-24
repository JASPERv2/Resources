'''
Using OpenCV takes a mp4 video and produces a number of images.
Requirements
----
You require OpenCV 3.2 to be installed.
Run
----
Open the main.py and edit the path to the video. Then run:
$ python main.py
Which will produce a folder called data with the images. There will be 2000+ images for example.mp4.
'''
import cv2
import numpy as np
import os
i=1
# Playing video from camera:
cap = cv2.VideoCapture(0)

while(True):
	try:
    		if not os.path.exists('training-data/s'+str(i)):
        		os.makedirs('training-data/s'+str(i))
			break

		i=i+1

	except OSError:
   	     print ('Error: Creating directory of data')

currentFrame = 1
while(currentFrame<=20):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    name = './training-data/s'+str(i)+'/'+ str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1

while(True):
	ret, frame = cap.read()
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
           break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
