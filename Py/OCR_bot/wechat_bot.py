from PIL import ImageGrab
import time
import win32gui
# import win32con
import pyperclip
import pyautogui
from aip import AipOcr
import bilibili_c_immedietly
import hashlib
import base64
import hashlib

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

def window_caputure_isnewmsg(window_position):
    # print(window_position) 
    is_new_msg = 0

    wechat_begin_Px = window_position[0] * 1.5 + 460
    wechatd_begin_Py = window_position[1]* 1.5 + 450
	#话泡最长度底部像素
    wechat_End_Px = wechat_begin_Px + 1340 - 660
    wechat_End_Py = wechatd_begin_Py + 100 - 30
	# 截图保存,输入屏幕左上角和右下角的坐标
    # 450, 0, 1340,750
    pic = ImageGrab.grab(bbox=(wechat_begin_Px, wechatd_begin_Py, wechat_End_Px, wechat_End_Py))
# print(time.time())
    pic_path = f'E:\Study\Py\OCR_bot\pic\pic.jpg'
    pic.save(pic_path)
    pic_hash_path = f'E:\Study\Py\OCR_bot\pic\pic_hash.jpg'
    
    if pic_md5(pic_path)!=pic_md5(pic_hash_path):
        is_new_msg = 1
        pic.save(pic_hash_path)
    return is_new_msg
    # 窗体标题  用于定位窗体
def get_file_content(filePath):
	    with open(filePath, 'rb') as fp:
	        return fp.read()

def ocr_data_get(BAIDU_OCR_APP_ID, BAIDU_OCR_API_KEY, BAIDU_OCR_SECRET_KEY):
    client = AipOcr(BAIDU_OCR_APP_ID, BAIDU_OCR_API_KEY, BAIDU_OCR_SECRET_KEY)
    save_pic_path = "E:\Study\Py\OCR_bot\pic\pic.jpg"
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
    ocr_data = ocr_data_get(BAIDU_OCR_APP_ID, BAIDU_OCR_API_KEY, BAIDU_OCR_SECRET_KEY)
    # print(ocr_data)
    if ocr_data['words_result']:
        news_msg = ocr_data['words_result'][len(ocr_data['words_result'])-1]['words']
        print(news_msg)
    
        if news_msg == 'b站热搜':
            res = f'top1《{bilibili_c_immedietly.get_bilibili_hot()[0]}》\ntop2《{bilibili_c_immedietly.get_bilibili_hot()[1]}》\ntop3《{bilibili_c_immedietly.get_bilibili_hot()[2]}》\n'
            send_msg(window_position, res)
        elif news_msg == '晚安':
            res = '好梦捏！'
            send_msg(window_position, res)
        else:
            res = ''
    else:
        print('Nothing found')
    # print(res)

def pic_md5(pic_path):
    with open(pic_path,'rb') as pic_hash:
            pic_data = pic_hash.read()
            base64_data = base64.b64encode(pic_data)
        # print(base64_data)
            data = hashlib.md5(base64_data).hexdigest()
            return data



def main():
    
    while 1:
        time.sleep(3)
        window_position = getwindow_position()
        is_new_msg = window_caputure_isnewmsg(window_position)
        print(is_new_msg)
        
        
        if is_new_msg:
            is_new_msg = 0
            msg_creat(window_position)
            

main()

