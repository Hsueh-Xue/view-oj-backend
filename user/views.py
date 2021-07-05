from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import User
from oj.models import OJ, OJUser


class AddUserView(APIView):

    @staticmethod
    def post(request, *args, **kwargs):
        try:
            username = request.data.get('username')
            print(username)
            # username = 'Dup4'
            user = User()
            user.nickname = username
            user.username = username
            user.password = make_password(username)
            user.save()

            oj = OJ.objects.filter(id=1).first()
            oj_user = OJUser()
            oj_user.oj = oj
            oj_user.user = user
            oj_user.oj_username = username
            oj_user.save()
            return Response({
                'code': 0,
                'msg': '创建成功'
            })
        except Exception as e:
            return Response({
                'code': 204,
                'msg': '遇到了异常错误',
                'err': e.args
            })


class GetRatingView(APIView):

    @staticmethod
    def get(request, *args, **kwargs):
        try:
            oj = OJ.objects.filter(id=1, status=0).first()
            if not oj:
                return Response({
                    'code': 204,
                    'msg': 'cf不存在'
                })
            oj_user_list = OJUser.objects.filter(oj=oj, status=0).all()

            data = []

            for item in oj_user_list:
                data_item = {'username': item.oj_username, 'rating': item.oj_rating, 'cnt': item.problem_count,
                             'nickname': item.user.nickname, 'last_cf_date': item.last_login}
                data.append(data_item)

            return Response({
                'code': 0,
                'msg': '创建成功',
                'data': data
            })
        except Exception as e:
            return Response({
                'code': 204,
                'msg': '遇到了异常错误',
                'err': e.args
            })
