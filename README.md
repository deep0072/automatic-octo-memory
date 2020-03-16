well hi my name id Deepak and i am newbie in deep learning...well i know you dont give damn about me...

so how is this working well lemme get back to straight on the the topic...also pardon on my english....

so i am using mtccn that is Multi-Task Cascaded Convolutional Neural Network...now you are wondering what the hell is this....ok let me explain...
In deep learning we used cnn which perform a defined steps like 
feature extraction  and then classification  now what is features so suppose there is cat its attributes are two ears , four legs etc so these attributes are 
features and classification is the what type of that image relate to as we discussed earlier that image was of cat so its calssified that is cat..or it is animal..

so in this project i used vggNEt which is based on CNN.for more depth you can search on google... or u can ask me...
how is this project is working well as vgg is used in  this so it like to eat 48*48 image size....wait what is it eating...is this alive?

well dont panic as cnn has different layers where images are fed from first layer up to the last layer...eating means when images are fed
to these layers then each layers start to exract its each pixel value and calculate and fire to its next layer and so on and after that outer layer
in the end we get  calculated images that is kind of average of all images and classified simultaneously wrt to its defined classes which
we defined...

each layer uses some function like relu (rectified linear unit) and optimizer which optimized the images and send it to next block of 
layers which is kind of  boring and hectic task... and for classification we uses maxpooling function..what it does that it gives us max probabilty of 
calculated images....

so we fed two types of images one for training purposes and one for testing...
training images are use to teach the cnn like what images should be called...like a student...woah we are teachers hurray! lol


now we again uses testing images to make sure that our student is performing well or not...well mostly dont perform well because of little 
study material...means when we give huge dataset to cnn its accuracy of learning will be increases...so thats why  i said...

so  it depends all on data...so when we get better accuracy in learning as well as in testing we uses it for real life applications
ok now lets get back to the on our project...

as mtcnn also based on cnn so it uses same method... mtcnn main function is to detect the faces just for detection which is already 
developed algorithm... so we dont need to train it...

it also give information about where are our eyes ears and lips... pretty cool.. thanks to our deep learning community for this algo

well so when we run emotmtcn.py it just triggered mtcnn for face detection and try to find our face and then our cnn model 

"Emotion_little_vgg,h5" it is kerad based model which contain information about expression...

so when a face detected with the help of mtcnn then that face will be albow aside in that model..
then that model will match it with its learned material and gives us information about our  emotions...

just download it and run "emotmtcnn.py" and boom.....

thanks for reading it...





