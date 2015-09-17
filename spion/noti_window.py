from Tkinter import Tk, BOTH
from Tkinter import Frame, Button 
import os
        
class Notif_win(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
    
    def openReport(self):
        os.startfile('C:\\Python26\\Lib\\site-packages\\Spion\\report.html')
        self.master.destroy()
    
        
    def initUI(self):
      
        self.parent.title("You have new notifications - Spion")

        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="View Notifications >>",
            command=self.openReport)
        quitButton.place(x=90, y=30)

