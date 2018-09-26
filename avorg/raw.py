import requests
from lxml import html

session = requests.Session()
arzon_url = 'https://www.arzon.jp/'

response = session.get(arzon_url)
xpath = r'//*[@id="warn"]/table/tr/td[1]/a'
tree = html.fromstring(response.content)
age_check = tree.xpath(xpath)
if age_check:
    url = arzon_url + age_check[0].get('href')
    response = session.get(url)
    print(session.cookies)
response = session.get(arzon_url)
xpath = r'//*[@id="warn"]/table/tr/td[1]/a'
tree = html.fromstring(response.content)
age_check = tree.xpath(xpath)
if age_check:
    url = arzon_url + age_check[0].get('href')
    response = session.get(url)
    print(session.cookies)
