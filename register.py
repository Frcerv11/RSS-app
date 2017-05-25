from Tkinter import *
import tkFont
import auth

#Registration Window
class RegisterWindow(Frame):
    def __init__(self,master,controller):
        Frame.__init__(self,master)
        self.customFont = tkFont.Font(family='Helvetica', size=15, weight='bold')
        self.controller = controller
        self.master = master
        self.initUI()

    def initUI(self):
        self.frame = Frame(self.master, width=100, height = 600)
        # GUI setup
        self.title = Label(self.frame)
        self.title['font'] = self.customFont
        self.title['text'] = 'Register'
        self.title.pack(anchor=CENTER)

        self.uNameText = Label(self.frame)
        self.uNameText['text'] = 'Set Username'
        self.uNameText.pack(anchor=W)

        self.uNameEntry = Entry(self.frame)
        self.uNameEntry.pack(anchor=W)

        self.passwordText = Label(self.frame)
        self.passwordText['text'] = 'Set password'
        self.passwordText.pack(anchor=W)

        self.passwordEntry = Entry(self.frame)
        self.passwordEntry.pack(anchor=W)

        self.alert = Label(self.frame)
        self.alert.pack(anchor=CENTER)

        self.button = Button(self.frame)
        self.button['text'] = 'Register'
        self.button['command'] = self.processUser
        self.button.pack(anchor=CENTER)

        self.button = Button(self.frame)
        self.button['text'] = 'Back to Login'
        self.button['command'] = self.closeWindow
        self.button.pack(anchor=CENTER)

        self.frame.grid(row=0, column=0, padx=100, pady=25)

    # Process and checks if user registration is successful 
    def processUser(self):
        if(auth.saveUser(self.uNameEntry.get(),self.passwordEntry.get())):
             self.alert['text'] = 'Registration Successful'
        else:
            self.alert['text'] = 'Registration Unsuccessful'

    def closeWindow(self):
        self.master.withdraw()
        self.controller.initr()



