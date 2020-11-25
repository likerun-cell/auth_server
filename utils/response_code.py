"""
API response code dict
"""
from enum import Enum


class ERRCODE:
    OK = 200
    SERVERERROR = 500
    NOPERMISSION = 600
    PARAMETERSILLEGAL = 1001
    NOSERVICE = 1002


errMsg = {
    ERRCODE.OK: "成功",
    ERRCODE.SERVERERROR: "服务器错误",
    ERRCODE.NOPERMISSION: "鉴权失败",
    ERRCODE.PARAMETERSILLEGAL: "参数非法",
    ERRCODE.NOSERVICE: "无服务"
}


class RESULTCODE:
    OK = "200"
    FAILURE = "500"


resultMessage = {
    RESULTCODE.OK: "成功",
    RESULTCODE.FAILURE: "生成token失败，请检查密码或用户名"
}
