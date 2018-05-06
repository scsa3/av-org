import requests

yes_xpath = '//*[@id="warn"]/table/tbody/tr/td[1]/a'
cookie = {'PHPSESSID': 'djbukmo3kthq2s5po0r8lu9744',
          'djbukmo3kthq2s5po0r8lu9744': 'djbukmo3kthq2s5po0r8lu9744',
          '__utmc': '217774537',
          '__utmz': '217774537.1485526154.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)	'}
url = "https://www.arzon.jp/index.php?action=adult_customer_agecheck&agecheck=1&redirect=https%3A%2F%2Fwww.arzon.jp%2Fitemlist.html%3Fmitemcd%3Dteam-100"
url = "https://www.arzon.jp/"
# url = 'http://google.com'
# r = requests.get(url, timeout=5, cookies=cookie)
r = requests.get(url)
r.encoding = 'utf-8'
print(r.url)
print(r.status_code)
# print(r.cookies)
print(r.text)

# for cookie in r.cookies:
#     print(cookie)
# if r.status_code == 200:
#     for cookie in r.cookies:
#         print(cookie)
