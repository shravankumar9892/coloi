import numpy as np
import cv2

# Download the dataset from 
# https://www.kaggle.com/shravankumar9892/image-colorization

def LUV(image, conversion = 1, inter = cv2.INTER_AREA):
    # Instead of loading images from the array, I'm doing everything again here so that it shouldn't give memory error.
    img = cv2.imread(image, 1)
    img = cv2.resize(img, (224,224), interpolation = inter)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    luv = (cv2.cvtColor(img,cv2.COLOR_RGB2LAB)+[0, 128, 128])/[100,255,255]
    return luv[:,:,0], luv[:,:,1:]

l = []
ab = []
# converting bgr to luv color space
#for i in range(2):
#    
#    l.append(luv[:,:,0])
#    ab.append(luv[:,:,1:])
#np.save("../../coloi1/dataset/l.npy", np.asarray(l))
#np.save("../../coloi1/dataset/ab.npy", np.asarray(ab))        
#image_array = np.load("../../coloi1/dataset/rgb.npy")     	

for i in range(25000):
    file = "../../coloi1/mirflickr25k(1)/mirflickr/im"+str(i+1)+".jpg"
    m,n = LUV(file)	
    l.append(m)
    ab.append(n)	
np.save("../../coloi1/dataset/l.npy", np.asarray(l))
np.save("../../coloi1/dataset/ab.npy", np.asarray(ab))



