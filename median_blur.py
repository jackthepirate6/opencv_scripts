import cv2

img = cv2.imread('dog.jpg')

#here 5 is the size of the kernel and it has to be odd
median_img = cv2.medianBlur(img,5)
