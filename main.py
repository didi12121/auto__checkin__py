import datetime
import os

from didi import CookieUtil, Checkin, Auto
from apscheduler.schedulers.blocking import BlockingScheduler

# profilePath = '/root/AutomationProfile'
profilePath = 'D:\AutomationProfiles'


def job():
    print('现在是{},开始执行任务'.format(datetime.datetime.now().strftime('%Y-%m-%d')))
    cookies = CookieUtil.__get_cookie__by__pro__file(r'user-data-dir=' + profilePath)
    print("获取cookie成功,开始签到")
    print('开始获得关注的超话列表')
    superIndexInfo = Checkin.to__get_super__index__list(cookies)
    for info in superIndexInfo:
        print('===== 开始签到超话 {} ====='.format(info['title']))
        Checkin.to__check__in(cookies=cookies, pid=str(info['link']).replace('//weibo.com/p/', ''))
        print('===== 结束签到超话 {} ====='.format(info['title']))


def init():
    if not os.path.exists(profilePath):
        print('====开始初始化=====')
        Auto.get_cookie(profilePath)
    print('====初始化结束,开始尝试签到====')
    job()
    print('====初始化成功====')


if __name__ == '__main__':
    print('====开始运行脚本====')
    init()
    scheduler = BlockingScheduler(timezone='Asia/Shanghai')
    scheduler.add_job(job, 'cron', day='*', hour='0', minute='0')
    scheduler.start()
