# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caruer_info.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!
import json
import sys

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from flask import Response

from util_package import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(494, 545)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(130, 110, 111, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 140, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 80, 231, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 50, 71, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 20, 71, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 20, 41, 16))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 50, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(60, 80, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(60, 110, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(60, 140, 54, 12))
        self.label_5.setObjectName("label_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(130, 170, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(60, 170, 54, 12))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 170, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(40, 270, 421, 241))
        self.textEdit.setObjectName("textEdit")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(40, 250, 54, 12))
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(60, 210, 211, 20))
        self.lineEdit_7.setToolTipDuration(5)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 210, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 210, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        self.headers = {'content-type': "application/json"}
        self.apiUser = envConfig.com_info['apiUser']
        self.apiEnc = envConfig.com_info['apiEnc']
        self.apiKey = envConfig.com_info['apiKey']
        self.Enc_md5org = envConfig.com_info['apiKey'] + envConfig.com_info['apiUser']

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEdit_5, self.lineEdit_4)
        Form.setTabOrder(self.lineEdit_4, self.lineEdit_3)
        Form.setTabOrder(self.lineEdit_3, self.lineEdit)
        Form.setTabOrder(self.lineEdit, self.lineEdit_2)
        Form.setTabOrder(self.lineEdit_2, self.pushButton)
        Form.setTabOrder(self.pushButton, self.lineEdit_6)
        Form.setTabOrder(self.lineEdit_6, self.pushButton_2)
        Form.setTabOrder(self.pushButton_2, self.lineEdit_7)
        Form.setTabOrder(self.lineEdit_7, self.pushButton_3)
        Form.setTabOrder(self.pushButton_3, self.pushButton_4)
        Form.setTabOrder(self.pushButton_4, self.textEdit)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "私有化运营商"))
        self.label.setText(_translate("Form", "运营商"))
        self.label_2.setText(_translate("Form", "姓名"))
        self.label_3.setText(_translate("Form", "身份证号"))
        self.label_4.setText(_translate("Form", "手机号"))
        self.label_5.setText(_translate("Form", "密码"))
        self.label_6.setText(_translate("Form", "验证码"))
        self.pushButton.setText(_translate("Form", "创建任务"))
        self.pushButton_2.setText(_translate("Form", "提交"))
        self.label_7.setText(_translate("Form", "响应"))
        self.pushButton_3.setText(_translate("Form", "查询状态"))
        self.pushButton_4.setText(_translate("Form", "查询数据"))

    def is_Chinese(self, word):
        for ch in word:
            if '\u4e00' <= ch <= '\u9fff':
                return True
        return False

    def is_check(self, param: dict):
        a = param.values()
        for x in a:
            print(x)
            if x.strip().isalnum() or self.is_Chinese(x.strip()):
                print('输入正常')
            else:
                print('必填项未填')
                return False
        return True

    def create(self):
        """
        创建任务接口
        :return:
        """

        url = 'http://10.0.221.96:8089/api/task/create'
        param = {
            "channelId": "1",
            "idCard": self.lineEdit_3.text(),
            "idCardNum": self.lineEdit_3.text(),
            "name": self.lineEdit_4.text(),
            "phone": self.lineEdit.text(),
            "pwd": self.lineEdit_2.text(),
            "realName": self.lineEdit_4.text()
        }
        print(param)
        if self.is_check(param):
            param_str = str(param)
            param_encry = str(get_rsa_sign(param_str))

            ti = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            sign = get_md5_sign(envConfig.com_info['apiUser'] + ti + ti + envConfig.com_info['apiKey'])

            data = {
                "apiEnc": self.apiEnc,
                "apiName": "shanghaitelecom",
                "code": "1217",
                "sign": sign,
                "time": ti,
                "terminalId": "",
                "params": param_encry,
                "apiUser": self.apiUser,
                "taskId": ti
            }

            res = requests.post(url, data=json.dumps(data), headers=self.headers)
            resp = res.text
            token = json.loads(resp)['detail']['token']
            print(token)
            print('创建任务请求参数：', data)
            print('创建任务返回结果：', resp)

            self.lineEdit_7.setText(token)
            self.textEdit.setText(resp)
        else:
            self.textEdit.setText('必填项未填写')

    def get_data(self):
        """
        查询数据接口
        :param token:
        :return:
        """
        token = self.lineEdit_7.text()
        param = {
            "apiUser": self.apiUser,
            "apiEnc": self.apiEnc
        }
        if token.isalnum():
            url = 'http://10.0.221.96:8089/api/data/' + token
            res = requests.get(url, param, headers=self.headers)
            resp = res.text
            print('查询数据请求参数：', param)
            print('查询数据返回结果：', resp)
            self.textEdit.setText(resp)
        else:
            self.textEdit.setText('token未正确填写')

    def get_status(self):
        """
        查询状态接口
        :param token:
        :return:
        """
        token = self.lineEdit_7.text()
        print('123:', token)
        param = {
            "apiUser": self.apiUser,
            "apiEnc": get_md5_sign(self.Enc_md5org + token)
        }
        if token.isalnum():
            url = 'http://10.0.221.96:8089/api/task/status/' + token
            res = requests.get(url, param, headers=self.headers)
            resp = res.text
            # resp = Response(json.dumps(res), mimetype='application/json')
            print('查询状态请求参数：', param)
            print('查询状态返回结果：', resp)
            self.textEdit.setText(resp)
        else:
            self.textEdit.setText('token未正确填写')

    def message(self):
        """
        提交消息接口，如短信验证码
        code	类型	描述
        200002	输入	输入短信验证码
        200009	输入	输入图片验证码
        200019	输入	输入答案
        200003	刷新	重新发送动态验证码
        200008	刷新	刷新图片验证码
        200013	刷新	刷新二维码
        :param token:
        :param code:
        :return:
        """
        token = self.lineEdit_7.text()
        code = self.lineEdit_6.text()
        param = {
            "apiUser": self.apiUser,
            "apiEnc": get_md5_sign(self.Enc_md5org + token),
            "token": token,
            "code": "200002",
            "value": code
        }
        if self.is_check(param):
            url = 'http://10.0.221.96:8089/api/task/message'
            res = requests.post(url, data=json.dumps(param), headers=self.headers)
            resp = res.text
            print('提交验证码请求参数：', param)
            print('验证码返回结果：', resp)
            self.textEdit.setText(resp)
        else:
            self.textEdit.setText('必填项未填写')

    def ui_create(self):
        self.pushButton.clicked.connect(self.create)

    def ui_get_status(self):
        self.pushButton_3.clicked.connect(self.get_status)

    def ui_get_data(self):
        self.pushButton_4.clicked.connect(self.get_data)

    def ui_message(self):
        self.pushButton_2.clicked.connect(self.message)


if __name__ == "__main__":
    #  0120454741440069632、0120452652173361152、0122250064949673984
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setupUi(widget)
    ui.ui_create()  # 执行类中的underline_to_hump_event方法,所有事件都得执行
    ui.ui_get_data()
    ui.ui_get_status()
    ui.ui_message()
    widget.show()
    sys.exit(app.exec_())
