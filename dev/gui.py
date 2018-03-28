from tkinter import *
import subprocess

class Application(Frame):

    def upload(self):
        val = "lala"
        # subprocess.run(["git","submodule","add", "../files"], shell=True)
        subprocess.run(["git", "add","-A", "."], shell=True)
        subprocess.run(["git", "commit", "-m", val], shell=True)
        subprocess.run(["git", "push"])
        subprocess.run(["cls"])
        # return
    def download(self):
        subprocess.run(["git","pull"])
        # return

    def createWidgets(self):
        # upload button
        self.UPLOAD = Button(self)
        self.UPLOAD["text"] = "UPLOAD"
        self.UPLOAD["command"] =  self.upload
        self.UPLOAD.pack({"side": "left"})

        # download button 
        self.hi_there = Button(self)
        self.hi_there["text"] = "DOWNLOAD",
        self.hi_there["command"] = self.download
        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()