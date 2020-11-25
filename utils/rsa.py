import base64
import json

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

from utils import pub_path, pri_path


def rsa_encode(mes_dict: dict) -> str:
    """
    rsa非对称加密
    :param mes_dict: 需要加密的字典
    :return: base64字符串密文
    """
    mes_str = json.dumps(mes_dict)
    mes_bytes = mes_str.encode()
    with open(pub_path) as f:
        pub_key = RSA.importKey(f.read())
    pub = PKCS1_OAEP.new(pub_key)
    secret_bytes = pub.encrypt(mes_bytes)
    secret_base64 = base64.b64encode(secret_bytes)
    secret_str = secret_base64.decode()
    return secret_str


def rsa_decode(secret_str: str) -> dict:
    """
    rsa非对称解密
    :param secret_str: 需要解密的密文
    :return: 内容dict
    """
    secret_bytes = base64.b64decode(secret_str)
    with open(pri_path) as f:
        pri_key = RSA.importKey(f.read())
    pri = PKCS1_OAEP.new(pri_key)
    mes_bytes = pri.decrypt(secret_bytes)
    mes_str = mes_bytes.decode()
    mes_dict = json.loads(mes_str)
    return mes_dict
