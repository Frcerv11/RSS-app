from Tkinter import *
import tkFont
import auth

#Login Window
class Login(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        customFont = tkFont.Font(family='Helvetica', size=15, weight='bold')
        
        self.title = Label(self)
        self.title['font'] = customFont
        self.title['text'] = 'RSS APP'
        self.title.pack(anchor=CENTER)

        self.uNameText = Label(self)
        self.uNameText['text'] = 'Username'
        self.uNameText.pack(anchor=W)

        self.uNameEntry = Entry(self)
        self.uNameEntry.pack(anchor=W)

        self.passwordText = Label(self)
        self.passwordText['text'] = 'Password'
        self.passwordText.pack(anchor=W)

        self.passwordEntry = Entry(self)
        self.passwordEntry.pack(anchor=W)
        
        self.button = Button(self)
        self.button['text'] = 'Login'
        self.button['command'] = self.action
        self.button.pack(anchor=CENTER)

        self.alert = Label(self)
        self.alert.pack(anchor=CENTER)

    #Passes user input (username and password) to processCredentials function in auth module. The processCredentials
    #function returns true or false. 
    def action(self):
        if auth.processCredentials(self.uNameEntry.get(),self.passwordEntry.get()):
            self.alert['text'] = 'Welcome'
        else:
            self.alert['text'] = 'Login failed'

root = Tk()

frame = Frame(root, width=100, height = 600)
frame.grid(row=0, column=0, padx=100, pady=25)
frame.update()

loginForm = Login(frame)
loginForm.pack()

mainloop()
