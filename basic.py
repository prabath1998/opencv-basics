import cv2 as cv

img = cv.imread('Photos/park.jpg')
# cv.imshow('Cat',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

# blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)

# Edge cascade
canny = cv.Canny(img,125,175)
# cv.imshow('Canny',canny)

# dialating
dilated = cv.dilate(img, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)

# resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
# cv.imshow('Resized', resized)

# cropping
cropped = img[100:300, 100:300]
cv.imshow('Cropped', cropped)


cv.waitKey(0)