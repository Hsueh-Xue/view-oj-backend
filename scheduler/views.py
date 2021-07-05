# import time
# from apscheduler.schedulers.background import BackgroundScheduler
# from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
# from user.models import User
# from oj.models import OJUser, OJ
# from spiders.codeforces_spider import CodeforcesSpider
#
# scheduler = BackgroundScheduler()
# scheduler.add_jobstore(DjangoJobStore(), "default")
#
#
# # 时间间隔3秒钟打印一次当前的时间
# @register_job(scheduler, "interval", seconds=60, id='codeforces_spider')
# def codeforces():
#     user_list = User.objects.filter(status=0).all()
#     oj = OJ.objects.filter(id=1, status=0).first()
#     if not oj:
#         pass
#     codeforces_spider = CodeforcesSpider()
#     for user in user_list:
#         oj_user = OJUser.objects.filter(user=user, oj=oj).first()
#         if not oj:
#             continue
#         print(user.username)
#         rating = codeforces_spider.get_user_rating(oj_user.oj_username)
#         problem_cnt = codeforces_spider.get_problem_info(oj_user.oj_username)
#         oj_user.oj_rating = rating
#         oj_user.problem_count = problem_cnt
#         oj_user.save()
#
#
# # per-execution monitoring, call register_events on your scheduler
# register_events(scheduler)
# scheduler.start()
# print("Scheduler started!")
