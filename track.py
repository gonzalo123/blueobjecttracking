import cv2
import numpy

cam = cv2.VideoCapture(0)
kernel = numpy.ones((5 ,5), numpy.uint8)

while (True):
    ret, frame = cam.read()
    rangomax = numpy.array([255, 50, 50]) # B, G, R
    rangomin = numpy.array([51, 0, 0])
    mask = cv2.inRange(frame, rangomin, rangomax)
    # reduce the noise
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    x, y, w, h = cv2.boundingRect(opening)

    cv2.rectangle(frame, (x, y), (x+w, y + h), (0, 255, 0), 1)
    cv2.circle(frame, (x+w/2, y+h/2), 5, (0, 0, 255), -1)

    cv2.imshow('camera', frame)

    k = cv2.waitKey(1) & 0xFF

    if k == 27:
        break

