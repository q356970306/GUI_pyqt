# coding=utf-8

"""
Author： jinshuai_qiao
Date： 2019/12/4
Desc：
"""

param = {
    "channelId": "1",
    "idCard": '123',
    "idCardNum": '2',
    "name": '2',
    "phone": '321',
    "pwd": 'asd ',
    "realName": '是'
}


def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


def is_check(param: dict):
    a = param.values()
    for x in a:
        print(x)
        if x.strip().isalnum() or is_Chinese(x.strip()):
            print('输入正常')
        else:
            print('必填项未填')
            return False
    return True
a= is_check(param)
print(a)