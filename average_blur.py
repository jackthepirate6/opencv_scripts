import cv2

img = cv2.imread('dog.jpg')

#here (3,3) is the kernel size for blurring operation
blur_image = cv2.blur(img,(3,3))

