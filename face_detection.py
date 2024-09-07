import cv2
alg=r"C:\Users\SRUCHEN KUMAR\Downloads\haarcascade_frontalface_default.xml"
haar_cascade=cv2.CascadeClassifier(alg)
cam=cv2.VideoCapture(0  )#Intitialising the camera ID 
while True:#Infinite loop
    _,img=cam.read()#Reading frame from camera and '_' will be like a placeholder
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#Converting color to GrayColor
    faces=haar_cascade.detectMultiScale(grayImg,1.3,4)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,225,0),2)#Drawing rectangle
    cv2.imshow("FaceDetection",img) #Displaying the Frame 
    key=cv2.waitKey(10) #One frame is waited for 10milli seconds for another frame to display
    print(key)
    if key==27:#Escape Key to exit
        break
cam.release()
cv2.destroyAllWindows()