import pickle
import requests
from lxml import etree
from pathlib import Path
import re


# class AVOrg:
#     session_path = './session.pickle'
#     index_url = 'https://www.arzon.jp/'
#     xpaths = {'yes': '//*[@id="warn"]/table/tr/td[1]/a',
#               'detail': '//*[@id="item"]/div/dl/dd[1]/h2/a',
#               'name': '//*[@id="detail_new"]/table/tr/td[1]/table/tr[3]/td/div/table/tr[1]/td[2]/a',
#               'date': '//*[@id="detail_new"]/table/tr/td[1]/table/tr[3]/td/div/table/tr[6]/td[2]',
#               'number': '//*[@id="detail_new"]/table/tr/td[1]/table/tr[3]/td/div/table/tr[8]/td[2]', }
#
#     def save_session(self):
#         s = requests.Session()
#         r = s.get(self.index_url)
#         yes_url = self.index_url + etree.HTML(r.content).xpath(self.xpath['yes'])[0].get('href')
#         s.get(yes_url)
#         with open(self.session_path, 'wb') as f:
#             pickle.dump(s, f, pickle.HIGHEST_PROTOCOL)


yes_xpath = '//*[@id="warn"]/table/tr/td[1]/a'
main_page_xpath = '//*[@id="item"]/div/dl/dd[1]/h2/a'
number_xpath = '//*[@id="detail_new"]/table/tr/td[1]/table/tr[3]/td/div/table/tr[8]/td[2]'
name_xpath = '//*[@id="detail_new"]/table/tr/td[1]/table/tr[3]/td/div/table/tr[1]/td[2]/a'
date_xpath = '//*[@id="detail_new"]/table/tr/td[1]/table/tr[3]/td/div/table/tr[6]/td[2]'
url = 'https://www.arzon.jp/'
session_pickle = './session.pickle'
cookies = dict()
search_path = 'itemlist.html?mitemcd=team-100'


def get_18_session():
    s = requests.Session()
    r = s.get(url)
    tree = etree.HTML(r.content)
    redirect_url = r.url + tree.xpath(yes_xpath)[0].get('href')
    s.get(redirect_url)
    with open(session_pickle, 'wb') as f:
        pickle.dump(s, f, pickle.HIGHEST_PROTOCOL)
    return s


def main(url_postfix):
    try:
        with open(session_pickle, 'rb') as f:
            s = pickle.load(f)
        print(1)
    except FileNotFoundError:
        s = get_18_session()
        # s = requests.Session()
        # r = s.get(url)
        # with open(session_pickle, 'wb') as f:
        #     pickle.dump(s, f, pickle.HIGHEST_PROTOCOL)
        print(2)
    r = s.get(url + url_postfix)

    tree = etree.HTML(r.content)
    mymy = tree.xpath(main_page_xpath)[0].get('href')
    r = s.get(url + mymy)
    tree = etree.HTML(r.content)
    print(tree.xpath(number_xpath)[0].text)
    with open('my.html', 'wb') as f:
        f.write(r.content)


def get_detail():
    with open('my.html', 'rb') as f:
        tree = etree.HTML(f.read())
        print(tree.xpath(number_xpath)[0].text.strip())
        print(tree.xpath(name_xpath)[0].text.strip())
        print(tree.xpath(date_xpath)[0].text.strip())
        raw_date = tree.xpath(date_xpath)[0].text.strip()
        print(re.search(r'\d{4}/\d{2}/\d{2}', raw_date).group(0))


# if __name__ == '__main__':
#     # main(search_path)
#     get_detail()


# r = s.get(url)
# r.encoding = 'UTF-8'
# print(r.text)

# if Path(session_pickle).is_file():
#     with open(session_pickle, 'rb') as f:
#         cookies = pickle.load(f)
#         print(cookies)
# else:
#     s = requests.Session()
#     r = s.get(url)
#     with open(session_pickle, 'wb') as f:
#         pickle.dump(s.cookies.get_dict(), f, pickle.HIGHEST_PROTOCOL)



# with open('1111data.pickle', 'rb') as f:
#     # The protocol version used is detected automatically, so we do not
#     # have to specify it.
#     data = pickle.load(f)
#
# yes_xpath = '//*[@id="warn"]/table/tr/td[1]/a'

#
# s = requests.Session()
# r = s.get(url)
# print(s.cookies)
# print(r.url)
#
# tree = etree.HTML(r.content)
# redirect_url = r.url + tree.xpath(yes_xpath)[0].get('href')
# print(redirect_url)
#
# r = s.get(redirect_url)
# # r = requests.get(redirect_url)
#
# print(r.url)
# print(s.cookies)
# print(s.cookies.get_dict())
# with open('data.pickle', 'wb') as f:
#     # Pickle the 'data' dictionary using the highest protocol available.
#     pickle.dump(s.cookies.get_dict(), f, pickle.HIGHEST_PROTOCOL)

# session
#
# s = requests.Session()
# r = s.get(url)
# print(s.cookies)
# get_18_session()
#######################
session_path = './session.pickle'
host_url = 'https://www.arzon.jp/'
xpaths = {'yes': '//*[@id="warn"]/table/tr/td[1]/a',
          'detail': '//*[@id="item"]/div/dl/dd[1]/h2/a',
          'name': '//*[@id="detail_new"]/table/tr/td[1]/table/tr[3]/td/div/table/tr[1]/td[2]/a',
          'date': '//*[@id="detail_new"]/table/tr/td[1]/table/tr[3]/td/div/table/tr[6]/td[2]',
          'number': '//*[@id="detail_new"]/table/tr/td[1]/table/tr[3]/td/div/table/tr[8]/td[2]', }
search_path = 'itemlist.html?mitemcd=team-100'

try:
    with open(session_path, 'rb') as f:
        s = pickle.load(f)
except FileNotFoundError:
    s = requests.Session()
    r = s.get(host_url)
    yes_path = etree.HTML(r.content).xpath(xpaths['yes'])[0].get('href')
    yes_url = host_url + yes_path
    s.get(yes_url)
    with open(session_path, 'wb') as f:
        pickle.dump(s, f, pickle.HIGHEST_PROTOCOL)
