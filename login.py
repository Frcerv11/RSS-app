from Tkinter import *
import tkFont
import auth

#Login Window
class LoginWindow(Frame):
    def __init__(self,master,controller):
        Frame.__init__(self,master)
        self.customFont = tkFont.Font(family='Helvetica', size=15, weight='bold')
        self.controller = controller
        self.master = master
        self.initUI()

    def initUI(self):
        self.frame = Frame(self.master, width=100, height = 600)

        self.title = Label(self.frame)
        self.title['font'] = self.customFont
        self.title['text'] = 'RSS APP'
        self.title.pack(anchor=CENTER)
        
        self.uNameText = Label(self.frame)
        self.uNameText['text'] = 'Username'
        self.uNameText.pack(anchor=W)

        self.uNameEntry = Entry(self.frame)
        self.uNameEntry.pack(anchor=W)

        self.passwordText = Label(self.frame)
        self.passwordText['text'] = 'Password'
        self.passwordText.pack(anchor=W)

        self.passwordEntry = Entry(self.frame,show="*")
        self.passwordEntry.pack(anchor=W)
        
        self.button = Button(self.frame)
        self.button['text'] = 'Login'
        self.button['command'] = self.login
        self.button.pack(anchor=CENTER)

        self.button = Button(self.frame)
        self.button['text'] = 'Register'
        self.button['command'] = self.register
        self.button.pack(anchor=CENTER)

        self.alert = Label(self.frame)
        self.alert.pack(anchor=CENTER)

        self.frame.grid(row=0, column=0, padx=100, pady=25)

    #Passes user input (username and password) to processCredentials function in auth module. The processCredentials
    #function returns true or false. 
    def login(self):
        if auth.processCredentials(self.uNameEntry.get(),self.passwordEntry.get()):
            self.alert['text'] = 'Welcome'
            self.controller.initApp(self.uNameEntry.get(),self.passwordEntry.get())
        else:
            self.alert['text'] = 'Login failed'

    def register(self):
        self.controller.loginToRegister()




