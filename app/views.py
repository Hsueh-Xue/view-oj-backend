from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework.response import Response
from oj.models import OJ


class InitView(APIView):
    authentication_classes = []

    @staticmethod
    def get(request, *args, **kwargs):
        try:
            oj = OJ()
            oj.name = 'codeforces'
            oj.save()
            return Response("success")
        except Exception as e:
            return Response({
                'status': 204,
                'msg': '遇到了异常错误',
                'err': e.args
            })
