import sqlite3
import Tkinter, tkSimpleDialog


class function():


   def __init__(self):
      self.root = Tkinter.Tk()
      self.root.withdraw()





   def GetServer(self,Name,Type):
      self.conn=sqlite3.connect('email_sys')
      self.cmd="select Adress,Port from Servers where Name like '%"+str(Name) +"%' AND Type='"+str(Type)+"'"
      self.cursor=self.conn.execute(self.cmd)
      data=self.cursor.fetchone()
      for row in data:
         return data
      self.conn.close()



   def AddServer(self):
      self.Name = str(tkSimpleDialog.askstring("Name", "Enter Server Name:"))
      self.Type = str(tkSimpleDialog.askstring("Type", "Enter Server Type (imap / smtp) :", show='*'))
      self.Adress = str(tkSimpleDialog.askstring("Adress", "Enter Server Adress:"))
      self.Port = tkSimpleDialog.askstring("Port", "Enter Server Port:")
      print self.Name
      print self.Port
      self.conn=sqlite3.connect("email_sys")
      cmd="INSERT INTO Servers VALUES('"+self.Name+"','"+self.Type+"','"+self.Adress+"',"+self.Port+")"
      self.cursor=self.conn.execute(cmd)
      self.conn.commit()
      self.conn.close()




   def get_login_passwd(self,ID):
      self.ID = str(ID)
      self.conn=sqlite3.connect('email_sys')
      self.cmd="select Email,Password from User where ID="+self.ID
      self.cursor=self.conn.execute(self.cmd)
      data=self.cursor.fetchone()
      for row in data:
         return data
      self.conn.close()


   def get_to(self,ID,text):
      self.text = text
      self.ID = str(ID)
      self.conn=sqlite3.connect('email_sys')
      for word in self.text.split():
         self.cmd="select Email from Contact where Name like '%"+str(word) +"%' AND ID="+self.ID
         self.cursor=self.conn.execute(self.cmd)
         data=self.cursor.fetchone()
         for row in data:
            return data
         self.conn.close()
            
 





   def add_user(self):
      self.name = str(tkSimpleDialog.askstring("Name", "Enter Your Name:"))
      self.email = str(tkSimpleDialog.askstring("Email", "Enter Your Email Adress :"))
      self.password = str(tkSimpleDialog.askstring("Password", "Enter Your Password:", show='*'))
      self.conn=sqlite3.connect("email_sys")
      cmd="INSERT INTO User (Name,Email,Password) VALUES('"+self.name+"','"+self.email+"','"+self.password+"')"
      self.cursor=self.conn.execute(cmd)
      self.conn.commit()
      self.conn.close()

      


   def add_contact(self,ID,Email):
      self.conn=sqlite3.connect('email_sys')
      cmd="INSERT INTO Contact VALUES('"+self.ID+"','"+self.email+"')"
      self.cursor=self.conn.execute(cmd)
      self.conn.commit()
      self.conn.close()



   def update_email_nb(self,ID,nb):
      self.ID = str(ID)
      self.nb = str(nb)
      self.conn=sqlite3.connect("email_sys")
      cmd="UPDATE User SET email_nb = '"+self.nb+"' where ID = " +self.ID 
      self.cursor=self.conn.execute(cmd)
      self.conn.commit()
      self.conn.close()

   def get_email_nb(self,ID):
      self.ID = str(ID)
      self.conn=sqlite3.connect('email_sys')
      self.cmd="select email_nb from User where ID="+self.ID
      self.cursor=self.conn.execute(self.cmd)
      data=self.cursor.fetchone()[0]
      if data == None:
         return 0
      else:
         return data
      self.conn.close()

   def get_last_id(self):
      self.conn=sqlite3.connect('email_sys')
      self.cursor = self.conn.execute('SELECT max(id) FROM User')
      self.max_id = self.cursor.fetchone()[0]
      if self.max_id == None:
         return 0
      else:
         return self.max_id
      self.conn.close()


