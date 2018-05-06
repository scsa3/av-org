import re
import pickle
import requests
from lxml import etree
from pathlib import Path


class AVOrg:
    pass


class AV:
    pass


class Arzon:
    url_host = 'https://www.arzon.jp/'
    url_dict = {'host': 'https://www.arzon.jp',
                'search': 'itemlist.html?mitemcd='}
    xpath_dict = {'yes': './/*[@id="warn"]/table/tr/td[1]/a'}
    session = requests.Session()

    def __init__(self):
        self.age_check()

    def age_check(self):
        url = self.url_dict
        xpath = self.xpath_dict

        response = self.session.get(url['host'])
        tree = etree.HTML(response.content)
        branch_yes = tree.find(xpath['yes'])
        if branch_yes is not None:
            path = {'yes': branch_yes.get('href')}
            self.session.get(url['host'] + path['yes'])

    def search(self, number=None):
        url = self.url_dict
        xpath = self.xpath_dict

        response = self.session.get(url['host'] + url['search'] + number)
        tree = etree.HTML(response.content)
        branch = tree.find(xpath['search'])
        path = {'result': branch.get('href')}
        response = self.session.get(url['host'] + path['result'])

        return response


a = Arzon()
