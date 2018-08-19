"""
* AV Finder: Find out all av in some folder
    * Folder Path Text:
    * Folder Select Button:
    * File List:
"""
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.source_entry = tk.Entry(self, width=50)
        self.pack()
        self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.source_button = tk.Button(self, text='Select')
        self.source_label = tk.Label(self, text='Source Folder')

        self.create_widgets()

    def create_widgets(self):

        self.quit.pack(side="bottom")
        self.source_label.pack()
        self.source_entry.pack()
        self.source_button.pack()


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
