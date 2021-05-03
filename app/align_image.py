# Imports
import os
import re
import imutils
import pytesseract
import cv2 

import numpy as np
from wand.image import Image as WandImage
from PIL import Image as Image

# Get angle
def get_angle(image):
    osd = pytesseract.image_to_osd(image)
    angle = float(re.search('(?<=Rotate: )\d+', osd).group(0))
    return angle


def align_image(image):
    return skew_image(correct_angle(image))

# Main
def correct_angle(image):
    #Image is opencv image
    angle = get_angle(Image.fromarray(image))
    print(angle)

    if angle == 0.0:
        return image

    new_image = imutils.rotate_bound(image,angle)

    r_angle = get_angle(Image.fromarray(new_image))
    if r_angle != 0:    
        new_image = imutils.rotate_bound(image, -angle)

    return new_image

def skew_image(image):
    img = WandImage.from_array(image) 
    img.deskew(0.4*img.quantum_range)
    return img

def main(img_path):
    image = cv2.imread(img_path)
    image_name = os.path.basename(img_path)

    image = correct_angle(image)
    result = skew_image(image)
    result.save(filename='output-' + image_name)

if __name__ == '__main__':
    pass

"""
Resources
1. https://stackoverflow.com/questions/43232813/convert-opencv-image-format-to-pil-image-format
2. https://stackoverflow.com/questions/47515243/reading-image-file-file-storage-object-using-cv2
(use frombuffer instead)

"""