import cv2

img = cv2.imread('dog.jpg')

#here 9 is the kernel size of filter, 75 is the sigma in the colour space, 75 is the sigma in the coordinate space
bilFilter_img = cv2.bilateralFilter(img,9,75,75) 
