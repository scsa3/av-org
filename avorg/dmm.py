# ['対応デバイス：', '配信開始日：', '商品発売日：', '収録時間：', '出演者：', '監督：',
# 'シリーズ：', 'メーカー：]
# ['Release Date:', 'Runtime:', 'Director:', 'Studio:', 'Label:', 'Subtitles:',
# 'Channel:', 'Content ID:', 'DVD ID:', 'Series:', 'Languages:']


from pathlib import Path

# 応デバイス：	パソコン、iPhone/iPad、Android、Chromecast、Amazon Fire TV/Fire TV Stick、Apple TV、PS4/PS Vita
# 配信開始日：	2007/12/13
# 商品発売日：	----
# 収録時間：	116分
# 出演者：	妃乃ひかり
# 監督：	南★波王
# シリーズ：	E-BODY
# メーカー：	E-BODY
# レーベル：	E-BODY
# ジャンル：	単体作品  独占配信  潮吹き  指マン  巨乳  シックスナイン  3P・4P
# 品番：	ebod00001
# 平均評価：	 レビューを見る
import requests
from lxml import etree


class URL:
    main = 'http://www.dmm.co.jp'

    def search(self, keyword: str):
        return (self.main
                + '/search/=/sort=ranking/n1=FgRCTw9VBA4GAVhfWkIHWw__/searchstr='
                + keyword)


class DMM:
    url = r'http://www.dmm.co.jp/search/=/searchstr=ebod-001/n1=FgRCTw9VBA4GAVhfWkIHWw__/sort=ranking/'
    search_url = r'http://www.dmm.co.jp/search/=/searchstr={keyword}/n1={category}/sort=ranking/'

    category = {
        'Videos': r'FgRCTw9VBA4GAVhfWkIHWw__',
        'Monthly': r'FgRCTw9VBA4GCF5WR14KTg__',
    }

    class XPath:
        result = r'//*[@id="list"]/li/div/p[2]/a'
        actresses = r'//*[@id="performer"]/a'
        release_date = r'//*[@id="mu"]/div/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]'
        # //*[@id="mu"]/div/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]
        # //*[@id="mu"]/div/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]

    def search(self, dvd_id: str):
        url = URL().search(dvd_id)
        response = requests.get(url)
        tree = etree.HTML(response.content)
        results = tree.find('//*[@id="list"]/li/div/p[2]/a')
        print(results)

    def detail(self, dvd_id):
        pass


class DMM2:
    directories = {
        'done': Path('./Done'), }
    urls = {
        'main': 'http://www.dmm.co.jp/',
        'search': 'http://www.dmm.co.jp/digital/videoa/-/detail/=/cid=',
        'search2': 'http://www.dmm.co.jp/search/=/n1=FgRCTw9VBA4GAVhfWkIHWw__/sort=ranking/searchstr=hmgl00149', }
    xpaths = {
        'name': './/*[@id="performer"]/a',
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

if __name__ == '__main__':
    dmm = DMM()
    dmm.search('ebod-001')
