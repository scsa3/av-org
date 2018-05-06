# https://www.arzon.jp/itemlist.html?mitemcd=team-100
# https://www.arzon.jp/index.php?action=adult_customer_agecheck&agecheck=1&redirect=https%3A%2F%2Fwww.arzon.jp%2Fitemlist.html%3Fmitemcd%3Dteam-100
# //*[@id="item"]/div/dl/dd[1]/h2/a
# from lxml import etree
# from lxml.html import fromstring
# from lxml import html
from lxml import etree
from io import StringIO
# f = open("my_urllib.html", "rb")
# root = etree.fromstring(f.read())
# print(root.tag)
f = StringIO('<foo><bar></bar></foo>')
tree = etree.parse(f)
r = tree.xpath('/foo/bar')
print(len(r))

f = open("my_urllib.html", "rb")
tree = etree.HTML(f.read())
r = tree.xpath('//*[@id="item"]/div/dl/dd[1]/h2/a')
print(len(r))
#
# # tree = lxml.html
# # tree = etree.parse('my_urllib.html')
# # tree = etree.htmlfile('my_urllib.html')
# # r = tree.xpath('//*[@id="item"]/div/dl/dd[1]/h2/a')
# # print(len(r))
# with open("my_urllib.html", "rb") as f:
#     html = etree.HTML(f.read())
#     r = html.xpath('//*[@id="item"]/div/dl/dd[1]/h2/a')
#     result = etree.tostring(html, pretty_print=True, method="html")
#     print(result)
#     print(len(r))
#     #
#     # tree = fromstring(f.read())
#     # # tree = fromstring(f.read())
#     # # pass
#     # # print(type(f.read()))
#     # # tree = etree.parse(f.read())
#     # r = tree.xpath('//*[@id="item"]/div/dl/dd[1]/h2/a')
#     # # print(len(r))
#     # print(tree.tostring())
# # f = StringIO('<foo><bar></bar></foo>')
# # tree = etree.parse(f)
# #
# # r = tree.xpath('//*[@id="item"]/div/dl/dd[1]/h2/a')
# # >>> len(r)
# # 1
# # >>> r[0].tag
# # 'bar'
# #
# # >>> r = tree.xpath('bar')
# # >>> r[0].tag
# # 'bar'
