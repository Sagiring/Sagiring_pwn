from site import USER_BASE
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
import random
from bilibili_hot import get_bilibili_hot
from weibo_hot import weibo_get_hot

BAIDU_OCR_APP_ID = '27238006'
BAIDU_OCR_API_KEY = 'ksVOt8Rw4CN3yrEEGpi0nOVx'
BAIDU_OCR_SECRET_KEY = 'k2zv3nQOTjxKoc8XYa3GPGgOQK07GZIX'
WINDOW_TITLE = "微信"
PIC_USER = [80, 90, 450, 380]
PIC_MSG = [450, 30, 1300, 550]
PIC_RES = [460, 430, 1050, 520]
CLICK_USER = [300, 150]
CLICK_MSG = [650, 650]
CLICK_SEND = [1200, 720]


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
    # list(window_position)

    # 缩放比例
    # 话泡最长度底部像素
    # 截图保存,输入屏幕左上角和右下角的坐标
    # 450, 0, 1340,750
    pic_user = ImageGrab.grab(bbox=(window_position[0] * + PIC_USER[0], window_position[1] +
                              PIC_USER[1], window_position[0] + PIC_USER[2], window_position[1] + PIC_USER[3]))
    pic_user_path = f'E:\Study\Py\OCR_bot\pic\pic_user.jpg'
    pic_user_hash_path = f'E:\Study\Py\OCR_bot\pic\pic_user_hash.jpg'
    pic_user.save(pic_user_path)
    if pic_md5(pic_user_path) != pic_md5(pic_user_hash_path):
        pyautogui.click(
            window_position[0] + CLICK_USER[0], window_position[1] + CLICK_USER[1])
        pic_user.save(pic_user_hash_path)
        print("会话对象已更新")
    else:
        pass
        # print("会话对象重复")
    # 更新窗口！

    pic_msg = ImageGrab.grab(bbox=(window_position[0] + PIC_MSG[0], window_position[1] +
                             PIC_MSG[1], window_position[0] + PIC_MSG[2], window_position[1] + PIC_MSG[3]))
    pic_msg_path = f'E:\Study\Py\OCR_bot\pic\pic_msg.jpg'
    pic_msg_hash_path = f'E:\Study\Py\OCR_bot\pic\pic_msg_hash.jpg'
    pic_msg.save(pic_msg_path)
    if pic_md5(pic_msg_path) != pic_md5(pic_msg_hash_path):
        is_new_msg = 1
        pic_msg.save(pic_msg_hash_path)
        pic_res = ImageGrab.grab(bbox=(window_position[0] + PIC_RES[0], window_position[1] +
                                 PIC_RES[1], window_position[0] + PIC_RES[2], window_position[1] + PIC_RES[3]))
        pic_res_path = f'E:\Study\Py\OCR_bot\pic\pic_res.jpg'
        pic_res.save(pic_res_path)

    return is_new_msg
    # 窗体标题  用于定位窗体


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def ocr_data_get(BAIDU_OCR_APP_ID, BAIDU_OCR_API_KEY, BAIDU_OCR_SECRET_KEY):
    try:
        client = AipOcr(BAIDU_OCR_APP_ID, BAIDU_OCR_API_KEY,
                        BAIDU_OCR_SECRET_KEY)
        save_pic_path = "E:\Study\Py\OCR_bot\pic\pic_res.jpg"
        image = get_file_content(save_pic_path)
        ocr_result = client.basicGeneral(image)
        # print(ocr_result)
    except:
        ocr_result = ''
    return ocr_result


def send_msg(window_position, res):
    pyperclip.copy(res)
    pyautogui.click(window_position[0] + CLICK_MSG[0],
                    window_position[1] + CLICK_MSG[1])
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.click(window_position[0] + CLICK_SEND[0],
                    window_position[1] + CLICK_SEND[1])


