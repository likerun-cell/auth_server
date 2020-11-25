from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from JWT_Auth.utils import generate_jwt, JWT_EXPIRY, obtain_payload
from auth_server.settings import logger
from utils.decorator import view_handler


@method_decorator(view_handler, name='dispatch')
class Login(APIView):
    """登陆，返回jwt_token"""

    def post(self, request):
        user = {"user": request.data["user"],
                "password": request.data["password"]}
        jwt_token = generate_jwt(user)
        return Response({"data": jwt_token})


@method_decorator(view_handler, name='dispatch')
class Verify(APIView):
    """验证，返回"""

    def post(self, request):
        jwt = request.data["jwt"]
        payload = obtain_payload(jwt)
        if payload.get("errMsg"):
            return Response(payload, status=401)
        logger.info(f"数据库校验 {payload.get('user')}")
        return Response({"data": payload})
