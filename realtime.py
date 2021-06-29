# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 14:02:49 2021

@author: va
"""

import cv2
import numpy as np
import math
import copy
from maintry import *
import utilstry

old_sudoku = None
    
# Load and set up Camera
cap = cv2.VideoCapture(0)
# cap.set(3, 1280)    # HD Camera
# cap.set(4, 720)


while(True):
    ret, frame = cap.read() # Read the frame
       
    # # frame1 = frame.copy()  
    # sudoku_frame = helper(frame,old_sudoku)
    
    # if(not sudoku_frame): 
    #     print("hello")
    #     cv2.imshow("display",frame)
    # else:
    #     cv2.imshow("display",sudoku_frame)
        
    cv2.imshow("display",frame)   
    if cv2.waitKey(1) == ord('q'):   
        break


cap.release()
cv2.destroyAllWindows()
