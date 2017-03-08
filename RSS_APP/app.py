from Tkinter import *
class MainWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("Review")
        self.pack(fill=BOTH, expand=True)
        
        frame1 = Frame(self)
        frame1.pack(side=LEFT,fill=BOTH)
        
        lbl1 = Label(frame1, text="Welcome")
        lbl1.pack()           
       
        self.button = Button(frame1)
        self.button['text'] = 'Sign Out'
        self.button.pack()

        feedEntry = Frame(frame1)
        entry1 = Entry(feedEntry)
        entry1.pack(side=LEFT)
        self.button = Button(feedEntry)
        self.button['text'] = '+'
        self.button.pack(side=RIGHT)
        feedEntry.pack(expand=True)

        listbox = Listbox(frame1)
        listbox.insert(END, "Reddit")
        for item in ["PythonInfo Wiki", "BBC", "TechCrunch", "Reuters","DIGG"]:
            listbox.insert(END, item)
        listbox.pack(expand=True,fill=X)
        

        self.button = Button(frame1)
        self.button['text'] = 'Unsubscribe'
        self.button.pack(fill=X)


        frame2 = Frame(self)
        frame2.pack(side=RIGHT,fill=BOTH)

        listbox = Listbox(frame2,width=60, height=5)
        # listbox.insert(END, "Reddit")
        for item in ["PythonInfo Wiki", "BBC", "TechCrunch", "Reuters","DIGG"]:
            listbox.insert(END, item)
        listbox.pack()

        listbox = Listbox(frame2,width=60, height=10)
        for item in ["PythonInfo Wiki", "BBC", "TechCrunch", "Reuters","DIGG"]:
            listbox.insert(END, item)
        listbox.pack()