# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './date_dialog_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(984, 447)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.qlabel_top = QtWidgets.QLabel(Dialog)
        self.qlabel_top.setWordWrap(True)
        self.qlabel_top.setObjectName("qlabel_top")
        self.verticalLayout_3.addWidget(self.qlabel_top)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_after = QtWidgets.QLabel(Dialog)
        self.label_after.setAlignment(QtCore.Qt.AlignCenter)
        self.label_after.setObjectName("label_after")
        self.verticalLayout_5.addWidget(self.label_after)
        self.cw_after = QtWidgets.QCalendarWidget(Dialog)
        self.cw_after.setObjectName("cw_after")
        self.verticalLayout_5.addWidget(self.cw_after)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.qsp_after = QtWidgets.QSpinBox(Dialog)
        self.qsp_after.setObjectName("qsp_after")
        self.horizontalLayout_3.addWidget(self.qsp_after)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_before = QtWidgets.QLabel(Dialog)
        self.label_before.setAlignment(QtCore.Qt.AlignCenter)
        self.label_before.setObjectName("label_before")
        self.verticalLayout_4.addWidget(self.label_before)
        self.cw_before = QtWidgets.QCalendarWidget(Dialog)
        self.cw_before.setObjectName("cw_before")
        self.verticalLayout_4.addWidget(self.cw_before)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_before_days = QtWidgets.QLabel(Dialog)
        self.label_before_days.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_before_days.setObjectName("label_before_days")
        self.horizontalLayout_4.addWidget(self.label_before_days)
        self.qsp_before = QtWidgets.QSpinBox(Dialog)
        self.qsp_before.setObjectName("qsp_before")
        self.horizontalLayout_4.addWidget(self.qsp_before)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pb_accepted = QtWidgets.QPushButton(Dialog)
        self.pb_accepted.setObjectName("pb_accepted")
        self.horizontalLayout.addWidget(self.pb_accepted)
        self.pb_rejected = QtWidgets.QPushButton(Dialog)
        self.pb_rejected.setObjectName("pb_rejected")
        self.horizontalLayout.addWidget(self.pb_rejected)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.qlabel_top.setText(_translate("Dialog", "TextLabel"))
        self.label_after.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">After/Start</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "days ago:"))
        self.label_before.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Before/End</span></p></body></html>"))
        self.label_before_days.setText(_translate("Dialog", "days ago:"))
        self.pb_accepted.setText(_translate("Dialog", "Ok"))
        self.pb_rejected.setText(_translate("Dialog", "Cancel"))
