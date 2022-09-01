import requests

import time
import csv
import re



def weibo_get_hot():
    tilte = []
# headers = CaseInsensitiveDict()
# headers["User-Agent"] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    cookies = {
'SINAGLOBAL': '6706231733080.883.1630076787658',
'UOR': 'cn.bing.com,s.weibo.com,cn.bing.com',
'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WFQBfK_iLrU1pBYqj0XkQDo5JpX5KMhUgL.Fo-0SK2pSh2N1hq2dJLoI7YNSKe4SK2XSonE-s_HdXYt',
'ALF': '1693579541',
'SSOLoginState': '1662043541',
'SCF': 'AhMibtVML7Q3o9_7y8drkiB_cm8tN9exrkuukbRDvTWba9XlIz3tSV-LyG_K7WkVhBb_eRYcOgoDY2iKCCqlZ6Q.',
'SUB': '_2A25OFLXFDeThGeNN7lMQ9C_LwzqIHXVtY6ANrDV8PUNbmtANLRXZkW9NSblWWW-fik5lIUsqanNjvY7lVThQlrUp',
'_s_tentry': 'login.sina.com.cn',
'Apache': '2769734748409.92.1662043544578',
'ULV': '1662043544586:19:1:1:2769734748409.92.1662043544578:1646024198152',
}

    headers = {
'authority': 's.weibo.com',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-language': 'zh-CN,zh;q=0.9',
'cache-control': 'max-age=0',
# Requests sorts cookies= alphabetically
# 'cookie': 'SINAGLOBAL=6706231733080.883.1630076787658; UOR=cn.bing.com,s.weibo.com,cn.bing.com; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFQBfK_iLrU1pBYqj0XkQDo5JpX5KMhUgL.Fo-0SK2pSh2N1hq2dJLoI7YNSKe4SK2XSonE-s_HdXYt; ALF=1693579541; SSOLoginState=1662043541; SCF=AhMibtVML7Q3o9_7y8drkiB_cm8tN9exrkuukbRDvTWba9XlIz3tSV-LyG_K7WkVhBb_eRYcOgoDY2iKCCqlZ6Q.; SUB=_2A25OFLXFDeThGeNN7lMQ9C_LwzqIHXVtY6ANrDV8PUNbmtANLRXZkW9NSblWWW-fik5lIUsqanNjvY7lVThQlrUp; _s_tentry=login.sina.com.cn; Apache=2769734748409.92.1662043544578; ULV=1662043544586:19:1:1:2769734748409.92.1662043544578:1646024198152',
'referer': 'https://login.sina.com.cn/',
'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'cross-site',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}

    params = {
'sudaref': 'cn.bing.com',
}
    time.sleep(1)
    r = requests.get('https://s.weibo.com/top/summary/', params=params, cookies=cookies, headers=headers)
    content = r.text
# r.encoding='utf-8'
# print(content)
    tilte_list = re.findall('<a href="\/weibo\?q=.*?target="_blank">(.*?)<\/a>',content)
    # print(tilte_list)
    for i in range(len(tilte_list)):
        tilte.append([tilte_list[i]])
    # print(tilte)
    return tilte

with open('E:\Study\Py\OCR_bot\weibo_hot.csv','w',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    data = weibo_get_hot()
    # print(data)
    if data:
        csv_writer.writerows(data)