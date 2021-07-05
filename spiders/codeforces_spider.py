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

    def get_user_rating(self, oj_username):
        url = 'http://codeforces.com/api/user.info?handles={}'.format(oj_username)
        rating = 0
        res = self.codeforces_http.get(url=url).json()
        if res['status'] == "OK":
            rating = res['result'][0]['rating']
        return rating

    def get_user_info(self, oj_username, accept_problems):
        username = oj_username.oj_username
        accept_problem_list = []
        url = 'http://codeforces.com/api/user.status?handle={}'.format(username)
        res = self.codeforces_http.get(url=url)
        res = json.loads(res.text)
        if res['status'] != 'OK':
            return {'success': False, 'data': []}
        res = res['result']
        success = False
        for rec in res:
            success = True
            if rec['testset'] == 'PRETESTS':
                continue
            if rec.get('verdict') == 'OK':
                if rec['problem'].get('problemsetName'):
                    problem_pid = rec['problem']['index']
                else:
                    problem_pid = '{}{}'.format(rec['problem']['contestId'], rec['problem']['index'])
                accept_time = timestamp_to_str(rec['creationTimeSeconds'])
                if accept_problems.get("codeforces-{}".format(problem_pid)) == accept_time:
                    continue
                accept_problem_list.append({
                    'oj': 'codeforces',
                    'problem_pid': problem_pid,
                    'accept_time': accept_time
                })
        return {'success': success, 'data': accept_problem_list}
