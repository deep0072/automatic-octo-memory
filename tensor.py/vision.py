import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

mnist = keras.datasets.fashion_mnist  #this is data of different dresses and shoes

(training_images, training_labels), (test_images, test_labels) = mnist.load_data()  #this is used to load the data





training_images = training_images/255.0   #here is training images wchich will be feed to the neural network for training and first it will be converted into the o and 1 

test_images = test_images/255.0      #these iamges are used for testing by feeding it to the neural network

model = keras.models.Sequential()  #here sequential is use for applying layers of neurons
model.add(keras.layers.Flatten())  #this is input layer which will take all training images and convert it into the one dimesnional array
model.add(keras.layers.Dense(128, activation = tf.nn.relu))  #these are the hidden layer having 128 neuron which will use activation function relu
model.add(keras.layers.Dense(128, activation = tf.nn.relu))  #Activation function decides, whether a neuron should be activated or not by calculating weighted sum and further adding bias with it
model.add(keras.layers.Dense(128, activation = tf.nn.relu))

model.add(keras.layers.Dense(10, activation = tf.nn.softmax)) # this is output layer having 10 neuron which willbe decided on bases of classification of images
                                                            
                                                            # this takes softmax activation function which will select one node by assigning highest no to it


model.compile(optimizer = 'adam',        #this is compiling stage of neurons in which optimizzer will be used to check the accuracy at each step like how much it is the near to  positive value
    
    loss = 'sparse_categorical_crossentropy', # this is loss function for telling that how badly neuron behaving when it encounter with data
    
    metrics=['accuracy'])  


model.fit(training_images, training_labels, epochs = 5)  #it use to train the neural network where epochs is use to set no. of times for testing process



print(model.evaluate(test_images, test_labels)) #here evaluate method is used to test the neural network with test images wrt to the testing labels


classifications = model.predict([test_images]) #here predict method is used to predict output by feeding new data
 
print(np.argmax(classifications[1500]))  
plt.imshow(test_images[1500])
plt.show()



 

  
