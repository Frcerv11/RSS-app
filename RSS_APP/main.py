from Tkinter import *
import tkFont
import auth
from login import LoginWindow
from app import MainWindow

class Main(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.loginWindow = LoginWindow(self.master,self)

    def initApp(self,currentUser,currentPassword):
        self.master.withdraw()
        self.mainWindow = Toplevel(self.master)
        rssApp = MainWindow(self.mainWindow)
        print(currentUser,currentPassword)

# Only run if program is executed in this file
def main():
    root = Tk()
    app = Main(root)
    root.mainloop()

if __name__ == "__main__":
    main()
