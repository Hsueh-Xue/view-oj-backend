from django.shortcuts import render

# Create your views here.
import time
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")


# 时间间隔3秒钟打印一次当前的时间
@register_job(scheduler, "interval", seconds=3, id='test_job2')
def test_job():
    format_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(format_time)


# per-execution monitoring, call register_events on your scheduler
register_events(scheduler)
scheduler.start()
print("Scheduler started!")
