import time

import jwt
from datetime import datetime, timedelta

from JWT_Auth.utils import JWT_EXPIRY
from utils import rsa_encode, rsa_decode


def generate_jwt(payload: dict, secret: str = "") -> jwt:
    """
    生成jwt_token
    :param payload: 需要编码的消息载荷
    :param secret: 加秘密钥
    :return: jwt_token
    """
    payload.update({"date": time.mktime(datetime.now().timetuple())})
    payload = {"secret": rsa_encode(payload)}
    jwt_token = jwt.encode(payload, secret, algorithm="HS256")
    return jwt_token.decode()


def obtain_payload(jwt_token: jwt, secret: str = "") -> dict:
    """
    将jwt_token 解密
    :param jwt_token: 需要解密的jwt_token
    :param secret: 解密所需的密钥
    :return: payload
    """
    try:
        payload = jwt.decode(jwt_token, secret, algorithms=["HS256"])
    except jwt.PyJWTError:
        return {"errMsg": "jwt_token content error"}
    else:
        if payload.get("secret"):
            payload = rsa_decode(payload["secret"])
            expiry = time.mktime((datetime.now() - timedelta(seconds=JWT_EXPIRY)).timetuple())
            if isinstance(payload.get("date"), (int, float)):
                if payload["date"] >= expiry:
                    return payload
        return {"errMsg": "payload content error"}
