"""
一些公用的装饰器

def view_handler(func):
处理视图的返回值
"""

from functools import wraps

from utils.response_code import ERRCODE, errMsg


def view_handler(func):
    """
    处理视图的返回值
    :param func: 需要处理的视图方法
    :return:
    """

    @wraps(func)
    def inner(request, *args, **kwargs):
        res_dict = {
            "errCode": ERRCODE.OK,
            "errMsg": errMsg[ERRCODE.OK],
        }
        result = func(request, *args, **kwargs)
        if result.status_code == 401:
            res_dict.update({
                "errCode": ERRCODE.NOPERMISSION,
                "errMsg": f"{errMsg[ERRCODE.NOPERMISSION]} {result.data.get('errMsg', '-')} Refer to the payload "
                          f"generation rules",
            })
        result.data.update(res_dict)
        return result

    return inner
