import json

import requests
from requests.cookies import RequestsCookieJar

url = "https://weibo.com/p/aj/general/button?api=http://i.huati.weibo.com/aj/super/checkin&id" \
      "={}"


def to__check__in(cookies, pid):
    jar = RequestsCookieJar()
    for cookie in cookies:
        jar.set(cookie['name'], cookie['value'])
    response = requests.request("GET", url.format(pid), cookies=jar)
    data = json.loads(response.text)
    if data['code'] == 100000:
        print("签到成功")
    else:
        print(data['msg'])


def to__get_super__index__list(cookies):
    print("开始获取超话列表")
    jar = get_cookie(cookies)
    response = requests.request("GET", 'https://weibo.com/ajax/profile/topicContent?tabid=231093_-_chaohua', cookies=jar)
    data = json.loads(response.text)
    # return list(map(lambda x: (str(json.loads(json.dumps(x))['link']).replace('//weibo.com/p/', '')), data['data'][
    # 'list']))
    return data['data']['list']

def get_cookie(cookies):
    jar = RequestsCookieJar()
    for cookie in cookies:
        jar.set(cookie['name'], cookie['value'])
    return jar
