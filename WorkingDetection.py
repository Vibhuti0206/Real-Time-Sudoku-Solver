# -*- coding: utf-8 -*-
"""
Created on Sun May  2 02:10:10 2021

@author: va
"""


import cv2
from maintry import *
import pickle
model = pickle.load(open('knn.sav', 'rb'))
import warnings
warnings.filterwarnings("ignore","Ignore")
      
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    
    sudoku_frame = helper(frame,model)
    
    if(sudoku_frame is None): 
        
        cv2.imshow("Sudoku Solver",frame)
    else:
        cv2.imshow("Sudoku Solver",sudoku_frame)
        
    c = cv2.waitKey(1)
    if c == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

