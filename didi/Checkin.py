import json

import requests
from requests.cookies import RequestsCookieJar

url = "https://weibo.com/p/aj/general/button?api=http://i.huati.weibo.com/aj/super/checkin&id" \
      "={}"


def to__check__in(cookies, pid):
    print("{}签到开始".format(pid))
    jar = RequestsCookieJar()
    for cookie in cookies:
        jar.set(cookie['name'], cookie['value'])
    response = requests.request("GET", url.format(pid), cookies=jar)
    data = json.loads(response.text)
    if data['code'] == 100000:
        print("签到成功")
    else:
        print(data['msg'])
    print("{}签到结束".format(pid))
