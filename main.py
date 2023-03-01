import cv2
from cv2 import aruco
from utils import ARUCO_DICT, aruco_display
import numpy as np
import time

class MarkSearch :

    dict_aruco = aruco.Dictionary_get(aruco.DICT_4X4_50)
    parameters = aruco.DetectorParameters_create()

    def __init__(self):
        image = cv2.imread("image.jpg")
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray1 = cv2.resize(gray, (640, 480))
        (corners, ids, rejectedImgPoints) = cv2.aruco.detectMarkers(gray1, dict_aruco, parameters=parameters)
        print(corners,"\n\n")
        print(ids,"\n\n")
        print(rejectedImgPoints,"\n\n")
        detected_markers = aruco_display(corners, ids, rejectedImgPoints, image)
        cv2.imshow("Image", detected_markers)
        cv2.imwrite("output_sample.png",detected_markers)
        cv2.waitKey(0)
        
if __name__ == "__main__" :

    dict_aruco = aruco.Dictionary_get(aruco.DICT_4X4_50)
    parameters = aruco.DetectorParameters_create()

    ### --- parameter --- ###
    cameraID = 0
    cam0_mark_search = MarkSearch()




    
