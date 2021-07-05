import time
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from user.models import User

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")


# 时间间隔3秒钟打印一次当前的时间
@register_job(scheduler, "interval", seconds=3, id='codeforces_spider')
def codeforces():
    user_list = User.objects.filter()


# per-execution monitoring, call register_events on your scheduler
register_events(scheduler)
scheduler.start()
print("Scheduler started!")
