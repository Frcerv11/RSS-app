from Tkinter import *
from bs4 import BeautifulSoup
import feedparser
import auth
class MainWindow(Frame):
    def __init__(self, parent,controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        self.sites = {}  
        self.articles = {}
        self.username = self.controller.getUserInfo()[0]
        self.password = self.controller.getUserInfo()[1]
        self.urls = auth.getFeedUrls(self.username,self.password)
        for item in self.urls:
            self.storeUrls(item)
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
        self.entry = Entry(feedEntry)
        self.entry.pack(side=LEFT)
        self.entryInput = Button(feedEntry, text = "+", command = lambda: auth.storeUrl(self.entry.get()))
        self.entryInput.pack(side=RIGHT)
        feedEntry.pack(expand=True)

        self.listbox = Listbox(frame1)
        for key, value in self.sites.iteritems():
            self.listbox.insert(END, key)
        self.listbox.bind('<<ListboxSelect>>',self.displayArticles)
        self.listbox.pack(expand=True,fill=X)

        self.button = Button(frame1)
        self.button['text'] = 'Unsubscribe'
        self.button.pack(fill=X)

        frame2 = Frame(self)
        frame2.pack(side=RIGHT,fill=BOTH)

        self.listbox2 = Listbox(frame2,width=60, height=5)
        self.listbox2.bind('<<ListboxSelect>>',self.displayArticleContent)
        self.listbox2.pack()

        self.listbox3 = Text(frame2,width=60, height=10)

        self.listbox3.pack()

    def storeUrls(self,url):
        feeds = feedparser.parse(url)
        self.sites[feeds['feed']['title']] = url

    def displayArticles(self,evt):
        self.listbox2.delete(0, END)
        selection=str((self.listbox.get(self.listbox.curselection())))
        siteUrl = self.sites[selection]
        feads = feedparser.parse(siteUrl)
        for entry in feads.entries:
            value = feads.url
            key = entry.title
            self.listbox2.insert(END,entry.title)
            self.articles[key] = value
        

    def displayArticleContent(self,evt):
        self.listbox3.delete('1.0', END)
        selection=str((self.listbox2.get(self.listbox2.curselection())))
        selectionIndex=self.listbox2.curselection()
        feads = feedparser.parse(self.articles[selection])
        # print(feads.entries[selectionIndex[0]].summary)
        temp = feads.entries[selectionIndex[0]].title + "\n"
        temp += feads.entries[selectionIndex[0]].link + "\n" 
        temp += feads.entries[selectionIndex[0]].description + "\n"
        temp += feads.entries[selectionIndex[0]].id

        soup = BeautifulSoup(temp,"html.parser")
        print(soup.get_text())
        self.listbox3.insert(END, soup.get_text())
        # selection=str((self.listbox2.get(self.listbox2.curselection())))
        # page = urllib2.urlopen(self.articles[selection])
        # print(page)
        # soup = BeautifulSoup(page, "html.parser")
        # for i in soup.body:
        #     print(i)