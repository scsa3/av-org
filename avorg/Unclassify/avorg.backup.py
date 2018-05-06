import re
import shutil
import pickle
import requests
from lxml import etree
from pathlib import Path
from time import sleep

url_host = 'https://www.arzon.jp'
url = {'search': 'http://www.dmm.co.jp/digital/videoa/-/detail/=/cid='}
path = {'done': './Done',
        'yet': './Yet'}
path_done = Path('./Done/')
path_yet = Path('./Yet')
xpath = {'yes': './/*[@id="warn"]/table/tr/td[1]/a',
         'thumb': './/*[@id="item"]/div/dl/dt/a/img',
         'detail': './/*[@id="item"]/div/dl/dd[1]/h2/a',
         'name': './/*[@id="detail_new"]/table/tr/td[1]/table/tr[3]/td/div/table/tr[1]/td[2]/a',
         'date': './/*[@id="detail_new"]/table/tr/td[1]/table/tr[3]/td/div/table/tr[6]/td[2]',
         'image': './/*[@id="detail_new"]/table/tr/td[1]/table/tr[1]/td[1]/a/img'}
# get file list
pattern_av = r'[a-zA-Z]{3,4}-\d{3}(\.mp4|\.avi|\.wmv|\.mkv)'
pattern_url_extension = r'/\w+(?P<extension>\.\w+)(\?|$)'

list_file = [x for x in path_yet.iterdir() if x.is_file() and re.match(pattern_av, x.name)]
print(list_file)
# get age check
session = requests.Session()
response = session.get(url_host)
tree = etree.HTML(response.content)
branch_yes = tree.find(xpath['yes'])
path_yes = branch_yes.get('href')
session.get(url_host + path_yes)
sleep(1)
#
path_done.mkdir(parents=True, exist_ok=True)
for path_file in list_file:
    av_number = path_file.stem
    # search
    response_search = session.get('https://www.arzon.jp/itemlist.html?mitemcd=' + av_number)
    tree_search = etree.HTML(response_search.content)
    branch_detail = tree_search.find(xpath['detail'])
    branch_thumb = tree_search.find(xpath['thumb'])
    path_detail = branch_detail.get('href')
    # go to detail page
    response_detail = session.get(url_host + path_detail)
    tree_detail = etree.HTML(response_detail.content)
    branch_name = tree_detail.find(xpath['name'])
    branch_date = tree_detail.find(xpath['date'])
    av_name = branch_name.text.strip()
    av_date = branch_date.text.strip().replace('/', '-')[:10]
    branch_image = tree_detail.find(xpath['image'])
    path_image = branch_image.get('src')
    url_image = 'https:' + path_image
    response_image = session.get(url_image, stream=True)
    new_file_stem = '{}_{}_{}'.format(av_name, av_date, av_number)
    new_file_name = new_file_stem + path_file.suffix
    match_image_extension = re.search(pattern_url_extension, url_image)
    image_extension = match_image_extension.group('extension')
    image_file_name = new_file_stem + image_extension
    print(new_file_name)
    print(image_file_name)
    new_av_path = path_done / new_file_name
    new_image_path = path_done / image_file_name
    # path_file.rename(new_av_path)
    print(url_image)
    with open('./done/test.jpg', 'wb') as f:
        response_image.raw.decode_content = True
        shutil.copyfileobj(response_image.raw, f)
        # # rename
    # new_name = path_file.name
    # path_file.rename(path_done / new_name)
    # sleep(5)


