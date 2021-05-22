Adaptive histogram equalization does not compute one but several histograms in an image each one belonging to a distinct part of the image and using those histograms to redistribute the lighting condition of that image. Now , this method improves the local contrast and improves the edge definition.
However applying only AHE actually overamplifies the noise in relatively homogeneous regions of an image.
Now, normal Histogram equalization uses a single transformation function throughout the image, but adaptive histogram equalization actually uses different types of transformation function in each local neighborhood of the image. 
This transformation function is proportional to the cumulative distribution function (CDF) of pixel values in the neighborhood.
Now , applying only AHE , can actually overamplify noise in the relatively homogenous regions , so to tackle this CLAHE comes into picture:
In CLAHE, the contrast amplification in the vicinity of a given pixel value is given by the slope of the transformation function.
Now this transformation function is directly proportional to the slope of the neighborhood cumulative distribution function (CDF). CLAHE limits the amplification of noise by clipping the histogram at a predefined value before computing the CDF. This limits the slope of the CDF and therefore of the transformation function which in turn limits the overamplification of noise.
Generally this clip limit is between 3–5.
