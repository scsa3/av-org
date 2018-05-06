import re
import shutil
import pickle
import requests
from lxml import etree
from pathlib import Path
from time import sleep

search_prefix = 'http://www.r18.com/common/search/searchword='
url_xpath = '//*[@id="contents"]/div[2]/section/ul[2]/li/a'
name_xpath = '//*[@id="contents"]/div[10]/div[1]/section/section/section[1]/div[2]/div/div[1]/div/span/a/text()'
genre_xpath = '//*[@id="contents"]/div[10]/div[1]/section/section/section[1]/div[2]/div/div[2]/div/a/text()'
date_xpath = '//*[@id="contents"]/div[10]/div[1]/section/section/section[1]/div[2]/dl[1]/dd[1]/text()'


def search(number='ebod-001'):
    url = search_prefix + number
    search_response = requests.get(url)
    page_url = my_parser(search_response.content, url_xpath)[0].get('href')
    page_response = requests.get(page_url)
    page_html = page_response.content
    names = my_parser(page_html, name_xpath)
    genres = my_parser(page_html, genre_xpath)
    # branches = prune(search_prefix + number, url_xpath)
    # page_url = branches[0].get('href')
    # names = prune(page_url, name_xpath)
    print(names)
    genres = [i.strip() for i in genres]
    print(genres)
    # for i in genres:
    #     print(i.strip())
    # print(genres)
    # url = search_prefix + number
    # response = requests.get(url)
    # tree = etree.HTML(response.content)
    # branch = tree.xpath(url_xpath)[0]
    # url = branch.get('href')
    # response = requests.get(url)
    # tree = etree.HTML(response.content)
    # branch = tree.xpath(name_xpath)[0]
    # print(branch)
    # print(response.content.decode('utf-8'))


def prune(url, xpath):
    response = requests.get(url)
    tree = etree.HTML(response.content)
    branches = tree.xpath(xpath)
    return branches


def my_parser(html, xpath):
    tree = etree.HTML(html)
    branches = tree.xpath(xpath)
    return branches


class R18:
    def search(self, number=str()):
        self.search_response = requests.get('http://www.r18.com/common/search/searchword={}'.format(number))
        self.page_url = my_parser(self.search_response.content, url_xpath)[0].get('href')
        self.page_response = requests.get(self.page_url)

    def names(self):
        return my_parser(self.page_response.content, name_xpath)

    def date(self):
        return my_parser(self.page_response.content, date_xpath)[0].strip()


if __name__ == '__main__':
    my_r18 = R18()
    my_r18.search('lzan00012')
    print(my_r18.names())
    print(my_r18.date())
