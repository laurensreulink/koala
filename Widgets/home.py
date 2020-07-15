from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2.QtCore import Signal

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(900, 600))
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 90, 661, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.ButtonBox = QtWidgets.QGroupBox(self.groupBox_4)
        self.ButtonBox.setGeometry(QtCore.QRect(20, 10, 181, 231))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonBox.sizePolicy().hasHeightForWidth())
        self.ButtonBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonBox.setFont(font)
        self.ButtonBox.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.ButtonBox.setFlat(False)
        self.ButtonBox.setCheckable(False)
        self.ButtonBox.setObjectName("ButtonBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ButtonBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.ButtonBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.btn_qck_clf = QtWidgets.QPushButton(self.ButtonBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.btn_qck_clf.setFont(font)
        self.btn_qck_clf.setObjectName("btn_qck_clf")
        self.verticalLayout_2.addWidget(self.btn_qck_clf)
        self.btn_qck_reg = QtWidgets.QPushButton(self.ButtonBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.btn_qck_reg.setFont(font)
        self.btn_qck_reg.setObjectName("btn_qck_reg")
        self.verticalLayout_2.addWidget(self.btn_qck_reg)
        self.line = QtWidgets.QFrame(self.ButtonBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.label_3 = QtWidgets.QLabel(self.ButtonBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.ButtonBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.ButtonBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_2.setGeometry(QtCore.QRect(210, 10, 241, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.line_2 = QtWidgets.QFrame(self.groupBox_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.btn_pred_clf = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.btn_pred_clf.setFont(font)
        self.btn_pred_clf.setObjectName("btn_pred_clf")
        self.verticalLayout_3.addWidget(self.btn_pred_clf)
        self.btn_pred_reg = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.btn_pred_reg.setFont(font)
        self.btn_pred_reg.setObjectName("btn_pred_reg")
        self.verticalLayout_3.addWidget(self.btn_pred_reg)
        self.line_3 = QtWidgets.QFrame(self.groupBox_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.btn_risk = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.btn_risk.setFont(font)
        self.btn_risk.setObjectName("btn_risk")
        self.verticalLayout_3.addWidget(self.btn_risk)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_3.setGeometry(QtCore.QRect(460, 10, 173, 110))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_recommend_clf = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.btn_recommend_clf.setFont(font)
        self.btn_recommend_clf.setObjectName("btn_recommend_clf")
        self.verticalLayout.addWidget(self.btn_recommend_clf)
        self.btn_recommend_reg = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.btn_recommend_reg.setFont(font)
        self.btn_recommend_reg.setObjectName("btn_recommend_reg")
        self.verticalLayout.addWidget(self.btn_recommend_reg)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 337, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 584, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ButtonBox.setTitle(_translate("Form", "Data Mining Tools"))
        self.label_2.setText(_translate("Form", "Quick Training"))
        self.btn_qck_clf.setText(_translate("Form", "Classification"))
        self.btn_qck_reg.setText(_translate("Form", "Regression"))
        self.label_3.setText(_translate("Form", "Advanced Training"))
        self.pushButton_2.setText(_translate("Form", "Classification"))
        self.pushButton_3.setText(_translate("Form", "Regression"))
        self.groupBox_2.setTitle(_translate("Form", "Prediction Tools"))
        self.pushButton_4.setText(_translate("Form", "Preprocessing for Prediction"))
        self.btn_pred_clf.setText(_translate("Form", "Categorical"))
        self.btn_pred_reg.setText(_translate("Form", "Continuous"))
        self.btn_risk.setText(_translate("Form", "Risk Analysis"))
        self.groupBox_3.setTitle(_translate("Form", "Recommendations"))
        self.btn_recommend_clf.setText(_translate("Form", "Classification Model"))
        self.btn_recommend_reg.setText(_translate("Form", "Regressional Model"))
        self.label.setText(_translate("Form", "Welcome to the <b>Koala</b> Process Prediction Environment.  "))
        self.label_4.setText(_translate("Form", "Click on of the option below to continue, or use the menu bar to navigate around the application."))