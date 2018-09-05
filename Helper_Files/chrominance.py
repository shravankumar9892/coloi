import numpy as np
import cv2

# image_array is an array with bgr values of each image, per element.
image_array = np.load("../../dataset/images.npy")

# Scaling the image between 0 and 1
#image_array = image_array/255

# converting bgr to luv color space
image_luv = cv2.cvtColor(image_array, 'CV_RGB2Luv')
L = []
u = []
v = []
# Seperating L, u and v
for i in range(25000):
	a,b,c = image_luv[i]
	L.append(a)
	u.append(b)
	v.append(c)
L = np.asarray(L)
u = np.asarray(u)
v = np.asarray(v)

np.save("../../dataset/u.npy", u)
np.save("../../dataset/v.npy", v)




