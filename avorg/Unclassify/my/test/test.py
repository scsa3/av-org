import re
import pickle
import requests
from lxml import etree
from pathlib import Path

session_path = './session.pickle'
host_url = 'https://www.arzon.jp/'
xpaths = {'yes': '//*[@id="warn"]/table/tr/td[1]/a',
          'detail': '//*[@id="item"]/div/dl/dd[1]/h2/a',
          'name': '//*[@id="detail_new"]/table/tr/td[1]/table/tr[3]/td/div/table/tr[1]/td[2]/a',
          'date': '//*[@id="detail_new"]/table/tr/td[1]/table/tr[3]/td/div/table/tr[6]/td[2]',
          'number': '//*[@id="detail_new"]/table/tr/td[1]/table/tr[3]/td/div/table/tr[8]/td[2]',
          'img': '//*[@id="detail_new"]/table/tr/td[1]/table/tr[1]/td[1]/a/img'}
search_path = 'itemlist.html?mitemcd='
done_path = Path('./!Done')
yet_path = Path('./!Yet')
test_path = Path('./!Test')
s = requests.session()
# file_list = [x for x in yet_path.iterdir() if x.is_file()]
#
# # ############
# with open(session_path, 'rb') as f:
#     s = pickle.load(f)
#
# print(file_list[0].stem)
# print(s.cookies)
#
# r = s.get(host_url + search_path + file_list[0].stem)
# # print(r.content.decode('utf8'))
# Path('./!Test/1.html').write_text(r.content.decode('utf8'))
#
# r = s.get(host_url + etree.HTML(r.content).xpath(xpaths['detail'])[0].get('href'))
# # print(r.content.decode('utf8'))
# Path('./!Test/2.html').write_text(r.content.decode('utf8'))
# name = etree.HTML(r.content).xpath(xpaths['name'])[0].text.strip()
# date = etree.HTML(r.content).xpath(xpaths['date'])[0].text.strip().replace('/', '-')
# number = etree.HTML(r.content).xpath(xpaths['number'])[0].text.strip()
# print(name)
# print(date)
# print(number)
# file_list[0].rename(done_path / '{}_{}_{}.mp4'.format(name, date, number))
#

# r = s.get()
# r = s.get()


def get_session():
    try:
        with open(session_path, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        global s
        s = requests.Session()
        r = s.get(host_url)
        yes_path = etree.HTML(r.content).xpath(xpaths['yes'])[0].get('href')
        yes_url = host_url + yes_path
        s.get(yes_url)
        with open(session_path, 'wb') as f:
            pickle.dump(s, f, pickle.HIGHEST_PROTOCOL)
        return s


def get_details(av_number):
    global s
    detail = dict()
    search_response = s.get(host_url + search_path + av_number)
    detail_path = etree.HTML(search_response.content).xpath(xpaths['detail'])[0].get('href')
    search_response = s.get(host_url + detail_path)
    detail['name'] = etree.HTML(search_response.content).xpath(xpaths['name'])[0].text.strip()
    detail['date'] = etree.HTML(search_response.content).xpath(xpaths['date'])[0].text.strip().replace('/', '-')
    detail['date'] = re.search(r'\d{4}-\d{2}-\d{2}', detail['date']).group(0)
    detail['number'] = etree.HTML(search_response.content).xpath(xpaths['number'])[0].text.strip()

    return detail


def main():
    global s
    file_list = [x for x in yet_path.iterdir() if x.is_file()]
    s = get_session()
    for file in file_list:
        name_parts = get_details(file.stem)
        name_parts['extension'] = file.suffix
        file.rename(done_path / '{name}_{date}_{number}{extension}'.format(**name_parts))

if __name__ == '__main__':
    main()