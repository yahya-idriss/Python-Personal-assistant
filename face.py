#!/usr/bin/env python

import os
import cv2
import numpy as np
import sqlite3
from function import function


class face_detect():

   def __init__(self):
      self.cam = cv2.VideoCapture(0)
      self.detector=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
      server = function()
      self.id = server.get_last_id()

   

   def new(self):
      Id=str(self.id+1)
      sampleNum=0

      while(True):
         ret, img = self.cam.read()
         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         faces = self.detector.detectMultiScale(gray, 1.3, 5)
         for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            sampleNum=sampleNum+1
            cv2.imwrite("dataSet/User."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w]) #
            cv2.imshow('frame',img)
         if cv2.waitKey(100) & 0xFF == ord('q'):
            break
         elif sampleNum>20:
            break
      self.cam.release()
      cv2.destroyAllWindows()

