# Histogram-Equalization
HISTOGRAM EQUALIZATION
In the previous tutorial we learnt about histograms in image processing and how it works, this time we are going to level up and see its implementation in feature extraction techniques and how this simple technique actually levels up your game!
Consider the image below, this image has irregular lighting conditions , which makes it difficult to detect objects in the image. So, you can apply a simple technique known as histogram equalization to improve the results of your detection or improve the lighting in this image.
Let's see how can we do that in python! Lets start by importing these packages. If you don't have any package installed in the below code block
just go to terminal and type pip install package-name.
import cv2
import argparse
import numpy as np
import matplotlib.pyplot as plt
Fortunately, OpenCV provides us with histogram equalization method from default, all you have to do is:
Load the image
Covert it to grayscale
Apply cv2.equalizeHist(gray_scale_image)

Lets see it in action!
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='image to be prcoessed')
args = vars(ap.parse_args())
image = cv2.imread(args['image'])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
equalized_image = cv2.equalizeHist(gray)
cv2.imshow("original gray", gray)
cv2.imshow("Equalized image", equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

And the result is this:
Original image vs equalized imageNow, As you can see that though we can see the objects in the background like that "A" looking object on the right or chairs that you can see clearly now, or the objects on the top of the fireplace, but some noise has been amplified too! Now this is due to the fact that the image lighting was equalized on the whole image at once and this overamplified the image noise ,so to tackle that problem we can use adaptive histogram equalization which applies histogram equalization piece by piece or you can say window by window.
Now this is called CLAHE(Contrast Limited Adaptive Histogram Equalization).
Now how this works is:
Adaptive histogram equalization does not compute one but several histograms in an image each one belonging to a distinct part of the image and using those histograms to redistribute the lighting condition of that image. Now , this method improves the local contrast and improves the edge definition.
However applying only AHE actually overamplifies the noise in relatively homogeneous regions of an image.
Now, normal Histogram equalization uses a single transformation function throughout the image, but adaptive histogram equalization actually uses different types of transformation function in each local neighborhood of the image. 
This transformation function is proportional to the cumulative distribution function (CDF) of pixel values in the neighborhood.
Now , applying only AHE , can actually overamplify noise in the relatively homogenous regions , so to tackle this CLAHE comes into picture:
In CLAHE, the contrast amplification in the vicinity of a given pixel value is given by the slope of the transformation function.
Now this transformation function is directly proportional to the slope of the neighborhood cumulative distribution function (CDF). CLAHE limits the amplification of noise by clipping the histogram at a predefined value before computing the CDF. This limits the slope of the CDF and therefore of the transformation function which in turn limits the overamplification of noise.
Generally this clip limit is between 3–5.
Lets see that in action!
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='image to be processed')
ap.add_argument('-c', '--clip', default=2.0, help='clip size for CLAHE')
ap.add_argument('-t', '--tile', default=8, help='tile size for CLAHE')
args = vars(ap.parse_args())
Here , the clip is the clip limit as we discussed above and tile is the neighborhood size , a size of 8 means we are going to divide this image in (8x8) neighborhood.
image = cv2.imread(args['image'])

(b, g, r) = cv2.split(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
clahe = cv2.createCLAHE(
    clipLimit=args['clip'], tileGridSize=(args['tile'], args['tile']))
equalized_imageb = clahe.apply(b)
equalized_imageg = clahe.apply(g)
equalized_imager = clahe.apply(r)
merged = cv2.merge([equalized_imageb, equalized_imageg, equalized_imager])
cv2.imshow('Original Image', image)
cv2.imshow('Equalized Image', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
Now Lets, see the results,
Original vs equalized(CLAHE)Now , In these two images you can see that in equalized image, the contrast is actually enhanced significantly and this method generally gives an edge , while performing certain computer vision tasks.
You can find the full code here
