import dlib
import cv2
import numpy as np

def image_lab2bgr(image,color):
    if(image.shape[-1] != 3):
        image = image.astype(np.float32)
        image = np.transpose(image, (1, 2, 0))
        updated_image = cv2.cvtColor(image, cv2.COLOR_LAB2RGB)  * 255.
        updated_image = np.transpose(updated_image, (2, 0, 1))
        return updated_image
    return cv2.cvtColor(image, cv2.COLOR_LAB2)  * 255 

