#!/usr/bin/env python

import os
import cv2
import numpy as np
import sqlite3

class face_rec():


   def getProfile(self,id):
      conn=sqlite3.connect("email_sys")
      cmd="select Name from User where ID=" +str(id)
      cursor=conn.execute(cmd)   
      data = cursor.fetchone()
      conn.close()
      return data
     


   def rec(self):
      if os.path.isfile('recognizer/trainingData.yml') is False:
         return "0"
      rec=cv2.createLBPHFaceRecognizer();
      rec.load("recognizer/trainingData.yml")
      detector=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
      cam = cv2.VideoCapture(0)
      font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX,1,1,0,1,1)
      while(True):
         ret, img = cam.read()
         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         faces = detector.detectMultiScale(gray, 1.3, 5)
         for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            id,conf=rec.predict(gray[y:y+h,x:x+w])
            profile=self.getProfile(id)
            if( profile!=None):
               return profile[0]
            else:
               return "0"
         cv2.imshow('frame',img)
         break
      cam.release()
      cv2.destroyAllWindows()


