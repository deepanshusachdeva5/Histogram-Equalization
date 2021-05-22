import cv2
import argparse
import numpy as np
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='image to be prcoessed')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

equalized_image = cv2.equalizeHist(gray)

hist_original = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title('Original image Histogram')
plt.plot(hist_original)

hist_equalized = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])
plt.figure()
plt.title('Eqalized image image Histogram')
plt.plot(hist_equalized)


cv2.imshow("original gray", gray)
cv2.imshow("Equalized image", equalized_image)
equalized_image = cv2.resize(equalized_image, (300, 300))
gray = cv2.resize(gray, (300, 300))
cv2.imwrite("Equalized image.jpg", equalized_image)
cv2.imwrite("gray_original.jpg", gray)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
