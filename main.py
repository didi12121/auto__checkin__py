import datetime

from didi import CookieUtil, Checkin
from apscheduler.schedulers.blocking import BlockingScheduler


def job():
    print('现在是{},开始执行任务'.format(datetime.datetime.now().strftime('%Y-%m-%d')))
    cookies = CookieUtil.__get_cookie__by__pro__file(r'user-data-dir=D:\AutomationProfile')
    print("获取cookie成功,开始签到")
    pids = [
        '100808445c68f22a32b95efe6c3d025512d13c',
        '1008089f1260fce8d1d56c76d01541995b2d5c',
    ]
    for pid in pids:
        Checkin.to__check__in(cookies=cookies, pid=pid)


if __name__ == '__main__':
    print('开始执行任务')
    scheduler = BlockingScheduler(timezone='Asia/Shanghai')
    scheduler.add_job(job, 'cron', day='*', hour='0', minute='0')
    scheduler.start()
