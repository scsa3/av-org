import re
import shutil
import pickle
# import requests
# from lxml import etree
from pathlib import Path
from time import sleep
import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk
import sys


class DMM:
    directories = {'done': Path('./Done'), }
    urls = {'main': 'http://www.dmm.co.jp/',
            'search': 'http://www.dmm.co.jp/digital/videoa/-/detail/=/cid=',
            'search2': 'http://www.dmm.co.jp/search/=/n1=FgRCTw9VBA4GAVhfWkIHWw__/sort=ranking/searchstr=hmgl00149', }
    xpaths = {'name': './/*[@id="performer"]/a',
              'date': './/*[@id="mu"]/div/table/tr/td[1]/table/tr[3]/td[2]',
              'image': './/*[@id="sample-video"]/a', }

    def __init__(self):
        # self.response = requests.get(self.urls['main'])
        # self.number = ''
        # self.name = ''
        # self.date = ''
        pass

    def search(self, av_number):
        self.number = av_number
        dmm_number = av_number.replace('-', '00')
        self.response = requests.get(self.urls['search'] + dmm_number)

    def parse(self):
        tree = etree.HTML(self.response.content)
        self.name = tree.find(self.xpaths['name']).text.strip()
        self.date = tree.find(self.xpaths['date']).text.strip().replace('/', '-')[:10]
        image_url = tree.find(self.xpaths['image']).get('href')
        self.image = requests.get(image_url).content


class R18:
    pass


class Tools:
    pattern = re.compile(r'^[a-zA-Z]{2,4}-[0-9]{3}\.(avi|mp4|mpg|mkv)$')

    def av_filter(self, path=Path('/Users/heweihan/Downloads/')):
        av_list = list()
        for p in path.glob('**/*.*'):
            result = self.pattern.search(p.name)
            if result and p.is_file():
                # print(p)
                av_list.append(p)
        # print(av_list)
        return av_list

    def number_getter(self, file_name='team-100.mp4'):
        av_pattern = re.compile(r'[a-zA-Z]{2,4}-[0-9]{3}')
        result = av_pattern.search(file_name)
        if result:
            return result.group()

    def create_dummy(self, source_path=Path(), target_path=Path()):
        paths = source_path.rglob('*')
        target_path.mkdir(parents=True, exist_ok=True)
        for path in paths:
            relative_path = path.relative_to(source_path)
            print(relative_path)
            if path.is_dir():
                target_path.joinpath(relative_path).mkdir(parents=True)
            elif path.is_file():
                target_path.joinpath(relative_path).touch()

    def create_series_dummy(self, target_path=Path(), start_number=int(), end_number=int()):
        for i in range(start_number, end_number + 1):
            target_path.mkdir(parents=True, exist_ok=True)
            target_path.joinpath('team-{:03d}.mp4'.format(i)).touch()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.quit.pack(side="bottom")

        # self.my = tk.Button(self, text='Search', fg="red", command=Tools().av_filter)
        # self.my.pack(side="bottom")

        self.source_label = tk.Label(self, text='Source Folder')
        self.source_label.pack(side="top")

        self.source_entry = tk.Entry(self, width=50)
        self.source_entry.pack(side="top")
        self.source_entry.delete(0, tk.END)

        self.source_button = tk.Button(self, text='Select', command=self.select_source)
        self.source_button.pack(side="top")

        self.target_label = tk.Label(self, text='Target Folder')
        self.target_label.pack(side="top")

        self.target_entry = tk.Entry(self, width=50)
        self.target_entry.pack(side="top")

        self.target_button = tk.Button(self, text='Select', command=self.select_target)
        self.target_button.pack(side="top")

        self.s = tk.ttk.Separator(self, orient='horizontal')
        self.s.pack(side='top', fill='both')

        self.source_content = tk.Listbox(self, selectmode='extended', width=50)
        self.source_content.pack(side="top")

        self.move_button = tk.Button(self, text='Move', command=self.move)
        self.move_button.pack(side="top")

        self.dummy_button = tk.Button(self, text='Create Dummy', command=self.create_dummy)
        self.dummy_button.pack(side="top")

    def say_hi(self):
        print("hi there, everyone!")

    def select_source(self):
        file_path = filedialog.askdirectory()
        if len(file_path) == 0:
            return
        self.source_entry.delete(0, tk.END)
        self.source_entry.insert(0, file_path)

        self.av_list = Tools().av_filter(Path(file_path))

        self.source_content.delete(0, tk.END)
        for i in self.av_list:
            self.source_content.insert(tk.END, i.name)

    def select_target(self):
        file_path = filedialog.askdirectory()
        self.target_entry.delete(0, tk.END)
        self.target_entry.insert(0, file_path)
        self.target_path = Path(file_path)

    def move(self):
        target_directory_path = self.target_entry.get()
        if len(target_directory_path) == 0:
            messagebox.showinfo('No Target', 'Select a target path.')
        else:
            i = 0
            for av_path in self.av_list:
                new_path = Path(target_directory_path) / av_path.name
                if not new_path.exists():
                    av_path.rename(new_path)
                    self.source_content.delete(i)
                else:
                    i += 1

    def create_dummy(self):
        source_directory_path = Path(self.source_entry.get())
        target_directory_path = Path(self.target_entry.get())
        Tools().create_dummy(source_directory_path, target_directory_path)


if __name__ == '__main__':
    # Tools().create_dummy(Path('/Users/heweihan/Desktop/KodiTest'), Path('/Users/heweihan/Desktop/1'))
    # av_list = Tools().av_filter(Path('./KodiTest'))
    # Path('./!!!').mkdir(parents=True, exist_ok=True)
    # for path in av_list:
    #     dmm = DMM()
    #     print(path.name)
    #     dmm.search(Tools().number_getter(path.name))
    #     try:
    #         dmm.parse()
    #         file_stem = '{}_{}_{}'.format(dmm.name, dmm.date, dmm.number)
    #         Path('./!!!').joinpath(file_stem + '.jpg').write_bytes(dmm.image)
    #         target = Path('./!!!').joinpath(file_stem + path.suffix)
    #         path.rename(target)
    #     except Exception as err:
    #         print(path.name, 'no result')
    #         print(err)
    # dmm = DMM()
    # dmm.search('ebod-447')
    # dmm.parse()
    # #
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
