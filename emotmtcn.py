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
            

            if len(roi_gray) > 0:
                face = roi_gray.astype('float')/255.0
              
                face_array = img_to_array(face)
               
                face = np.expand_dims(face_array, axis=0)
              
                
                preds = classifier.predict(face)[0]
               
                
               


                label = class_labels[preds.argmax()]

            
                x=x
                y=y+240
                label_position = (x,y)
                
                print(label_position)
                cv2.putText(frame,label , label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                
    except Exception as e:
        pass
    cv2.imshow(("Emotion Detector"),cv2.resize(frame, (480,360), interpolation = cv2.INTER_LINEAR))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()








