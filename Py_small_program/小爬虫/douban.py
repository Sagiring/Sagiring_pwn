import requests
from lxml import etree
from requests.structures import CaseInsensitiveDict
from IPython.display import display
from IPython.core.display import HTML
import time
import csv

page = 1
book_info = []
next_url = 'https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?start=0&type=T'
while 1:
    headers = CaseInsensitiveDict()
    headers["User-Agent"] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    time.sleep(1)
    r = requests.get(next_url,headers=headers)

    sel = etree.HTML(r.text)
    print(r.status_code)

    for block in sel.xpath("//li[@class='subject-item']"):
        title = ''
        elem_price = block.xpath('.//h2/a')
        
        if elem_price:
            title = ''.join(elem_price[0].itertext()).replace(' ','').replace('\n','')
      

        price = -1
        elem_price = block.xpath(".//span[@class='buy-info']/a/text()")
        # print(elem_price)
        if elem_price:
            find_loc = elem_price[0].strip()
            price = float(elem_price[0].strip()[find_loc.find('版')+2:find_loc.find('元')])
        

        cover = ''
        elem_cover = block.xpath(".//img/@src")
        # print(elem_price)
        # 加载图片！
        if elem_cover:
            cover = elem_cover[0]
        # # print(cover)
        print(title,price)
        book_info.append([title, cover, price])
        # display(HTML(f"<img src='{cover}'>"))
         #加载图片！

    elem_next_page = sel.xpath("//span[@class='next']/a/@href")

    if elem_next_page:
        # print(elem_next_page[0])
        next_url = f'https://book.douban.com{elem_next_page[0]}'
        # print(next_url)
        page += 1
        print(page)
    else:
            break
    if page > 5:
        break
with open('books.csv','w',encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(book_info)