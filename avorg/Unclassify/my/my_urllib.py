# https://www.arzon.jp/itemlist.html?mitemcd=team-100
# https://www.arzon.jp/index.php?action=adult_customer_agecheck&agecheck=1&redirect=https%3A%2F%2Fwww.arzon.jp%2Fitemlist.html%3Fmitemcd%3Dteam-100
# //*[@id="item"]/div/dl/dd[1]/h2/a
import urllib.request
import urllib.parse

cookie = {'PHPSESSID': 'djbukmo3kthq2s5po0r8lu9744',
          'djbukmo3kthq2s5po0r8lu9744': 'djbukmo3kthq2s5po0r8lu9744',
          '__utmc': '217774537',
          '__utmz': '217774537.1485526154.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)	'}
with urllib.request.urlopen(
        'https://www.arzon.jp/index.php?action=adult_customer_agecheck&agecheck=1&redirect=https%3A%2F%2Fwww.arzon.jp%2Fitemlist.html%3Fmitemcd%3Dteam-100') as response:
    content = response.read().decode('utf-8')
    # content = response.read()
    # html = response.read()
    print(content)
    with open("my_urllib2.html", "w") as text_file:
        text_file.write(content)
with urllib.request.urlopen('https://www.arzon.jp/itemlist.html?mitemcd=team-100') as response:
    # content = response.read().decode(response.headers.get_content_charset())
    content = response.read().decode('utf-8')
    # content = response.read()
    # html = response.read()
    print(content)
    with open("my_urllib.html", "w") as text_file:
        text_file.write(content)