def msg_creat(window_position):
    exit = 0
    res = ''
    ocr_data = ocr_data_get(
        BAIDU_OCR_APP_ID, BAIDU_OCR_API_KEY, BAIDU_OCR_SECRET_KEY)
    # print(ocr_data)
    if ocr_data['words_result']:
        news_msg = ocr_data['words_result'][len(
            ocr_data['words_result'])-1]['words']

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
    if ('b站热搜' in news_msg and news_msg[4:].isdigit()) or news_msg == 'b站热搜':
        if news_msg[4:].isdigit():
            res = bilibili_msg_creat(int(news_msg[4:]))
        else:
            res = bilibili_msg_creat()
        res += '(后跟数字指定显示列数)'
    elif news_msg == '更新b站热搜':
        get_bilibili_hot()
        res = '已更新'

    elif ('微博热搜' in news_msg and news_msg[4:].isdigit()) or news_msg == '微博热搜':
        if news_msg[4:].isdigit():
            res = weibo_msg_creat(int(news_msg[4:]))
        else:
            res = weibo_msg_creat()
        res += '(后跟数字指定显示列数)'
    elif news_msg == '更新微博热搜':
        weibo_get_hot()
        res = '已更新'

    elif 'bot说' in news_msg:
        if news_msg[4:]:
            res = news_msg[4:]
        else:
            res = '要说什么捏？'

    # elif news_msg == 'bot关机':
    #     res = '正在关闭bot'
    #     exit = 1

    elif '拍了拍我' in news_msg:
        if '"Marln"拍了拍我' == news_msg:
            user = news_msg[1:-5]
            res = f'@{user} 老子草尼玛'
        else:
            user = news_msg[1:-5]
            res = f'@{user} 我喜欢你~'

    elif '问' in news_msg and '答' in news_msg:
        write_msg_incsv(news_msg)
        res = '我记住啦~'
    elif '删除词条' in news_msg:
        pass
        res = 'bot在努力开发此功能~'

    elif 'bot-help' == news_msg:
        path = 'E:\Study\Py\OCR_bot\\help.txt'
        res = text_reader(path)

    elif news_msg == 'bot今天吃什么':
        path = 'E:\Study\Py\OCR_bot\\today_diet.txt'
        with open(path, 'r', encoding='utf-8', newline='')as f:
            content = f.read().split('\n')
            res = random.choice(content)

    elif news_msg:
        res = find_msg_incsv(news_msg)
    return res, exit


def text_reader(path):
    with open(path, 'r', encoding='utf-8', newline='')as f:
        content = f.read()
        return content


def write_msg_incsv(news_msg):
    with open('E:\Study\Py\OCR_bot\human_language.csv', 'a+', encoding='utf-8', newline='') as f:
        data = [news_msg[1:str.find(news_msg, '答')],
                news_msg[str.find(news_msg, '答') + 1:]]
        csv_writer = csv.writer(f)
        csv_writer.writerow(data)


def find_msg_incsv(news_msg):
    with open('E:\Study\Py\OCR_bot\human_language.csv', 'r', encoding='utf-8', newline='')as f:
        res = ''
        content = csv.reader(f)
        for row in content:
            # print(row)
            if row[0] == news_msg:
                res = row[1]
    return res


def pic_md5(pic_path):
    with open(pic_path, 'rb') as pic_hash:
        pic_data = pic_hash.read()
        base64_data = base64.b64encode(pic_data)
        # print(base64_data)
        data = hashlib.md5(base64_data).hexdigest()
        return data


def bilibili_msg_creat(cnt=3):
    num = 0
    result_content = ''
    with open('E:\Study\Py\OCR_bot\\bilibili.csv', 'r', encoding='utf-8', newline='') as f:
        content = csv.reader(f)
        for row in content:
            num += 1
            result_content += f'top{num}->{row[0]}->{row[2]}\n'
            if num >= cnt:
                break
    return result_content


def weibo_msg_creat(cnt=10):
    num = 0
    result_content = ''
    with open('E:\Study\Py\OCR_bot\weibo_hot.csv', 'r', encoding='utf-8', newline='') as f:
        content = csv.reader(f)
        for row in content:
            num += 1
            result_content += f'top{num}->{row[0]}\n'
            if num >= cnt:
                break
    return result_content


def main():

    while 1:

        window_position = getwindow_position()
        is_new_msg = window_caputure_isnewmsg_click(window_position)
        # print(is_new_msg)
        print('监听ing')

        if is_new_msg:
            is_new_msg = 0
            print('会话已更新')
            exit = msg_creat(window_position)
            if exit:
                print('已关机')
                break

        time.sleep(10)


main()
