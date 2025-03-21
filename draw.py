import cv2 as cv
import numpy as np


img = cv.imread('Photos/cat.jpg')
blank = np.zeros((500,500,3),dtype='uint8')


# blank[200:300, 300:400] = 0,255,0
# cv.imshow('Green', blank)

# draw a rectangle
cv.rectangle(blank, (0,0), (250,250), (0,250,0), thickness=cv.FILLED)
# cv.imshow('Rectangle', blank)

# draw a circle
circle = cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)

# draw a  line
line = cv.line(blank, (0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255), thickness=3)

# write text
cv.putText(blank, "Init text",(255,255), cv.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0),thickness=2)

cv.imshow('Text', blank)

cv.waitKey(0)