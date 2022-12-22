import time
from datetime import datetime
from random import randint
from requests_html import HTMLSession

from configs import (QUESTION_ID, QUESTION_URL, POST_URL_MAP,
                     QUESTION_INFO, ANSWER_TIMES)


def parse_post_url(resp):
    '''
    解析出提交问卷的url
    '''
    # 找到rn
    rn = resp.html.search('rndnum="{}"')[0]
    # 提交问卷的时间
    raw_t = round(time.time(), 3)
    t = int(str(raw_t).replace('.', ''))
    # 模拟开始答题时间
    starttime = datetime.fromtimestamp(
        int(raw_t) - randint(1, 60 * 3)).strftime("%Y/%m/%d %H:%M:%S")
    jqnonce = resp.html.search('jqnonce="{}"')[0]
    print(f"{jqnonce},{rn}")
    url = POST_URL_MAP.format(QUESTION_ID,starttime,rn,t,jqnonce)
    return url


def parse_post_data(resp):

    data = ""
    for i in range(1,7):
        data += f'{i}${randint(1,3)}'
        data += "}"
    data += "7$3"
    post_data = {'submitdata': data}
 
    return post_data


def post_answer(session, url, data):
    '''
    提交答案
    '''
    r = session.post(url, data)
    print('提交状态：{}'.format(r.status_code))


def simulate_survey():
    '''
    模拟回答问卷
    '''
    session = HTMLSession()
    resp = session.get(QUESTION_URL)
    url = parse_post_url(resp)
    data = parse_post_data(resp)
    post_answer(session, url, data)


def main():
    print('开始模拟填写问卷,共模拟{}次'.format(ANSWER_TIMES))
    for i in range(ANSWER_TIMES):
        simulate_survey()
        sleep_time = 5
        print('第{}次问卷填写完毕，即将沉睡{}s'.format(i+1, sleep_time))
        time.sleep(sleep_time)


if __name__ == '__main__':
    main()
