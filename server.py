import re
import imaplib
import smtplib
import datetime
import email
import email.header
import email.mime.multipart
import Tkinter, tkSimpleDialog
from pygame import mixer
import speech_recognition as sr
from bs4 import BeautifulSoup
from subprocess import call



mixer.init()
r = sr.Recognizer()


class EmailServer():




   def login_server(self,email,pwd,adress,port):
      try:
         
         self.email = email
         self.pwd = pwd
         self.adress = adress
         self.port = port
         print self.email
         print self.pwd
         self.M=imaplib.IMAP4_SSL(self.adress,self.port)
         status, summary = self.M.login(self.email,self.pwd)
         print "Login Success"
      except imaplib.IMAP4.error:
         print "errer"


   def mailbody(self,msg):
      if msg.is_multipart():
         for payload in msg.get_payload():
             # if payload.is_multipart(): ...
             body = (
                 payload.get_payload(decode=True)
                 .split(msg['from'])[0]
                 .split('\r\n\r\n2015')[0]
             )
             return body
      else:
         body = (
             msg.get_payload(decode=True)
             .split(msg['from'])[0]
             .split('\r\n\r\n2015')[0]
         )
         return body
        
            
   

   def emailnumber(self):
      status, count = self.M.search(None,"All")
      if status == 'OK':
         list = count[0]
      return len(list)


   def inbox(self):
      return self.M.select("Inbox")


   def returnid(self):
      status, count = self.M.search(None,"UNSEEN")
      if status == 'OK':
         list = count[0].split()
      return list

   def get_speech(self): 
      with sr.Microphone() as source:
         audio = r.listen(source)
         try:
            recon=r.recognize_google(audio)
            print recon
            return recon
         except:
            recon=r.recognize_sphinx(audio)
            call(["espeak","-s","160","i can't understand what you said, please say again"])
            return self.get_speech()   



   def import_contact(self):
      status, count = self.M.search(None,"SEEN")
      if status == 'OK':
         list = count[0].split()
         for id in range(len(list),1,-1):
            status, data = self.M.fetch(list[id-1],'(RFC822)')
            self.raw_email = data[0][1]
            self.email_message = email.message_from_string(self.raw_email)
            self.to = email.header.decode_header(self.email_message['From'])[0]
           

            print email.utils.parseaddr(self.to[0])[1]+ " | " + email.utils.parseaddr(self.to[0])[0]






   def access_server(self,listid,nb):
         self.nb = self.emailnumber() - nb
         call(["espeak","-s","160","You have "+str(self.nb)+ " new email"])
         call(["espeak","-s","160","and "+str(len(listid))+" unread old email"])
         call(["espeak","-s","160","do you want me to read them for you?"])
         speech = self.get_speech()
         if "yes" or "yeah" in speech.lower():
            id = 0
            for id in range(len(listid)):
               status, data = self.M.fetch(listid[id],'(RFC822)')
               self.raw_email = data[0][1]
               self.email_message = email.message_from_string(self.raw_email)
               self.fro = email.header.decode_header(self.email_message['From'])[0]
               self.sub = email.header.decode_header(self.email_message['Subject'])[0]
               print "---------------  " +str(id)+ " -----------------------"
               call(["espeak","-s","160","You recieved email from   "+ email.utils.parseaddr(self.fro[0])[0]])
               call(["espeak","-s","160","the email subject is about   " +self.sub[0]])
               call(["espeak","-s","160","Say read to read this email, or next to go to the next one"]) 
               speech = self.get_speech()
               if "read" in speech.lower() or "reed" in speech.lower():              
                  text = BeautifulSoup(self.mailbody(self.email_message), "lxml")
                  text_clean = re.sub(r'^https?:\/\/.*[\r\n]*', '', text.get_text(), flags=re.MULTILINE)
                  print text_clean
                  call(["espeak","-s","160","the sender tell you " + text_clean ])
               else:
                  id =+1
         else:
            break




