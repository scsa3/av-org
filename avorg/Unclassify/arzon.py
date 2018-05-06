import re
import shutil
import pickle
import requests
from lxml import etree
from pathlib import Path
from time import sleep

url = {'search': 'https://www.arzon.jp/itemlist.html?t=&m=all&s=&q='}
xpath = {'url': '//*[@id="item"]/div/dl/dt/a'}


def search(number='ebod-001'):
    search_url = url['search'] + number
    response = requests.get(search_url)
    main_url = etree.HTML(response.content).xpath(xpath['url'])
    print(response.content.decode('utf-8'))
    print(main_url)


if __name__ == '__main__':
    search()
