from __future__ import print_function

import pprint
import tunet
import time
from apscheduler.schedulers.blocking import BlockingScheduler


username = ''
password = ''


def job():
    pprint.pprint(tunet.auth4.checklogin())
    pprint.pprint(tunet.auth4.login(username, password))
    pprint.pprint(tunet.net.checklogin())

if __name__ == '__main__':
    # 该示例代码生成了一个BlockingScheduler调度器，使用了默认的任务存储MemoryJobStore，以及默认的执行器ThreadPoolExecutor，并且最大线程数为10。
    
    # BlockingScheduler：在进程中运行单个任务，调度器是唯一运行的东西
    scheduler = BlockingScheduler()
    # 采用阻塞的方式

    # 采用固定时间间隔（interval）的方式，每隔600秒钟执行一次
    scheduler.add_job(job, 'interval', seconds=600)
    
    scheduler.start()
