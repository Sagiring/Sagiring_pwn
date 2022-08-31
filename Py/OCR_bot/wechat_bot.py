from PIL import ImageGrab
import time
import win32gui

WINDOW_TITLE = "微信" #可以是QQ聊天窗口

def getwindow_position():
    window = win32gui.FindWindow(None, WINDOW_TITLE)

    # 没有定位到窗体
    while not window:
        print('获取窗口失败,10秒后重新尝试')
        time.sleep(10)
        window = win32gui.FindWindow(None, WINDOW_TITLE)

    # 定位到窗体
    # 置顶窗口
    win32gui.SetForegroundWindow(window)
    window_position = win32gui.GetWindowRect(window)
    # 获取的坐标*缩放比例 = 显示器正确比例
  
    
    return (window_position)


def window_caputure(window_position):
    print(window_position) 
    
    wechat_begin_Px = window_position[0] * 1.5+ 450
    wechatd_begin_Py = window_position[1]* 1.5
	#话泡最长度底部像素
    wechat_End_Px = wechat_begin_Px + 1340 - 450
    wechat_End_Py = wechatd_begin_Py + 750
	# 截图保存,输入屏幕左上角和右下角的坐标
    # 450, 0, 1340,750
    pic = ImageGrab.grab(bbox=(wechat_begin_Px, wechatd_begin_Py, wechat_End_Px, wechat_End_Py))
# print(time.time())
    pic_path = f'E:\Study\Py\OCR_bot\pic\pic.jpg'
    pic.save(pic_path)

    

    # 窗体标题  用于定位窗体

def main():
    windou_position = getwindow_position()
    window_caputure(windou_position)

main()