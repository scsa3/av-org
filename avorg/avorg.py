import re
from dataclasses import dataclass
from operator import methodcaller
from pathlib import Path
from typing import List

import requests
from lxml import etree


@dataclass
class Porn:
    video_path: Path
    actress: str = None
    release_date: str = None
    cover_path: Path = None
    picture: bytes = None
    dvd_id: str = None
    page: bytes = None
    content_id: str = None

    def parse(self):
        tree = etree.HTML(self.page)
        self.actress = [
            actress.text.strip()
            for actress in tree.findall(XPath.actresses)
        ]
        self.release_date = tree.find(XPath.release_date).text.strip()
        self.content_id = tree.find(XPath.content_id).text.strip()

        pic_url = 'http://pics.dmm.co.jp/digital/video/{content_id}/{content_id}pl.jpg'
        pic_url = pic_url.format(content_id=self.content_id)
        self.picture = requests.get(pic_url).content

    def save_page(self):
        path = self.video_path.with_suffix('.html')
        path.write_bytes(self.page)

    def save_pic(self):
        path = self.video_path.with_suffix('.jpg')
        path.write_bytes(self.picture)


class DMM:
    def __init__(self):
        self.contain: bytes = None

    def search(self, dvd_id: str):
        url = r'http://www.dmm.co.jp/search/=/searchstr={keyword}/limit=30/n1=FgRCTw9VBA4GAVhfWkIHWw__/'

        keyword = dvd_id.replace('-', '00')
        response = requests.get(url.format(keyword=keyword))

        tree = etree.HTML(response.content)
        result = tree.find(XPath.result)

        result_url = result.get('href')
        detail_response = requests.get(result_url)
        self.contain = detail_response.content


class XPath:
    result = r'.//*[@id="list"]/li/div/p[2]/a'
    actresses = r'.//*[@id="performer"]/a'
    release_date = r'.//*[@id="mu"]/div/table/tr/td[1]/table/tr[3]/td[2]'
    content_id = r'.//*[@id="mu"]/div/table/tr/td[1]/table/tr[12]/td[2]'


class AVOrg:
    _video_pattern = r'(?P<dvd_id>[a-zA-Z]{2,5}-?[0-9]{2,5}).(avi|mp4|mkv)$'
    _pattern = re.compile(_video_pattern)

    def __init__(self):
        self.videos: List[Porn] = list()

    def collect(self, path: Path):
        for path in path.rglob('*'):
            match = self._pattern.search(path.name)
            if match:
                dvd_id = match.group('dvd_id')
                self.videos.append(Porn(video_path=path, dvd_id=dvd_id))

    def save_pages(self):
        [one_video.save_page() for one_video in self.videos]

    def loop(self, method: str):
        for i in self.videos:
            methodcaller(method)(i)

    def save_pics(self):
        self.loop('save_pic')

    def search(self):
        dmm = DMM()
        for one_video in self.videos:
            dmm.search(one_video.dvd_id)
            one_video.page = dmm.contain
            one_video.parse()

    def move(self, path: Path):
        path.mkdir(exist_ok=True)
        for one_video in self.videos:
            new_path = path / one_video.video_path.name
            one_video.video_path.rename(new_path)

    def list_video(self):
        for one_video in self.videos:
            print(one_video)


if __name__ == '__main__':
    root_path = Path('../videos/')
    # root_path = Path('/Users/heweihan/Downloads/target/')
    target_path = Path('../target/')
    # target_path = Path('/Users/heweihan/Downloads/')
    organizer = AVOrg()
    organizer.collect(root_path)
    organizer.search()
    organizer.save_pics()
    # organizer.list_video()
