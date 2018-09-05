import numpy as np
import cv2

# image_array is an array with bgr values of each image, per element.
image_array = np.load("../../dataset/images.npy")

# converting bgr to luv color space
Luv = []

for i in range(25000):
	Luv.append(cv2.cvtColor(image_array[i],cv2.COLOR_BGR2LUV))	
	
Luv = np.asarray(Luv) # It's showing a memory error in this line :/

np.save("../../dataset/Luv.npy", Luv)




