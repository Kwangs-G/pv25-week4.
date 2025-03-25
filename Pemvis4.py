# from PyQt5 import QtCore, QtGui, QtWidgets
#
#
# class Ui_Dialog(object):
#     def setupUi(self, Dialog):
#         Dialog.setObjectName("Dialog")
#         Dialog.resize(640, 480)
#
#         self.label = QtWidgets.QLabel(Dialog)
#         self.label.setGeometry(QtCore.QRect(100, 40, 55, 16))
#         self.label.setObjectName("label")
#
#         self.label_2 = QtWidgets.QLabel(Dialog)
#         self.label_2.setGeometry(QtCore.QRect(100, 80, 55, 16))
#         self.label_2.setObjectName("label_2")
#
#         self.label_3 = QtWidgets.QLabel(Dialog)
#         self.label_3.setGeometry(QtCore.QRect(100, 120, 55, 16))
#         self.label_3.setObjectName("label_3")
#
#         self.label_4 = QtWidgets.QLabel(Dialog)
#         self.label_4.setGeometry(QtCore.QRect(100, 370, 200, 16))
#         self.label_4.setObjectName("label_4")
#
#         self.comboBox = QtWidgets.QComboBox(Dialog)
#         self.comboBox.setGeometry(QtCore.QRect(170, 40, 151, 22))
#         self.comboBox.setObjectName("comboBox")
#
#         self.lineEdit = QtWidgets.QLineEdit(Dialog)
#         self.lineEdit.setGeometry(QtCore.QRect(170, 80, 113, 22))
#         self.lineEdit.setObjectName("lineEdit")
#
#         self.spinBox = QtWidgets.QSpinBox(Dialog)
#         self.spinBox.setGeometry(QtCore.QRect(170, 120, 42, 22))
#         self.spinBox.setObjectName("spinBox")
#         self.spinBox.setSuffix("%")
#         self.spinBox.setRange(0, 50)  # Diskon bisa dari 0% - 50%
#
#         self.pushButton = QtWidgets.QPushButton(Dialog)
#         self.pushButton.setGeometry(QtCore.QRect(100, 160, 93, 28))
#         self.pushButton.setObjectName("pushButton")
#
#         self.pushButton_2 = QtWidgets.QPushButton(Dialog)
#         self.pushButton_2.setGeometry(QtCore.QRect(220, 160, 93, 28))
#         self.pushButton_2.setObjectName("pushButton_2")
#
#         self.textEdit = QtWidgets.QTextEdit(Dialog)
#         self.textEdit.setGeometry(QtCore.QRect(100, 200, 391, 151))
#         self.textEdit.setObjectName("textEdit")
#
#         self.retranslateUi(Dialog)
#         QtCore.QMetaObject.connectSlotsByName(Dialog)
#
#         self.products = {
#             "Bimoli  (RP. 20.000)": 20000,
#             "Burger  (RP. 15.000)": 15000,
#             "Minyak  (RP. 25.000)": 25000,
#             "Lifeboy (RP. 5000)": 5000,
#             "Indomie (RP. 3500)": 3500
#         }
#         self.comboBox.addItems(self.products.keys())
#
#         self.total = 0
#         self.pushButton.clicked.connect(self.add_to_cart)
#         self.pushButton_2.clicked.connect(self.clear_cart)
#
#     def retranslateUi(self, Dialog):
#         _translate = QtCore.QCoreApplication.translate
#         Dialog.setWindowTitle(_translate("Dialog", "POS Application"))
#         self.label.setText(_translate("Dialog", "Produk"))
#         self.label_2.setText(_translate("Dialog", "Quantity"))
#         self.label_3.setText(_translate("Dialog", "Discount"))
#         self.pushButton.setText(_translate("Dialog", "Add to Cart"))
#         self.pushButton_2.setText(_translate("Dialog", "Clear"))
#         self.label_4.setText(_translate("Dialog", "Total: Rp. 0"))
#
#     def add_to_cart(self):
#         product = self.comboBox.currentText()
#         quantity_text = self.lineEdit.text()
#
#         if not quantity_text.isdigit() or int(quantity_text) <= 0:
#             self.textEdit.append("⚠️ Quantity harus angka positif!")
#             return
#
#         quantity = int(quantity_text)
#         discount = self.spinBox.value() / 100
#         price = self.products[product]
#
#         total_price = quantity * price * (1 - discount)
#         self.total += total_price
#
#         self.textEdit.append(f"{product} (Rp. {price:,}) - {quantity} x Rp. {price:,} (disc {int(discount * 100)}%)")
#
#         self.label_4.setText(f"Total: Rp. {self.total:,.0f}")
#
#     def clear_cart(self):
#         self.textEdit.clear()
#         self.total = 0
#         self.label_4.setText("Total: Rp. 0")
#
#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 40, 55, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 80, 55, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 120, 55, 16))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(100, 370, 200, 16))
        self.label_4.setObjectName("label_4")

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(170, 40, 151, 22))
        self.comboBox.setObjectName("comboBox")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(170, 80, 113, 22))
        self.lineEdit.setObjectName("lineEdit")

        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(170, 120, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setSuffix("%")
        self.spinBox.setRange(0, 50)  # Diskon bisa dari 0% - 50%

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 160, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 160, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(100, 200, 391, 151))
        self.textEdit.setObjectName("textEdit")

        # Label tambahan untuk Nama dan NIM
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(100, 400, 200, 16))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(100, 420, 200, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.products = {
            "Bimoli  (RP. 20.000)": 20000,
            "Burger  (RP. 15.000)": 15000,
            "Minyak  (RP. 25.000)": 25000,
            "Lifeboy (RP. 5000)": 5000,
            "Indomie (RP. 3500)": 3500
        }
        self.comboBox.addItems(self.products.keys())

        self.total = 0
        self.pushButton.clicked.connect(self.add_to_cart)
        self.pushButton_2.clicked.connect(self.clear_cart)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "POS Application"))
        self.label.setText(_translate("Dialog", "Produk"))
        self.label_2.setText(_translate("Dialog", "Quantity"))
        self.label_3.setText(_translate("Dialog", "Discount"))
        self.pushButton.setText(_translate("Dialog", "Add to Cart"))
        self.pushButton_2.setText(_translate("Dialog", "Clear"))
        self.label_4.setText(_translate("Dialog", "Total: Rp. 0"))
        self.label_5.setText(_translate("Dialog", "Nama: Fernandao Kwangtama Tekayadi "))
        self.label_6.setText(_translate("Dialog", "NIM: F1D022120"))

    def add_to_cart(self):
        product = self.comboBox.currentText()
        quantity_text = self.lineEdit.text()

        if not quantity_text.isdigit() or int(quantity_text) <= 0:
            self.textEdit.append("⚠️ Quantity harus angka positif!")
            return

        quantity = int(quantity_text)
        discount = self.spinBox.value() / 100
        price = self.products[product]

        total_price = quantity * price * (1 - discount)
        self.total += total_price

        self.textEdit.append(f"{product} (Rp. {price:,}) - {quantity} x Rp. {price:,} (disc {int(discount * 100)}%)")

        self.label_4.setText(f"Total: Rp. {self.total:,.0f}")

    def clear_cart(self):
        self.textEdit.clear()
        self.total = 0
        self.label_4.setText("Total: Rp. 0")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
