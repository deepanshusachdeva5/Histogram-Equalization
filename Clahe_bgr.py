import cv2
import numpy as np
import pandas as pd
import argparse
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='image to be processed')
ap.add_argument('-c', '--clip', default=2.0, help='clip size for CLAHE')
ap.add_argument('-t', '--tile', default=8, help='tile size for CLAHE')

args = vars(ap.parse_args())

image = cv2.imread(args['image'])
#image = cv2.resize(image, (300, 300))
(b, g, r) = cv2.split(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

clahe = cv2.createCLAHE(
    clipLimit=args['clip'], tileGridSize=(args['tile'], args['tile']))
equalized_imageb = clahe.apply(b)
equalized_imageg = clahe.apply(g)
equalized_imager = clahe.apply(r)

merged = cv2.merge([equalized_imageb, equalized_imageg, equalized_imager])
cv2.imwrite('test1.jpg', merged)

hist_original = cv2.calcHist([gray], [0], None, [256], [0, 256])
hist_equalizedb = cv2.calcHist([equalized_imageb], [0], None, [256], [0, 256])
hist_equalizedg = cv2.calcHist([equalized_imageg], [0], None, [256], [0, 256])
hist_equalizedr = cv2.calcHist([equalized_imager], [0], None, [256], [0, 256])


plt.figure()
plt.title('Original Image Histogram')
plt.plot(hist_original)

plt.figure()
plt.title('CLAHE Equalized Image Histogram')
plt.plot(hist_equalizedb)
plt.plot(hist_equalizedg)
plt.plot(hist_equalizedr)

cv2.imshow('Original Image', image)
#cv2.imshow('Equalized Image', equalized_image)
cv2.imshow('Equalized Image', merged)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
