# Form implementation generated from reading ui file 'Window.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 100, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(parent=Form)
        self.radioButton.setGeometry(QtCore.QRect(80, 30, 100, 20))
        self.radioButton.setObjectName("radioButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.radioButton.setText(_translate("Form", "RadioButton"))
