from django.contrib.auth.hashers import make_password, check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import User
from oj.models import OJ, OJUser


class AddUserView(APIView):

    @staticmethod
    def post(request, *args, **kwargs):
        try:
            username = request.data.get('username')
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
                data_item = {'username': item.user.username, 'rating': item.oj_rating, 'cnt': item.problem_count,
                             'nickname': item.user.nickname, 'last_cf_date': item.last_login,
                             'contest_cnt': item.user.contest_num, 'handle': item.oj_username}
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


class AuthView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            user = User.objects.filter(username=username, status=0).first()
            if not user:
                return Response({
                    'code': 404,
                    'msg': '账号或密码不正确'
                })
            if check_password(password, user.password):
                data = {
                    'id': user.id,
                    'username': user.username,
                    'nickname': user.nickname
                }
                return Response({
                    'code': 0,
                    'msg': '登录成功',
                    'data': data
                })
            else:
                return Response({
                    'code': 404,
                    'msg': '账号或密码不正确'
                })
        except Exception as e:
            return Response({
                'code': 204,
                'msg': '遇到了异常错误',
                'err': e.args
            })


class ModifyNicknameView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            id = request.data.get('id')
            nickname = request.data.get('nickname')
            user = User.objects.filter(id=id, status=0).first()
            if not user:
                return Response({
                    'code': 404,
                    'msg': '用户不存在'
                })
            user.nickname = nickname
            user.save()
            return Response({
                'code': 0,
                'msg': '修改成功'
            })
        except Exception as e:
            return Response({
                'code': 204,
                'msg': '遇到了异常错误',
                'err': e.args
            })


class ModifyPasswordView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            id = request.data.get('id')
            old_password = request.data.get('oldPassword')
            new_password = request.data.get('newPassword')
            user = User.objects.filter(id=id, status=0).first()
            if not user:
                return Response({
                    'code': 404,
                    'msg': '用户不存在'
                })
            if check_password(old_password, user.password):
                user.password = make_password(new_password)
                user.save()
            else:
                return Response({
                    'code': 204,
                    'msg': '原密码不正确'
                })
            return Response({
                'code': 0,
                'msg': '修改成功'
            })
        except Exception as e:
            return Response({
                'code': 204,
                'msg': '遇到了异常错误',
                'err': e.args
            })


class ModifyCodeforcesView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            id = request.data.get('id')
            handle = request.data.get('handle')

            user = User.objects.filter(id=id, status=0).first()
            if not user:
                return Response({
                    'code': 404,
                    'msg': '用户不存在'
                })

            oj = OJ.objects.filter(id=1, status=0).first()
            if not oj:
                return Response({
                    'code': 404,
                    'msg': 'OJ不存在'
                })
            oj_user = OJUser.objects.filter(user=user, oj=oj, status=0).first()
            if not oj_user:
                oj_user = OJUser()
            oj_user.oj_username = handle
            oj_user.save()
            return Response({
                'code': 0,
                'msg': '修改成功'
            })
        except Exception as e:
            return Response({
                'code': 204,
                'msg': '遇到了异常错误',
                'err': e.args
            })
