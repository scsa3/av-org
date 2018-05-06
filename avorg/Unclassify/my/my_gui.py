# !/usr/bin/python3
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pathlib import Path


def test():
    file_path = filedialog.askdirectory()
    source_entry.delete(0, END)
    source_entry.insert(0, file_path)
    source_path = Path(file_path)
    search_content.delete(0, END)
    for i in source_path.glob('**/*'):
        if i.is_file:
            search_content.insert(END, i)
            print(i)


def av_filter(self, path=Path('./KodiTest')):
    pattern = re.compile(r'[a-zA-Z]{2,4}-[0-9]{3}\.(avi|mp4|mpg|mkv)')
    av_list = list()
    for p in path.glob('**/*.*'):
        # print(p.name)
        result = self.pattern.search(p.name)
        if result and p.is_file():
            # print(p)
            av_list.append(p)
    return av_list


class MyTest:
    def my_print():
        print('my print')


top = Tk()
source_label = Label(top, text='Source Folder')
source_entry = Entry(top, width=50)
source_button = Button(top, text='Select', command=MyTest.my_print)
source_path = Path()

some_label = Label(top, text='something')
search_content = Listbox(top, selectmode='extended')
# for line in range(100):
#     search_content.insert(END, "This is line number " + str(line))
search_button = Button(top, text='Search', command=test)

target_label = Label(top, text='Target Folder')
target_entry = Entry(top, width=50)
target_button = Button(top, text='Select', command=test)

#
source_label.grid(row=0, column=0)
source_entry.grid(row=0, column=1)
source_button.grid(row=0, column=2)
some_label.grid(row=1, column=0)
search_content.grid(row=1, column=1, ipadx=100, ipady=100)
search_button.grid(row=1, column=2)
target_label.grid(row=2, column=0)
target_entry.grid(row=2, column=1)
target_button.grid(row=2, column=2)

top.mainloop()
