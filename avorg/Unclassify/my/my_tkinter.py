import tkinter as tk
from tkinter import filedialog


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.select_file = tk.Button(self)
        self.select_file["text"] = "file chooser"
        self.select_file["command"] = self.file_chooser
        self.select_file.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def file_chooser(self):
        filedialog.askdirectory()
        return 123


root = tk.Tk()
app = Application(master=root)
app.mainloop()
