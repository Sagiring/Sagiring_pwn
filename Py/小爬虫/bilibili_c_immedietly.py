import requests
from requests.structures import CaseInsensitiveDict
import time

page = 1
while 1:
    next_url = f'https://api.bilibili.com/x/web-interface/popular?ps=20&pn={page}'
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
        'bp_article_offset_23111878': '689267583018336400',
        'SESSDATA': '87cc0878%2C1677249680%2C08686%2A81',
        'bili_jct': '8de252bd1bd48acdcb4a14bd32bd2b32',
        'sid': '6ofrn8b3',
        'CURRENT_FNVAL': '4048',
        'innersign': '0',
        'b_lsid': '265A5528_182EA0BF7C9',
        'PVID': '4',
        'bp_video_offset_23111878': '699843450464370700',
    }

    headers = {
        'authority': 'api.bilibili.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'buvid3=19F99527-07B1-434F-852D-AD240DA95712148831infoc; LIVE_BUVID=AUTO4716261050593882; rpdid=|(J|YmYulk~~0J\'uYkYuJJm|u; video_page_version=v_old_home; fingerprint_s=9b0bccf4ec57734720e42828cf636185; i-wanna-go-back=-1; buvid_fp_plain=undefined; buvid4=FA94223F-82CA-ACC9-D0BB-E38B02B4731991204-022012417-4HxpIjLfbKYv65KDSYmcdw%3D%3D; fingerprint3=0111e39952fcd2d0e77176058d70888b; CURRENT_BLACKGAP=0; hit-dyn-v2=1; nostalgia_conf=-1; CURRENT_QUALITY=116; blackside_state=0; _uuid=A99993BA-C72A-4106B-8344-C9D7109BCAFBF01405infoc; fingerprint=0b5f8746827d7037afa0e55420fc4564; buvid_fp=0b5f8746827d7037afa0e55420fc4564; DedeUserID=23111878; DedeUserID__ckMd5=0d9aed6047896e63; b_ut=5; bp_article_offset_23111878=689267583018336400; SESSDATA=87cc0878%2C1677249680%2C08686%2A81; bili_jct=8de252bd1bd48acdcb4a14bd32bd2b32; sid=6ofrn8b3; CURRENT_FNVAL=4048; innersign=0; b_lsid=265A5528_182EA0BF7C9; PVID=4; bp_video_offset_23111878=699843450464370700',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }

    params = {
        'ps': '20',
        'pn': f'{page}',
    }

    time.sleep(1)
    r = requests.get('https://api.bilibili.com/x/web-interface/popular', params=params, cookies=cookies, headers=headers)
    # print(r.status_code)
    json_content = r.json()
    for item in json_content['data']['list']:
        print(item['title'])
    page +=1
    if page > 2:
        break

