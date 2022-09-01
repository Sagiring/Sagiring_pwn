from PIL import ImageGrab
import time
import win32gui
# import win32con
import pyperclip
import pyautogui
from aip import AipOcr
import hashlib
import base64
import hashlib
import csv
import requests
from requests.structures import CaseInsensitiveDict



BAIDU_OCR_APP_ID = '27238006'
BAIDU_OCR_API_KEY = 'ksVOt8Rw4CN3yrEEGpi0nOVx'
BAIDU_OCR_SECRET_KEY = 'k2zv3nQOTjxKoc8XYa3GPGgOQK07GZIX'
WINDOW_TITLE = "微信" 

def getwindow_position():
    window_hwnd = win32gui.FindWindow(None, WINDOW_TITLE)

    # 没有定位到窗体
    while not window_hwnd:
        print('获取窗口失败,10秒后重新尝试')
        time.sleep(10)
        window_hwnd = win32gui.FindWindow(None, WINDOW_TITLE)

    # 定位到窗体
    # 置顶窗口
    # if win32gui.IsIconic(window_hwnd):
    #     win32gui.ShowWindow(WINDOW_TITLE,win32con.SW_SHOW)
    #     # 最小化顶置有问题
    # else:
    win32gui.SetForegroundWindow(window_hwnd)
    # win32gui.SetFocus(window_hwnd)

    window_position = win32gui.GetWindowRect(window_hwnd)
    # 获取的坐标*缩放比例 = 显示器正确比例
  
    
    return (window_position)

def window_caputure_isnewmsg_click(window_position):
    # print(window_position) 
    is_new_msg = 0

    wechat_begin_Px = window_position[0] * 1.5 + 460
    wechatd_begin_Py = window_position[1]* 1.5 + 450
	#话泡最长度底部像素
    wechat_End_Px = wechat_begin_Px + 1340 - 550
    wechat_End_Py = wechatd_begin_Py + 100 - 30
	# 截图保存,输入屏幕左上角和右下角的坐标
    # 450, 0, 1340,750
    pic_user = ImageGrab.grab(bbox=(window_position[0] * 1.5 + 80, window_position[1]* 1.5 + 90,window_position[0] * 1.5 + 450,window_position[1]* 1.5 + 380))
    pic_user_path = f'E:\Study\Py\OCR_bot\pic\pic_user.jpg'
    pic_user_hash_path = f'E:\Study\Py\OCR_bot\pic\pic_user_hash.jpg'
    pic_user.save(pic_user_path)
    if pic_md5(pic_user_path)!=pic_md5(pic_user_hash_path):
         pyautogui.click(window_position[0] + 300 ,window_position[1] + 150)
         pic_user.save(pic_user_hash_path)
         print("会话对象已更新")
    else:
        pass
        # print("会话对象重复")
    # 更新窗口！

    pic_msg = ImageGrab.grab(bbox=(wechat_begin_Px, wechatd_begin_Py, wechat_End_Px, wechat_End_Py))
    pic_msg_path = f'E:\Study\Py\OCR_bot\pic\pic_msg.jpg'
    pic_msg_hash_path = f'E:\Study\Py\OCR_bot\pic\pic_msg_hash.jpg'
    pic_msg.save(pic_msg_path)
    if pic_md5(pic_msg_path)!=pic_md5(pic_msg_hash_path):
        is_new_msg = 1
        pic_msg.save(pic_msg_hash_path)

    return is_new_msg
    # 窗体标题  用于定位窗体
def get_file_content(filePath):
	    with open(filePath, 'rb') as fp:
	        return fp.read()

def ocr_data_get(BAIDU_OCR_APP_ID, BAIDU_OCR_API_KEY, BAIDU_OCR_SECRET_KEY):
    client = AipOcr(BAIDU_OCR_APP_ID, BAIDU_OCR_API_KEY, BAIDU_OCR_SECRET_KEY)
    save_pic_path = "E:\Study\Py\OCR_bot\pic\pic_msg.jpg"
    image = get_file_content(save_pic_path)
    ocr_result = client.basicGeneral(image);
    # print(ocr_result)
    return ocr_result

def send_msg(window_position, res):
    pyperclip.copy( res )
    pyautogui.click(window_position[0] + 650 ,window_position[1] + 650)
    pyautogui.hotkey('ctrl','v')
    pyautogui.click(window_position[0] + 1200 ,window_position[1] + 720)

def msg_creat(window_position):
    exit = 0
    res = ''
    ocr_data = ocr_data_get(BAIDU_OCR_APP_ID, BAIDU_OCR_API_KEY, BAIDU_OCR_SECRET_KEY)
    # print(ocr_data)
    if ocr_data['words_result']:
        news_msg = ocr_data['words_result'][len(ocr_data['words_result'])-1]['words']
        
        print(news_msg)
        
        res, exit = langugage_functions(news_msg)
    else:
        print('Nothing found')
    # print(res)
    if res:
        send_msg(window_position, res)
    return exit

