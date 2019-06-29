import cv2

img = cv2.imread('dog.jpg')

#here (5,5) is the size of gaussian kernel
#here 0 is sigmaX, originally it is specified like (sigmaX,sigmaY), but if sigmaY is not specified, it is taken equal to sigmaX.
blur_img = cv2.GaussianBlur(img,(5,5),0)
