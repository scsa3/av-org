import re
import shutil
import pickle
import requests
from lxml import etree
from pathlib import Path
from time import sleep

path = {'done': Path('./Done/'),
        'yet': Path('./Done/')}

# get file list
pattern_av = r'[a-zA-Z]{3,4}-\d{3}(\.mp4|\.avi|\.wmv|\.mkv)'
pattern_url_extension = r'/\w+(?P<extension>\.\w+)(\?|$)'


#
class DMM:
    url = {'search': r'http://www.dmm.co.jp/search/=/n1=FgRCTw9VBA4GAVhfWkIHWw__/searchstr=',
           'search_bak': 'http://www.dmm.co.jp/digital/videoa/-/detail/=/cid='}
    xpath = {'name': './/*[@id="performer"]/a',
             'date': './/*[@id="detail_new"]/table/tr/td[1]/table/tr[3]/td/div/table/tr[6]/td[2]',
             'image': './/*[@id="detail_new"]/table/tr/td[1]/table/tr[1]/td[1]/a/img',
             'main_page': './/*[@id="list"]/li/div/p[2]/a'}

    def __init__(self):
        self.av = dict()

    def search(self, number):
        search_number = number.replace('-', '00')
        response = requests.get(self.url['search'] + search_number)
        page_url = etree.HTML(response.content).find(self.xpath['main_page']).get('href')
        response = requests.get(page_url)
        branch_name = etree.HTML(response.content).find(self.xpath['name'])
        branch_date = etree.HTML(response.content).find(self.xpath['date'])
        branch_image = etree.HTML(response.content).find(self.xpath['image'])
        print(branch_name.text)

    def search_bak(self, number):
        self.av['number'] = number
        search_number = number.replace('-', '00')
        response = requests.get(self.url['search'] + search_number)
        branch_name = etree.HTML(response.content).find(self.xpath['name'])
        branch_date = etree.HTML(response.content).find(self.xpath['date'])
        branch_image = etree.HTML(response.content).find(self.xpath['image'])
        self.av['name'] = None

        return branch_name


def save_info_page(av_number):
    url = {'search': 'http://www.dmm.co.jp/digital/videoa/-/detail/=/cid='}

    response = requests.get(url['search'] + av_number)

    xpath = {'name': './/*[@id="detail_new"]/table/tr/td[1]/table/tr[3]/td/div/table/tr[1]/td[2]/a',
             'date': './/*[@id="detail_new"]/table/tr/td[1]/table/tr[3]/td/div/table/tr[6]/td[2]',
             'image': './/*[@id="detail_new"]/table/tr/td[1]/table/tr[1]/td[1]/a/img',
             'name': './/*[@id="detail_new"]/table/tr/td[1]/table/tr[3]/td/div/table/tr[1]/td[2]/a',
             'date': './/*[@id="detail_new"]/table/tr/td[1]/table/tr[3]/td/div/table/tr[6]/td[2]',
             'image': './/*[@id="detail_new"]/table/tr/td[1]/table/tr[1]/td[1]/a/img'
             }


if __name__ == '__main__':
    my_dmm = DMM()
    x = my_dmm.search('siv00028')
    print(x)
