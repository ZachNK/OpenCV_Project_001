import cv2 as cv


cam=cv.VideoCapture(0)

ret, frame1=cam.read()
ret, frame2=cam.read()

while cam.isOpened():
    diff=cv.absdiff(frame1, frame2)
    gray=cv.cvtColor(diff,cv.COLOR_RGB2GRAY)
    blur=cv.GaussianBlur(gray,(5,5),0)
    _,thres=cv.threshold(blur,20, 255, cv.THRESH_BINARY)
    dil=cv.dilate(thres, None, iterations=5)
    contours,_=cv.findContours(dil,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h)=cv.boundingRect(contour)
        if cv.contourArea(contour) <700:
            continue
        cv.rectangle(frame1,(x,y), (w+x,h+y), (0,255,0), 2)
        cv.putText(frame1,"Status: {}".format('Movement'),(50,50),cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,255),2)
    #cv.drawContours(frame1, contours,-1, (0,255,0), 2)

    cv.imshow('Video', frame1)
    frame1=frame2
    ret, frame2=cam.read()

    if cv.waitKey(1)==27:
        break


cam.release()