def langugage_functions(news_msg):
    exit = 0
    res = ''
    if news_msg == 'b站热搜':
        res = bilibili_msg_creat()
        res += '(发送 更新b站热搜 即可更新)'
    elif news_msg == '更新b站热搜':
        get_bilibili_hot()
        res = '已更新'
    elif news_msg == '微博热搜':
        pass
        res = 'bot在努力开发此功能~'
    elif 'bot说' in news_msg:
        if news_msg[4:]:
            res = news_msg[4:]
        else:
            res = '要说什么捏？'
    elif news_msg == 'bot关机':
        res = '正在关闭bot'
        exit = 1
    elif '拍了拍我' in news_msg:
        if '"Marln"拍了拍我' == news_msg:
            res = '老子草尼玛'
        else:
            res = '我喜欢你~'
    elif '问' in news_msg and '答' in news_msg:
        write_msg_incsv(news_msg)
        res ='我记住啦~'
    elif '删除词条' in news_msg:
        pass
        res = 'bot在努力开发此功能~'
    elif news_msg:
        res = find_msg_incsv(news_msg)
    return res,exit

def write_msg_incsv(news_msg):
    with open('E:\Study\Py\OCR_bot\human_language.csv','a+',encoding='utf-8',newline='') as f:
        data=[news_msg[1:str.find(news_msg,'答')],news_msg[str.find(news_msg,'答') + 1:]]
        csv_writer = csv.writer(f)
        csv_writer.writerow(data)

def find_msg_incsv(news_msg):
    with open('E:\Study\Py\OCR_bot\human_language.csv','r',encoding='utf-8',newline='')as f:
        res = ''
        content = csv.reader(f)
        for row in content:
                    # print(row)
            if row[0] == news_msg:
                res = row[1]
    return res

def pic_md5(pic_path):
    with open(pic_path,'rb') as pic_hash:
            pic_data = pic_hash.read()
            base64_data = base64.b64encode(pic_data)
        # print(base64_data)
            data = hashlib.md5(base64_data).hexdigest()
            return data

def bilibili_msg_creat(cnt = 3):

    num = 0
    result_content = ''
    with open('E:\Study\Py\OCR_bot\\bilibili.csv','r',encoding='utf-8',newline='') as f:
            content = csv.reader(f)
            for row in content:
                    num += 1
                    result_content += f'top->{num}{row[0]}->{row[2]}\n'
                    if num >= cnt:
                            break
    return result_content

def get_bilibili_hot():
    page = 1
    bilibili_data = []
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
        'CURRENT_FNVAL': '4048',
        'innersign': '0',
        'SESSDATA': '92089377%2C1677495170%2Cf6a2f%2A81',
        'bili_jct': 'e1f20d7b43ef9b44fc321addf4ed0b3f',
        'sid': 'parqjy1w',
        'b_lsid': 'DB9D9F6F_182F3DB085D',
        'bp_video_offset_23111878': '700562458064978000',
        'PVID': '3',
    }

        headers = {
            'authority': 'api.bilibili.com',
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'buvid3=19F99527-07B1-434F-852D-AD240DA95712148831infoc; LIVE_BUVID=AUTO4716261050593882; rpdid=|(J|YmYulk~~0J\'uYkYuJJm|u; video_page_version=v_old_home; fingerprint_s=9b0bccf4ec57734720e42828cf636185; i-wanna-go-back=-1; buvid_fp_plain=undefined; buvid4=FA94223F-82CA-ACC9-D0BB-E38B02B4731991204-022012417-4HxpIjLfbKYv65KDSYmcdw%3D%3D; fingerprint3=0111e39952fcd2d0e77176058d70888b; CURRENT_BLACKGAP=0; hit-dyn-v2=1; nostalgia_conf=-1; CURRENT_QUALITY=116; blackside_state=0; _uuid=A99993BA-C72A-4106B-8344-C9D7109BCAFBF01405infoc; fingerprint=0b5f8746827d7037afa0e55420fc4564; buvid_fp=0b5f8746827d7037afa0e55420fc4564; DedeUserID=23111878; DedeUserID__ckMd5=0d9aed6047896e63; b_ut=5; CURRENT_FNVAL=4048; innersign=0; SESSDATA=92089377%2C1677495170%2Cf6a2f%2A81; bili_jct=e1f20d7b43ef9b44fc321addf4ed0b3f; sid=parqjy1w; b_lsid=DB9D9F6F_182F3DB085D; bp_video_offset_23111878=700562458064978000; PVID=3',
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
        # print(r.status_code)
        json_content = r.json()
        for item in json_content['data']['list']:
            # print(item['short_link'])
            bilibili_data.append((item['title'],item['pic'],item['short_link']))

        
        page +=1
        if page > 1:
            break
    # print(bilibili_data)
    with open('E:\Study\Py\OCR_bot\\bilibili.csv','w',encoding='utf-8',newline='') as f:
        csv_writer = csv.writer(f)
        data = get_bilibili_hot()
        csv_writer.writerows(data)

def main():
    
    while 1:
        
        window_position = getwindow_position()
        is_new_msg = window_caputure_isnewmsg_click(window_position)
        # print(is_new_msg)
        print('会话重复ing')
        
        
        if is_new_msg:
            is_new_msg = 0
            print('会话已更新')
            exit = msg_creat(window_position)
            if exit:
                print('已关机')
                break
        
        time.sleep(10)
main()

