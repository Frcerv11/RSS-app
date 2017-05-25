from Tkinter import *
from bs4 import BeautifulSoup
import feedparser
import auth
from login import LoginWindow


class style:
   BOLD = '\033[1m'
   END = '\033[0m'

class MainWindow(Frame):
    def __init__(self, parent,controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        self.sites = {}
        self.articles = {}
        # Get username and password inputted in login screen
        self.username = self.controller.getUserInfo()[0]
        self.password = self.controller.getUserInfo()[1]

        #Get list of users' rss feed urls
        self.urls = auth.getFeedUrls(self.username,self.password)

        #Parse urls through FeedParser
        for item in self.urls:
            self.storeUrls(item)

        self.initUI()
 
    #Gets called on after entries are removed or added
    def updateEntries(self):
        self.urls = []
        self.sites = {}
        self.urls = auth.getFeedUrls(self.username,self.password)
        for item in self.urls:
            self.storeUrls(item)

    #Refresh list box component 
    def updateListbox(self):
        self.titleList.delete(0, END)
        for key, value in self.sites.iteritems():
            self.titleList.insert(END, key)

    #App GUI
    def initUI(self):

        self.parent.title("RSS APPLICATION")
        self.pack(fill=BOTH, expand=True)
        
        frame1 = Frame(self)
        frame1.pack(side=LEFT,fill=BOTH)
        
        lbl1 = Label(frame1)
        lbl1['text'] = ("Welcome " +   self.username).title();
        lbl1.pack()           
        
       

        self.button = Button(frame1,height=2)
        self.button['text'] = 'Sign Out'
        self.button['command'] = self.closeWindow
        self.button.pack()

        feedEntry = Frame(frame1)
        self.entry = Entry(feedEntry)
        self.entry.pack(side=LEFT)
        self.entryInput = Button(feedEntry)
        self.entryInput['text'] = "+"
        self.entryInput['command'] = self.storeEntry
        self.entryInput.pack(side=RIGHT)
        feedEntry.pack(expand=True)

        self.titleList = Listbox(frame1)
        self.updateListbox()
        self.titleList.bind('<<ListboxSelect>>',self.displayArticles)
        self.titleList.pack(expand=True,fill=X)

        self.unsubButton = Button(frame1)
        self.unsubButton['text'] = 'Unsubscribe'
        self.unsubButton['command'] = self.removeEntry
        self.unsubButton.pack(fill=X)

        frame2 = Frame(self)
        frame2.pack(side=RIGHT,fill=BOTH)
        self.articleList = Listbox(frame2,width=60, height=5)
        self.articleList.bind('<<ListboxSelect>>',self.displayArticleContent)
        self.articleList.pack()

        self.contentText = Text(frame2,width=60, height=10)

        self.contentText.pack()

    #Close this window and switch to login window
    def closeWindow(self):
        self.parent.withdraw()
        self.controller.initr()

    #Save RSS feed url and if it processes successfully update application 
    def storeEntry(self):
        if(auth.saveEntry(self.username,self.password,self.entry.get())):
            self.updateEntries()
            self.updateListbox()
        self.entry.delete(0, 'end')
    
    #Remove RSS feed url and if it processes successfully update application 
    def removeEntry(self):
        selection=str((self.titleList.get(self.titleList.curselection())))
        siteUrl = self.sites[selection]
        if(auth.deleteEntry(self.username,self.password,siteUrl)):
            self.updateEntries()
            self.updateListbox()
        self.entry.delete(0, 'end')


    def storeUrls(self,url):
        feeds = feedparser.parse(url)
        self.sites[feeds['feed']['title']] = url

    def displayArticles(self,evt):
        self.articleList.delete(0, END)
        selection=str((self.titleList.get(self.titleList.curselection())))
        siteUrl = self.sites[selection]
        feads = feedparser.parse(siteUrl)
        for entry in feads.entries:
            value = feads.url
            key = entry.title
            self.articleList.insert(END,entry.title)
            self.articles[key] = value

    def displayArticleContent(self,evt):
        self.contentText.delete('1.0', END)
        selection=(self.articleList.get(self.articleList.curselection()))
        selection.encode('utf-8')
        selectionIndex=self.articleList.curselection()
        feads = feedparser.parse(self.articles[selection])
        temp =  "Title: " + feads.entries[selectionIndex[0]].title + "\n"
        temp += "Description: " + feads.entries[selectionIndex[0]].description + "\n" 
        temp += "Link: " + feads.entries[selectionIndex[0]].link
        soup = BeautifulSoup(temp,"html.parser")
        self.contentText.insert(END, soup.get_text())
