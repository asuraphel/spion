import Tkinter
from Tkinter import *
from noti_db import Noti_db


urlEntryWidget, patternEntryWidget, disappEntryWidget = None, None, None

def submit():
    global urlEntryWidget
    global patternEntryWidget
    global disappEntryWidget

    db = Noti_db('watch.db')
    
    if urlEntryWidget.get().strip() == "":
        return
    if not patternEntryWidget.get().strip() == "":   
        db.add_url_pattern(urlEntryWidget.get().strip(), patternEntryWidget.get().strip() )
    if not disappEntryWidget.get().strip() == '':
        db.add_url_disapp(urlEntryWidget.get().strip(), disappEntryWidget.get().strip() )

    #code to clear the inputs here
    #urlEntryWidget.delete(0, Tkinter.END) #left to allow entering multiple words for the same URL
    patternEntryWidget.delete(0, Tkinter.END)
    disappEntryWidget.delete(0, Tkinter.END)
    

class SubmitBox(Frame):
     
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()

    def quit(self):
        self.master.destroy()
        
    def initUI(self):
      
        self.parent.title("URL and Pattern Submission Form - Spion")
        
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=1)
        
        self.pack(fill=BOTH, expand=1)

        entryLabel = Label(frame)
        entryLabel["text"] = "URL or base_URL/*:(e.g. http://udacity.com/*)"
        entryLabel.place(x = 15, y = 15)

        entryLabel = Label(frame)
        entryLabel["text"] = "Words or regex to spy appearance of:(e.g. released)"
        entryLabel.place( x = 15, y = 70)

        entryLabel = Label(frame)
        entryLabel["text"] = "Words or regex to spy disappearance of:(e.g. under construction)"
        entryLabel.place( x = 15, y = 125)

        global urlEntryWidget
        urlEntryWidget = Entry(frame)
        urlEntryWidget["width"] = 60
        urlEntryWidget.place(x = 15, y = 40)
        urlEntryWidget.focus_set()

        global patternEntryWidget
        patternEntryWidget = Entry(frame)
        patternEntryWidget["width"] = 60
        patternEntryWidget.place(x = 15, y = 95)

        global disappEntryWidget
        disappEntryWidget = Entry(frame)
        disappEntryWidget["width"] = 60
        disappEntryWidget.place(x = 15, y = 150)
        
        closeButton = Button(self, text="Done", command=self.quit)
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="Submit", command=submit)
        okButton.pack(side=RIGHT)
              

def main():  
    root = Tk()
    root.geometry("400x250+300+300")
    app = SubmitBox(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
