import json
import time
from utils.time_utils import str_to_datetime, timestamp_to_str
from libs.spider_http import SpiderHttp


class CodeforcesHttp(SpiderHttp):
    @staticmethod
    def _end_request(res, encoding: str):
        time.sleep(0.5)
        return res


class CodeforcesSpider:
    codeforces_http = CodeforcesHttp()

    def get_user_rating(self, username):
        url = 'http://codeforces.com/api/user.info?handles={}'.format(username)
        rating = 0
        last_login = 0
        res = self.codeforces_http.get(url=url).json()
        if res['status'] == "OK":
            rating = res['result'][0]['rating']
            last_login = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(res['result'][0]['lastOnlineTimeSeconds']))
            print(last_login)
        return rating, last_login

    def get_problem_info(self, oj_username):
        username = oj_username
        accept_problem_list = []
        url = 'http://codeforces.com/api/user.status?handle={}'.format(username)
        res = self.codeforces_http.get(url=url)
        res = json.loads(res.text)
        if res['status'] != 'OK':
            return []
        res = res['result']
        for rec in res:
            if rec['testset'] == 'PRETESTS':
                continue
            if rec.get('verdict') == 'OK':
                if rec['problem'].get('problemsetName'):
                    problem_pid = rec['problem']['index']
                else:
                    problem_pid = '{}{}'.format(rec['problem']['contestId'], rec['problem']['index'])
                accept_time = timestamp_to_str(rec['creationTimeSeconds'])
                accept_problem_list.append({
                    'oj': 'codeforces',
                    'problem_pid': problem_pid,
                    'accept_time': accept_time
                })
        return len(accept_problem_list)
