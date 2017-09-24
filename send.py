import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText



class SendEmail():


   def Send(self,name,passwd,subject,body,to,server,port):
      self.name = name
      self.passwd = passwd

      self.server = server
      self.port = port

      headers = "\r\n".join([
          "from: " + self.name,
          "subject: " + subject,
          "to: " + to[0],
          "mime-version: 1.0",
          "content-type: text/html"
      ])

      content = headers + "\r\n\r\n" + str(body)
      self.s = smtplib.SMTP(self.server,self.port)
      self.s.ehlo()
      self.s.starttls()
      self.s.ehlo()
      self.s.login(self.name,self.passwd)
      if self.s.sendmail(name,to,content):
         return "sent"
         self.s.quit()
      else:
         return "errer"





