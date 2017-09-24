import os
import cv2
import numpy as np
from PIL import Image


class face_train():

   def __init__(self):
      self.recognizer=cv2.createLBPHFaceRecognizer();
      self.path='dataSet'
   
   

   def getImagesId(self,path):
      imagePaths=[os.path.join(self.path,f) for f in os.listdir(self.path)]
      faces=[]
      IDs=[]
      for imagePath in imagePaths:
         faceImg=Image.open(imagePath).convert('L');
         faceNp=np.array(faceImg,'uint8')
         ID= int(os.path.split(imagePath)[-1].split('.')[1])
         faces.append(faceNp)
         print ID
         IDs.append(ID)
         cv2.imshow("training",faceNp)
         cv2.waitKey(10)
      return IDs,faces

   def train(self):
      Ids,faces=self.getImagesId(self.path)
      self.recognizer.train(faces,np.array(Ids))
      self.recognizer.save('recognizer/trainingData.yml')
      cv2.destroyAllWindows()
   



