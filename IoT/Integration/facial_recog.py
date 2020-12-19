import cv2, os
import face_recognition


folder = 'Imgs'
def CaptureTestImg():
    videoCaptureObject = cv2.VideoCapture(0)
    #saving the image into a jpg file
    ret,frame = videoCaptureObject.read()
    cv2.imwrite("pic2.jpg",frame)
    imgTest = face_recognition.load_image_file('pic2.jpg')
    imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)
    encodeTest = face_recognition.face_encodings(imgTest)[0]
    DeleteTestImg()
    return encodeTest

def DeleteTestImg():
    os.remove("pic2.jpg")

    

def LoadImagesFromFolder(folder):
    img_list = []
    for imgname in os.listdir(folder):    
        img = face_recognition.load_image_file(os.path.join(folder,imgname))
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img = face_recognition.face_encodings(img)[0]
        img_list.append(img)
    return img_list
    

def RegisterNewUser(Name):
    videoCaptureObject = cv2.VideoCapture(0)
    #saving the image into a jpg file
    ret,frame = videoCaptureObject.read()
    cv2.imwrite("Imgs/" + Name + ".jpg",frame)

def GetImageEncoding(Name):
    videoCaptureObject = cv2.VideoCapture(0)
    #saving the image into a jpg file
    ret,frame = videoCaptureObject.read()
    cv2.imwrite("Imgs/" + Name + ".jpg",frame)
    imgSource = face_recognition.load_image_file("Imgs/" + Name + ".jpg")
    imgSource = cv2.cvtColor(imgSource,cv2.COLOR_BGR2RGB)
    encodeSource = face_recognition.face_encodings(imgSource)[0]
    return encodeSource

def RecognizeUser(folder = 'Imgs'):
    img_list = LoadImagesFromFolder(folder)
    encodeTest = CaptureTestImg()
    for img in img_list:
        result = face_recognition.compare_faces([img],encodeTest)
        if result:
            return True
    
    return False

    
    

def Recognize():
    imgSource = face_recognition.load_image_file('pic1.jpg')
    imgSource = cv2.cvtColor(imgSource,cv2.COLOR_BGR2RGB)
    encodeSource = face_recognition.face_encodings(imgSource)[0]

    # capturing a new image using the webcam
    videoCaptureObject = cv2.VideoCapture(0)
    #saving the image into a jpg file
    ret,frame = videoCaptureObject.read()
    cv2.imwrite("pic2.jpg",frame)

    imgTest = face_recognition.load_image_file('pic2.jpg')
    imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)
    encodeTest = face_recognition.face_encodings(imgTest)[0]

    result = face_recognition.compare_faces([encodeSource],encodeTest)
    faceDis = face_recognition.face_distance([encodeSource],encodeTest)

    print(result,faceDis)

    os.remove("pic2.jpg")

    return result


# print(RecognizeUser(folder))
# RegisterNewUser("Hamza")
# Recognize()


