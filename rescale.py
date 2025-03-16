import cv2 as cv

img = cv.imread('Photos/cat.jpg')
capture = cv.VideoCapture('Videos/dog.mp4')

def rescaleFrame(frame, scale=0.75):
    # images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # live video
    capture.set(3, width)
    capture.set(4, height)
    
   
cv.imshow('Cat',rescaleFrame(img))
cv.waitKey(0) 
    

while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame)
    
    cv.imshow('Video',frame)
    cv.imshow('Video',frame_resized)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()