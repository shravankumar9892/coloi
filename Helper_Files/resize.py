import numpy as np
import cv2

# Function for resizing the image + gray scale
def image_resize(image,conversion = 1, inter = cv2.INTER_AREA):
    # For gray scale: conversion = 0, otherwise let the default condition work.
    img = cv2.imread(image, conversion)
    resized = cv2.resize(img, (224,224), interpolation = inter)
    return resized

# Create a for loop to iterate over every image.(total == 25k)
# Save every image(pixels) in a list by appending each one
# use np.asarry() to convert this list into an array
# Store this numpy array as .npy file.
image_files = []
for i in range(25000):
        # Link for mirflickr is given on the project website :)
	file = "../mirflickr25k(1)/mirflickr/im"+str(i+1)+".jpg"
	image = np.asarray(image_resize(file, 0))
	image_files.append(image)
image_array = np.asarray(image_files)
np.save("../dataset/gray_scale.npy", image_array)
		
