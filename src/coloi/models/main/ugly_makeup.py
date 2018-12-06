from PIL import Image, ImageDraw
import face_recognition
import numpy as np
import cv2
import sys
import matplotlib.pyplot as plt

# Getting a reference to webcam
video_capture = cv2.VideoCapture(0)

while True:
    
    ret, frame = video_capture.read()
    
    # Convert the image from BGR color to RGB color 
    rgb_frame = frame[:, :, ::-1]

    # Find all facial features in all the faces in the image
    face_landmarks_list = face_recognition.face_landmarks(rgb_frame)
    
    for face_landmarks in face_landmarks_list:
        pil_image = Image.fromarray(image)
        d = ImageDraw.Draw(pil_image, 'RGBA')

        # Make the eyebrows into a nightmare
        d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
        d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
        d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=5)
        d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=5)

        # Gloss the lips
        d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
        d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
        d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=8)
        d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=8)

        # Sparkle the eyes
        d.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 30))
        d.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 30))

        # Apply some eyeliner
        d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=6)
        d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=6)

        pil_image.show()
    
    # Displaying the resulting image
    #cv2.imshow('Output', frame)

    # Hit 'q'  to quit!!!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
