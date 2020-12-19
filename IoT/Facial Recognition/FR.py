

import cv2, os
import face_recognition
 

def Recognize():
    imgSource = face_recognition.load_image_file('pic1.jpg')
    imgSource = cv2.cvtColor(imgSource,cv2.COLOR_BGR2RGB)
    encodeSource = face_recognition.face_encodings(imgSource)[0]

    #uncommnt this part if you want to the system to take an image of you and compare it the "pic1.jpg"
    # capturing a new image using the webcam
    # videoCaptureObject = cv2.VideoCapture(0)
    # #saving the image into a jpg file
    # ret,frame = videoCaptureObject.read()
    # cv2.imwrite("pic2.jpg",frame)

    imgTest = face_recognition.load_image_file('pic2.jpg')
    imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)
    encodeTest = face_recognition.face_encodings(imgTest)[0]

    result = face_recognition.compare_faces([encodeSource],encodeTest)
    faceDis = face_recognition.face_distance([encodeSource],encodeTest)

    print(result,faceDis)

    # os.remove("pic2.jpg")

    return result



Recognize()