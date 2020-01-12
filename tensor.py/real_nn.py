import tensorflow as tf

from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

import os
import cv2

import random 

import pickle


DATADIR = "E:/datasets/PetImages"


CATEGORIES = ["Dog", "Cat"]
IMg_SIZE = 50

training_data = [ ]
def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_index = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:

                Image_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                NEW_ARRAY = cv2.resize(Image_array, (IMg_SIZE, IMg_SIZE))
                training_data.append([ NEW_ARRAY, class_index])
            except Exception as e:
                pass
create_training_data()

random.shuffle(training_data)

A = [ ]
B = [ ]
for features, labels in training_data:
    A.append(features)
    B.append(labels)

A = np.array(A).reshape(-1, IMg_SIZE,IMg_SIZE ,1)

pickle_out = open("A.pickle", "wb")

pickle.dump(A , pickle_out)

pickle_out.close()


pickle_out = open("B.pickle", "wb")

pickle.dump(B , pickle_out)

pickle_out.close()


pickle_in = open("A.pickle", "rb")

A = pickle.load(pickle_in)
print(A[0])










       


    
