from Tkinter import *
import tkFont
import auth
from login import LoginWindow
from register import RegisterWindow
from app import MainWindow

class Main(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        #Display login w-indow
        self.loginWindow = LoginWindow(self.master,self)
    #
    def initApp(self,currentUser,currentPassword):
        self.username = currentUser
        self.password = currentPassword
        self.loginWindow.destroy()
        self.master.withdraw()
        self.mainWindow = Toplevel(self.master)
        rssApp = MainWindow(self.mainWindow,self)

    def getUserInfo(self):
        return self.username,self.password

    def initr(self):
        self.loginWindow = Toplevel(self.master)
        LoginWindow(self.loginWindow,self)

    def loginToRegister(self):
        self.loginWindow.destroy()
        self.master.withdraw()
        self.mainWindow = Toplevel(self.master)
        registerWindow = RegisterWindow(self.mainWindow,self)

# Only run if program is executed in this file
def main():
    root = Tk()
    app = Main(root)
    root.mainloop()

if __name__ == "__main__":
    main()