import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, MaxPooling2D, Activation, Dense, Dropout
import matplotlib.pyplot as plt
import numpy as np
import pickle
import cv2
from tensorflow.keras.callbacks import TensorBoard
import time
import os
NAME = "dogs-vs-cats-cnn-64by2-{}".format(int(time.time()))

log_dir = 'logs\\{}'.format(NAME)

tensorboard = TensorBoard(log_dir=log_dir)

A = pickle.load(open("A.pickle", "rb"))

B = pickle.load(open("B.pickle", "rb"))

A = A/255.0


model = Sequential()

model.add(Conv2D(64, (3,3), input_shape = A.shape[1:]))

model.add(Activation("relu"))

model.add(MaxPooling2D(2,2))


model.add(Conv2D(64, (3,3)))

model.add(Activation("relu"))

model.add(MaxPooling2D(2,2))


model.add(Conv2D(64, (3,3)))

model.add(Activation("relu"))

model.add(MaxPooling2D(2,2))



model.add(Flatten())

model.add(Dense(64))
model.add(Activation("relu"))

model.add(Dense(1))


model.add(Activation("sigmoid"))


model.compile(optimizer = "adam",
                loss = "binary_crossentropy",
                metrics = ['accuracy'])

model.fit(A,np.array(B),   batch_size = 32, epochs = 6, validation_split = 0.3, callbacks = [tensorboard])

model.save("dogsandcatsconvnet4.model")