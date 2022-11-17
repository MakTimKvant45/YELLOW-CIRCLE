from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(725, 554)
        self.draw_btn = QtWidgets.QPushButton(Form)
        self.draw_btn.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.draw_btn.setObjectName("draw_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.draw_btn.setText(_translate("Form", "Круг +"))
