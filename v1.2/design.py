# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(651, 502)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.checkBoxPizza = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBoxPizza.setFont(font)
        self.checkBoxPizza.setObjectName("checkBoxPizza")
        self.checkBoxPizza.stateChanged.connect(self.checked_item)  # проверка состояния чекбокса checkBoxPizza
        self.verticalLayout_6.addWidget(self.checkBoxPizza)
        self.checkBoxSalad = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBoxSalad.setFont(font)
        self.checkBoxSalad.setObjectName("checkBoxSalad")
        self.checkBoxSalad.stateChanged.connect(self.checked_item)  # проверка состояния чекбокса checkBoxSalad
        self.verticalLayout_6.addWidget(self.checkBoxSalad)
        self.checkBoxSaussage = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBoxSaussage.setFont(font)
        self.checkBoxSaussage.setObjectName("checkBoxSaussage")
        self.checkBoxSaussage.stateChanged.connect(self.checked_item)  # проверка состояния чекбокса checkBoxSaussage
        self.verticalLayout_6.addWidget(self.checkBoxSaussage)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.labelResult = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelResult.setFont(font)
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.verticalLayout.addWidget(self.labelResult)
        self.verticalLayout_7.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PyQt6 QCheckbox"))
        self.label.setText(_translate("Dialog", "Regular Tuna Price: 20 $"))
        self.label_2.setText(_translate("Dialog", "Select Extra"))
        self.checkBoxPizza.setText(_translate("Dialog", "Pizza : 3"))
        self.checkBoxSalad.setText(_translate("Dialog", "Salad : 4"))
        self.checkBoxSaussage.setText(_translate("Dialog", "Saussage : 5"))

    # проверка состояния чекбокса

    def checked_item(self):
        price = 20
        if self.checkBoxPizza.isChecked():
            price += 3
        if self.checkBoxSalad.isChecked():
            price += 4
        if self.checkBoxSaussage.isChecked():
            price += 5
        self.labelResult.setText("Total price is: {}".format(price))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
