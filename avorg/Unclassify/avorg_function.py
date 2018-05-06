import re
import pickle
import requests
from lxml import etree
from pathlib import Path

url = {'host': 'http://www.dmm.co.jp',
       'search': 'http://www.dmm.co.jp/search/=/n1=FgRCTw9VBA4GAVhfWkIHWw__/sort=ranking/searchstr='}
path = {'done': Path('./Done/'),
        'yet': Path('./Yet/')}
xpath = {'detail':  './/*[@id="list"]/li/div/p[2]/a',
         'name':    './/*[@id="performer"]/a',
         'date':    './/*[@id="mu"]/div/table/tr/td[1]/table/tr[3]/td[2]',
         'image':   './/*[@id="{}"]',
         'thumb':   './/*[@id="package-src-{}"]'}


def get_data(file_path=Path()):
    av = dict()
    av['number'] = file_path.stem
    page_path = file_path.parent / Path(av['number'] + '.html')
    search_number = av['number'].replace('-', '00')
    search_response = requests.get(url['search'] + search_number)
    search_tree = etree.HTML(search_response.content)
    branch_search = search_tree.find(xpath['detail'])
    detail_url = branch_search.get('href')
    response = requests.get(detail_url)
    branch = dict()
    tree = etree.HTML(response.content)
    branch['name'] = tree.find(xpath['name'])
    branch['date'] = tree.find(xpath['date'])
    branch['image'] = tree.find(xpath['image'].format(search_number))
    branch['thumb'] = tree.find(xpath['thumb'].format(search_number))

    image_url = branch['image'].get('href')
    image_name = av['number'] + '.' + image_url.split('.')[-1]
    image_path = file_path.parent / Path(image_name)

    thumb_url = branch['thumb'].get('src')
    thumb_name = av['number'] + '.thumb.' + image_url.split('.')[-1]
    thumb_path = file_path.parent / Path(thumb_name)

    image_path.write_bytes(requests.get(image_url).content)
    # page_path.write_bytes(response.content)
    # thumb_path.write_bytes(requests.get(thumb_url).content)

    av['path'] = file_path
    av['name'] = branch['name'].text
    av['date'] = branch['date'].text.strip().replace('/', '-')
    # av['page'] = response.content
    av['image'] = image_path
    # av['thumb'] = thumb_path

    return av


def save_data(av=dict()):
    new_file_name = '{}_{}_{}{}'.format(av['name'], av['date'], av['number'], av['path'].suffix)
    new_image_name = '{}_{}_{}{}'.format(av['name'], av['date'], av['number'], av['image'].suffix)
    av['path'].rename(path['done'] / new_file_name)
    av['image'].rename(path['done'] / new_image_name)


l = [x for x in path['yet'].iterdir() if x.is_file()]

for p in l:
    # try:
    #     d = get_data(p)
    #     save_data(d)
    # except:
    #     print('no data:' + p)
    d = get_data(p)
    save_data(d)

# d = get_data(Path('./Yet/team-100.mp4'))
# save_data(d)
