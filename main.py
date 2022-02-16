# convert any image to a sketch!
# pip install opencv-python
import cv2
# create two windows to display original and transformed
cv2.namedWindow('original', cv2.WINDOW_NORMAL)
cv2.resizeWindow('original', 800, 600)
cv2.namedWindow('transformed', cv2.WINDOW_NORMAL)
cv2.resizeWindow('transformed', 800, 600)
# load image
img = cv2.imread('IMG_0969.JPG')
# convert image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# invert the grayscale image
inverted_gray_img = 255 - gray_img
# blur gray image
blur_inverted_gray_img = cv2.GaussianBlur(inverted_gray_img, (131, 131), 0)
# invert the blurred image back
inverted_blur = 255 - blur_inverted_gray_img
# divide the gray image by the blurred image and scale
sketch = cv2.divide(gray_img, inverted_blur, scale=256)
# display the image
cv2.imshow('original', img)
cv2.imshow('transformed', sketch)
# save your sketch
cv2.imwrite('my_sketch.png', sketch)
# wait x miliseconds before automatically closing
cv2.waitKey(0)