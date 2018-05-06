import tkinter as tk
from tkinter import Entry, Label


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        # self.source_widgets()
        self.create_widgets()

    # def source_widgets(self):
    #     self.source_label = tk.Label(self, text='Source Folder')
    #     self.source_label.pack(side="top")

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


class SourceApp(tk.LabelFrame):
    def __init__(self, master=None):
        super().__init__(master, text='Source')
        self.pack()

        label = Label(self, text='Source Folder')
        label.pack(side="top")
        path = Entry(self)
        path.pack(side='top')


root = tk.Tk()
app = Application(master=root)
source = SourceApp(master=app)
app.mainloop()
