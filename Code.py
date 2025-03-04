import cv2
import numpy as np
import random

'''
    Face - detection of given image or through using camera xD

'''

a = input('''Enter your choice for face detection and camera ...
*** for camera enter : Cam   ***
*** for image enter : Img    ***
Type here -> ''')

model = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")    # model which detect face 


if (a == 'cam' or a == 'Cam'):
    # Capture video from our cam
    cam = cv2.VideoCapture(0)
    
    while cam.isOpened():
        ret, frame = cam.read()  # Read each frame
        if not ret:
            break  # Exit if there's a dikkat in camera
    
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to b&w aka gay scale
    
        faces = model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))   # face detection 
    
        # it will draw retangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255,0,0), 3)
    
        cv2.imshow("Real-Time Face Detection", frame)
    
        if cv2.waitKey(1) == ord("q"):
            break
    
    cam.release()
    cv2.destroyAllWindows()

else :
    img = input("Enter image path or image name which present in folder ")
    img = img + ".jpg"
    image = cv2.imread(img)                      # reading the given img
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)       # converting given img into grey scale
    
    faces = model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))   # detect face in img
    
    # for drwaing rectangle on faces hehe
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 3)
    
    cv2.imshow("Face Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  
