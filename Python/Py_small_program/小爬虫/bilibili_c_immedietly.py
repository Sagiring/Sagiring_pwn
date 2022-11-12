import requests
from requests.structures import CaseInsensitiveDict
import time
import csv

def get_bilibili_hot():
    page = 1
    bilibili_data = []
    while 1:
        next_url = f'https://api.bilibili.com/x/web-interface/popular?ps=20&pn=1'
        headers = CaseInsensitiveDict()
        # headers["User-Agent"] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'

        cookies = {
    'buvid3': '19F99527-07B1-434F-852D-AD240DA95712148831infoc',
    'LIVE_BUVID': 'AUTO4716261050593882',
    'rpdid': '|(J|YmYulk~~0J\'uYkYuJJm|u',
    'video_page_version': 'v_old_home',
    'fingerprint_s': '9b0bccf4ec57734720e42828cf636185',
    'i-wanna-go-back': '-1',
    'buvid_fp_plain': 'undefined',
    'buvid4': 'FA94223F-82CA-ACC9-D0BB-E38B02B4731991204-022012417-4HxpIjLfbKYv65KDSYmcdw%3D%3D',
    'fingerprint3': '0111e39952fcd2d0e77176058d70888b',
    'CURRENT_BLACKGAP': '0',
    'hit-dyn-v2': '1',
    'nostalgia_conf': '-1',
    'CURRENT_QUALITY': '116',
    'blackside_state': '0',
    '_uuid': 'A99993BA-C72A-4106B-8344-C9D7109BCAFBF01405infoc',
    'fingerprint': '0b5f8746827d7037afa0e55420fc4564',
    'buvid_fp': '0b5f8746827d7037afa0e55420fc4564',
    'DedeUserID': '23111878',
    'DedeUserID__ckMd5': '0d9aed6047896e63',
    'b_ut': '5',
    'SESSDATA': '92089377%2C1677495170%2Cf6a2f%2A81',
    'bili_jct': 'e1f20d7b43ef9b44fc321addf4ed0b3f',
    'PVID': '1',
    'CURRENT_FNVAL': '4048',
    'bp_video_offset_23111878': '700711373154287600',
    'innersign': '0',
    'b_lsid': '910EB7E25_182F9405DB8',
}

        headers = {
    'authority': 'api.bilibili.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'buvid3=19F99527-07B1-434F-852D-AD240DA95712148831infoc; LIVE_BUVID=AUTO4716261050593882; rpdid=|(J|YmYulk~~0J\'uYkYuJJm|u; video_page_version=v_old_home; fingerprint_s=9b0bccf4ec57734720e42828cf636185; i-wanna-go-back=-1; buvid_fp_plain=undefined; buvid4=FA94223F-82CA-ACC9-D0BB-E38B02B4731991204-022012417-4HxpIjLfbKYv65KDSYmcdw%3D%3D; fingerprint3=0111e39952fcd2d0e77176058d70888b; CURRENT_BLACKGAP=0; hit-dyn-v2=1; nostalgia_conf=-1; CURRENT_QUALITY=116; blackside_state=0; _uuid=A99993BA-C72A-4106B-8344-C9D7109BCAFBF01405infoc; fingerprint=0b5f8746827d7037afa0e55420fc4564; buvid_fp=0b5f8746827d7037afa0e55420fc4564; DedeUserID=23111878; DedeUserID__ckMd5=0d9aed6047896e63; b_ut=5; SESSDATA=92089377%2C1677495170%2Cf6a2f%2A81; bili_jct=e1f20d7b43ef9b44fc321addf4ed0b3f; PVID=1; CURRENT_FNVAL=4048; bp_video_offset_23111878=700711373154287600; innersign=0; b_lsid=910EB7E25_182F9405DB8',
    'origin': 'https://www.bilibili.com',
    'referer': 'https://www.bilibili.com/',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}

        params = {
            'ps': '20',
            'pn': f'{page}',
        }

        time.sleep(1)
        r = requests.get('https://api.bilibili.com/x/web-interface/popular', params=params, cookies=cookies, headers=headers)
        print(r.status_code)
        json_content = r.json()
        for item in json_content['data']['list']:
            
            bilibili_data.append((item['title'],item['pic'],item['short_link']))

        
        page +=1
        if page > 1:
            break
    return bilibili_data
with open('E:\Study\Py\OCR_bot\\bilibili.csv','w',encoding='utf-8',newline='') as f:
        csv_writer = csv.writer(f)
        data = get_bilibili_hot()
        # csv_writer.writerows(data)
        print(data)


    


       
