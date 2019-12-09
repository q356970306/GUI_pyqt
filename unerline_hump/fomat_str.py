# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fomat_str.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!
"""

Author： jinshuai_qiao
Date： 2019/12/4
Desc：下划线驼峰互转
"""


import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(546, 422)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(30, 60, 181, 281))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(320, 60, 171, 281))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(214, 140, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(214, 200, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 40, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(320, 40, 71, 16))
        self.label_2.setObjectName("label_2")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "下划线驼峰互转"))
        self.pushButton.setText(_translate("Form", "下划线转驼峰"))
        self.pushButton_2.setText(_translate("Form", "驼峰转下划线"))
        self.label.setText(_translate("Form", "原始数据"))
        self.label_2.setText(_translate("Form", "转换后数据"))

    # 下划线转驼峰的点击事件
    def underline_to_hump_event(self):
        self.pushButton.clicked.connect(self.underline_to_hump)

    # 下划线转驼峰
    def underline_to_hump(self):
        org = self.textEdit.toPlainText()
        print('输入内容是：', org)
        for x in range(len(org)):
            if org[x] == '_' and x + 1 < len(org):
                org = org.replace(org[x] + org[x + 1], org[x + 1].upper(), 1) + ' '
            elif org[x] == '_':
                org = org.replace(org[x], '') + ' '
        print('转换内容是：', org)
        self.textEdit_2.setText(org.strip())

    # 驼峰转下划线的点击事件
    def hump_to_underline_event(self):
        self.pushButton_2.clicked.connect(self.hump_to_underline)

    # 驼峰转下划线
    def hump_to_underline(self):
        org = self.textEdit.toPlainText()
        print('输入内容是：', org)
        b = org
        for x in org:
            if x.isupper():
                b = org.replace(x, '_' + x.lower())
        print('转换内容是：', b)
        self.textEdit_2.setText(b)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setupUi(widget)
    ui.underline_to_hump_event()  # 执行类中的underline_to_hump_event方法,所有事件都得执行
    ui.hump_to_underline_event()     # 执行类中的hump_to_underline_event方法,所有事件都得执行
    widget.show()
    sys.exit(app.exec_())
