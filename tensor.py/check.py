import cv2
import tensorflow as tf

import numpy as np

def prepare(filepath):

    img_size = 50
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    img_array = img_array/255.0
    new_array = cv2.resize(img_array , (img_size,img_size))
    return new_array.reshape(-1, img_size,img_size,1)


model = tf.keras.models.load_model("dogsandcatsconvnet4.model")

prediction = model.predict([prepare('E:\cat1.jpg')])
print(prediction[0])