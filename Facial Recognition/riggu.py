import cv2,os
import numpy as np
from PIL import Image
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

Motor1A = 16
Motor1B = 18
Motor1E = 22

Motor2A = 23
Motor2B = 21
Motor2E = 19

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.createLBPHFaceRecognizer()
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
while true:
    recognizer.load('trainner/trainner.yml')
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        if(conf<50):
            if(Id==1):
                Id="AJ"
            elif(Id==2):
                Id="MRSP"
            elif(Id==3):
                Id="Vamsee"
            elif(Id==4):
                Id="Girish"
        else:
            Id="Unknown"
        cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font, (0,0,0))
    cv2.imshow('im',im)
    if (Id=="Unknown")
        Id=raw_input('enter your id')
        sampleNum=0
        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
                #incrementing sample number
                sampleNum=sampleNum+1
                #saving the captured face in the dataset folder
                cv2.imwrite("dataSet/User."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
        
                cv2.imshow('frame',img)
            if sampleNum>20:
                break
        def getImagesAndLabels(path):
            #get the path of all the files in the folder
            imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
            #create empth face list
            faceSamples=[]
            #create empty ID list
            Ids=[]
            #now looping through all the image paths and loading the Ids and the images
            for imagePath in imagePaths:
                #loading the image and converting it to gray scale
                pilImage=Image.open(imagePath).convert('L')
                #Now we are converting the PIL image into numpy array
                imageNp=np.array(pilImage,'uint8')
                #getting the Id from the image
                Id=int(os.path.split(imagePath)[-1].split(".")[1])
                # extract the face from the training image sample
                faces=detector.detectMultiScale(imageNp)
                #If a face is there then append that in the list as well as Id of it
                for (x,y,w,h) in faces:
                    faceSamples.append(imageNp[y:y+h,x:x+w])
                    Ids.append(Id)
            return faceSamples,Ids
        faces,Ids = getImagesAndLabels('./dataSet1')
        recognizer.train(faces, np.array(Ids))
        recognizer.save('trainner/trainner.yml')
    if (w>=350 || h>=350):
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.HIGH)
        GPIO.output(Motor1E,GPIO.HIGH)

        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.HIGH)
        GPIO.output(Motor2E,GPIO.HIGH)
    elsif(w<=200 || h<=200):
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor1E,GPIO.HIGH)

        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.HIGH)
    else:
        GPIO.output(Motor1E,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.LOW)
cam.release()
cv2.destroyAllWindows()

