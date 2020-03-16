from tensorflow.keras.models import load_model
from time import sleep
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing import image
import cv2
import numpy as np
from mtcnn.mtcnn import MTCNN
from wide_resnet import  WideResNet

cap = cv2.VideoCapture(0)

detector = MTCNN()
model = WideResNet(64,16,8)()
# model.load_weights("weights.18-4.06.hdf5") to load this weight visit on given link below

#"https://drive.google.com/file/d/12Ub2ZUtiYXL1QKUPlAy6oOG4Qhn0GM0H/view"


classifier =load_model('./Emotion_little_vgg.h5')
class_labels = ['Angry','Happy','Neutral','Sad','Surprise']

while True:
    try:

        rat, frame = cap.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = detector.detect_faces(frame)
        


        for i , face in enumerate(faces):
            x,y,w,h = face['box']
            frame = cv2.rectangle(frame, (x,y),(x+w, y+h), (255,255,0), 2)
            gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
            roi_gray2 = gray[y:y+h, x:x+w]
            roi_gray = cv2.resize(roi_gray2 , (48,48))
            roi_gray1 = np.resize(roi_gray2, (64, 64, 3))

            if len(roi_gray) > 0:
                face = roi_gray.astype('float')/255.0
                face1 = roi_gray1.astype('float')/255.0
                face_array = img_to_array(face)
                face_array1 = img_to_array(roi_gray1)
                face = np.expand_dims(face_array, axis=0)
                face1 = np.expand_dims(face_array1, axis=0)
                results = model.predict(face1)
                preds = classifier.predict(face)[0]
                predicted_genders = results[0]
                ages = np.arange(0, 101).reshape(101, 1)
                predicted_ages = results[1].dot(ages).flatten()

                
                label1 = "{}, {}".format(int(predicted_ages[i]),
                                            "F" if predicted_genders[i][0] > 0.5 else "M")
                print(label1, "this is label1")


                label = class_labels[preds.argmax()]

            
                x=x
                y=y+240
                label_position = (x,y)
                
                print(label_position)
                cv2.putText(frame,label , label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                cv2.putText(frame , label1 , (w, h),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2 )
    except Exception as e:
        pass
    cv2.imshow(("Emotion Detector"),cv2.resize(frame, (480,360), interpolation = cv2.INTER_LINEAR))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()








