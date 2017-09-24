#! /usr/bin/env python

import os
from function import function
import speech_recognition as sr
from server import EmailServer
from pygame import mixer
from subprocess import call
from send import SendEmail
from detect import face_rec
from face import face_detect
from trainer import face_train





      


mixer.init()
r = sr.Recognizer()


with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)




while True:


   def get_speech(): 
      with sr.Microphone() as source:
         audio = r.listen(source)
         try:
            recon=r.recognize_google(audio)
            print recon
            return recon
         except:
            recon=r.recognize_sphinx(audio)
            call(["espeak","-s","160","i can't understand what you said, please say again"])
            return get_speech()

   def import_con():
      call(["espeak","-s","160","Do you want to import your contact?"])
      speech = get_speech()
      if "yes" in speech.lower():
         conn.import_contact()
      
   rec = face_rec()
   if rec.rec() != "0":
      computername = rec.rec()
   else:
      call(["espeak","-s","160","This is Your First Time using me"])
      call(["espeak","-s","160","Do you want to create a new account?"])
      speech = get_speech()
      if "yes" in speech.lower() or "yeah" in speech.lower():
         det = face_detect()
         det.new()
         server_ad = function()
         server_ad.add_user()
         train = face_train()
         train.train() 
         rec = face_rec() 
         computername = rec.rec()
      else:
         break    


   call(["espeak","-s","160","Hello "+computername+" can i help you?"])   

   speech = get_speech()
   if "email" in speech.lower():
      try: 
         server = function()
         if server.get_last_id() == "0":
            id=1
         else:
            id= server.get_last_id()

         email,passwd = server.get_login_passwd(id)
         email_server = email.split("@")[1].split(".")[0]
         adress,port = server.GetServer(email_server,'imap')
         print adress
         print port
         call(["espeak","-s","160","ok i will check it for you"])
         conn = EmailServer()
         conn.login_server(email.rstrip(),passwd,adress,port)
         conn.inbox()
         import_con()
         listid = conn.returnid()
         nb = server.get_email_nb(id)
         up_nb = conn.emailnumber()
         server.update_email_nb(id,up_nb)
         conn.access_server(listid,nb)
         
      except sr.UnknownValueError:
         call(["espeak","there is errer"])


   elif "send" in speech.lower() or "reply" in speech.lower() or "response" in speech.lower():
      try:
         call(["espeak","-s","160","you want to send email?"])
         speech = get_speech()
         if "yes" in speech.lower() or "yeah" in speech.lower():
            call(["espeak","-s","160","ok i will send email for you"])
            server_ad = function()
            adress,port = server_ad.GetServer('gmail','smtp')
            name,email,passwd = server_ad.get_login_passwd(2)
            call(["espeak","-s","160","what's the subject of this email?"])
            sub = get_speech()
            call(["espeak","-s","160","what you want to say to him?"])
            body = get_speech()
            call(["espeak","-s","160","to who you want to send it?"])
            to_txt = get_speech()
            to = server_ad.get_to(2,to_txt)
            send = SendEmail()
            send.Send(email.rstrip(),passwd,sub,body,to,adress,port)
      except sr.UnknownValueError:
         call(["espeak","-s","160","there is errer"])



   elif "add" in speech.lower() and "server" in speech.lower():
      try:
         call(["espeak","-s","160","are you sure you want to add new server?"])
         speech = get_speech()
         if "yes" in speech.lower():
            server_ad = function()
            server_ad.AddServer()

      except sr.UnknownValueError:
         call(["espeak","-s","160","there is errer"])





   elif "no" in speech.lower() or "quit" in speech.lower() or "close" in speech.lower():
      call(["espeak","-s","160","ok Good By."])
      call(["espeak","-s","160","if you need me please run me any time"])
      break


   


