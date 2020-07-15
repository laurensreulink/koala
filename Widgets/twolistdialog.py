from PySide2 import QtCore, QtGui, QtWidgets

class Ui_TwoListDialog(object):
    events = []

    def setupUi(self, TwoListDialog):
        TwoListDialog.setObjectName("TwoListDialog")
        TwoListDialog.resize(895, 650)
        self.verticalLayout = QtWidgets.QVBoxLayout(TwoListDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(TwoListDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.layoutWidget = QtWidgets.QWidget(self.tab_1)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 571, 391))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.combo_uid = QtWidgets.QComboBox(self.layoutWidget)
        self.combo_uid.setObjectName("combo_uid")
        self.verticalLayout_2.addWidget(self.combo_uid)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.combo_event = QtWidgets.QComboBox(self.layoutWidget)
        self.combo_event.setObjectName("combo_event")
        self.verticalLayout_2.addWidget(self.combo_event)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.combo_time = QtWidgets.QComboBox(self.layoutWidget)
        self.combo_time.setObjectName("combo_time")
        self.verticalLayout_2.addWidget(self.combo_time)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.combo_label = QtWidgets.QComboBox(self.layoutWidget)
        self.combo_label.setObjectName("combo_label")
        self.verticalLayout_2.addWidget(self.combo_label)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.verticalLayout_7.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_confirm = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_confirm.setObjectName("btn_confirm")
        self.horizontalLayout.addWidget(self.btn_confirm)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(20, -10, 821, 61))
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(490, 50, 201, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(20, 50, 201, 16))
        self.label_9.setObjectName("label_9")
        self.listWidget_Cat_Excl = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_Cat_Excl.setGeometry(QtCore.QRect(20, 70, 351, 450))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_Cat_Excl.sizePolicy().hasHeightForWidth())
        self.listWidget_Cat_Excl.setSizePolicy(sizePolicy)
        self.listWidget_Cat_Excl.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_Cat_Excl.setObjectName("listWidget_Cat_Excl")
        self.listWidget_Cat_Incl = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_Cat_Incl.setGeometry(QtCore.QRect(490, 70, 351, 450))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_Cat_Incl.sizePolicy().hasHeightForWidth())
        self.listWidget_Cat_Incl.setSizePolicy(sizePolicy)
        self.listWidget_Cat_Incl.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_Cat_Incl.setObjectName("listWidget_Cat_Incl")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(390, 90, 77, 387))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btn_cat_right = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cat_right.sizePolicy().hasHeightForWidth())
        self.btn_cat_right.setSizePolicy(sizePolicy)
        self.btn_cat_right.setObjectName("btn_cat_right")
        self.verticalLayout_6.addWidget(self.btn_cat_right)
        self.btn_cat_all_right = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cat_all_right.sizePolicy().hasHeightForWidth())
        self.btn_cat_all_right.setSizePolicy(sizePolicy)
        self.btn_cat_all_right.setObjectName("btn_cat_all_right")
        self.verticalLayout_6.addWidget(self.btn_cat_all_right)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem5)
        self.btn_cat_all_left = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cat_all_left.sizePolicy().hasHeightForWidth())
        self.btn_cat_all_left.setSizePolicy(sizePolicy)
        self.btn_cat_all_left.setObjectName("btn_cat_all_left")
        self.verticalLayout_6.addWidget(self.btn_cat_all_left)
        self.btn_cat_left = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cat_left.sizePolicy().hasHeightForWidth())
        self.btn_cat_left.setSizePolicy(sizePolicy)
        self.btn_cat_left.setObjectName("btn_cat_left")
        self.verticalLayout_6.addWidget(self.btn_cat_left)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 90, 77, 387))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_con_right = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_con_right.sizePolicy().hasHeightForWidth())
        self.btn_con_right.setSizePolicy(sizePolicy)
        self.btn_con_right.setObjectName("btn_con_right")
        self.verticalLayout_3.addWidget(self.btn_con_right)
        self.btn_con_all_right = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_con_all_right.sizePolicy().hasHeightForWidth())
        self.btn_con_all_right.setSizePolicy(sizePolicy)
        self.btn_con_all_right.setObjectName("btn_con_all_right")
        self.verticalLayout_3.addWidget(self.btn_con_all_right)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem6)
        self.btn_con_all_left = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_con_all_left.sizePolicy().hasHeightForWidth())
        self.btn_con_all_left.setSizePolicy(sizePolicy)
        self.btn_con_all_left.setObjectName("btn_con_all_left")
        self.verticalLayout_3.addWidget(self.btn_con_all_left)
        self.btn_con_left = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_con_left.sizePolicy().hasHeightForWidth())
        self.btn_con_left.setSizePolicy(sizePolicy)
        self.btn_con_left.setObjectName("btn_con_left")
        self.verticalLayout_3.addWidget(self.btn_con_left)
        self.listWidget_Con_Excl = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_Con_Excl.setGeometry(QtCore.QRect(20, 70, 351, 450))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_Con_Excl.sizePolicy().hasHeightForWidth())
        self.listWidget_Con_Excl.setSizePolicy(sizePolicy)
        self.listWidget_Con_Excl.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_Con_Excl.setObjectName("listWidget_Con_Excl")
        self.listWidget_Con_Incl = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_Con_Incl.setGeometry(QtCore.QRect(490, 70, 351, 450))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_Con_Incl.sizePolicy().hasHeightForWidth())
        self.listWidget_Con_Incl.setSizePolicy(sizePolicy)
        self.listWidget_Con_Incl.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_Con_Incl.setObjectName("listWidget_Con_Incl")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(20, -10, 821, 61))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(20, 50, 201, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(490, 50, 201, 16))
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.listWidget_events = QtWidgets.QListWidget(self.tab_7)
        self.listWidget_events.setGeometry(QtCore.QRect(20, 70, 351, 450))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_events.sizePolicy().hasHeightForWidth())
        self.listWidget_events.setSizePolicy(sizePolicy)
        self.listWidget_events.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_events.setObjectName("listWidget_events")
        self.label_21 = QtWidgets.QLabel(self.tab_7)
        self.label_21.setGeometry(QtCore.QRect(20, 50, 271, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.tab_7)
        self.label_22.setGeometry(QtCore.QRect(490, 50, 201, 16))
        self.label_22.setObjectName("label_22")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_7)
        self.groupBox_6.setGeometry(QtCore.QRect(390, 90, 77, 387))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setFlat(True)
        self.groupBox_6.setCheckable(False)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.btn_con_right_3 = QtWidgets.QPushButton(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_con_right_3.sizePolicy().hasHeightForWidth())
        self.btn_con_right_3.setSizePolicy(sizePolicy)
        self.btn_con_right_3.setObjectName("btn_con_right_3")
        self.verticalLayout_10.addWidget(self.btn_con_right_3)
        self.btn_con_all_right_3 = QtWidgets.QPushButton(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_con_all_right_3.sizePolicy().hasHeightForWidth())
        self.btn_con_all_right_3.setSizePolicy(sizePolicy)
        self.btn_con_all_right_3.setObjectName("btn_con_all_right_3")
        self.verticalLayout_10.addWidget(self.btn_con_all_right_3)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_10.addItem(spacerItem7)
        self.btn_con_all_left_3 = QtWidgets.QPushButton(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_con_all_left_3.sizePolicy().hasHeightForWidth())
        self.btn_con_all_left_3.setSizePolicy(sizePolicy)
        self.btn_con_all_left_3.setObjectName("btn_con_all_left_3")
        self.verticalLayout_10.addWidget(self.btn_con_all_left_3)
        self.btn_con_left_3 = QtWidgets.QPushButton(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_con_left_3.sizePolicy().hasHeightForWidth())
        self.btn_con_left_3.setSizePolicy(sizePolicy)
        self.btn_con_left_3.setObjectName("btn_con_left_3")
        self.verticalLayout_10.addWidget(self.btn_con_left_3)
        self.listWidget_recs = QtWidgets.QListWidget(self.tab_7)
        self.listWidget_recs.setGeometry(QtCore.QRect(490, 70, 351, 450))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_recs.sizePolicy().hasHeightForWidth())
        self.listWidget_recs.setSizePolicy(sizePolicy)
        self.listWidget_recs.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_recs.setObjectName("listWidget_recs")
        self.label_23 = QtWidgets.QLabel(self.tab_7)
        self.label_23.setGeometry(QtCore.QRect(20, -10, 821, 61))
        self.label_23.setWordWrap(True)
        self.label_23.setObjectName("label_23")
        self.tabWidget.addTab(self.tab_7, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(TwoListDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        #SIGNALS/EVENTS/TRIGGERS
        self.btn_cat_left.clicked.connect(self.buttonClickedCatLeft)
        self.btn_cat_right.clicked.connect(self.buttonClickedCatRight)
        self.btn_cat_all_left.clicked.connect(self.buttonClickedCatAllLeft)
        self.btn_cat_all_right.clicked.connect(self.buttonClickedCatAllRight)
        self.btn_con_left.clicked.connect(self.buttonClickedConLeft)
        self.btn_con_right.clicked.connect(self.buttonClickedConRight)
        self.btn_con_all_left.clicked.connect(self.buttonClickedConAllLeft)
        self.btn_con_all_right.clicked.connect(self.buttonClickedConAllRight)
        self.btn_confirm.clicked.connect(self.buttonConfirm)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.retranslateUi(TwoListDialog)
        self.tabWidget.setCurrentIndex(0)
        self.tab_2.setEnabled(False)
        self.tab_3.setEnabled(False)
        self.tab_7.setEnabled(False)
        QtCore.QMetaObject.connectSlotsByName(TwoListDialog)

    def retranslateUi(self, TwoListDialog):
        _translate = QtCore.QCoreApplication.translate
        TwoListDialog.setWindowTitle(_translate("TwoListDialog", "Dialog"))
        self.label_2.setText(_translate("TwoListDialog", "Select the column that represents the unique identifier of the process:"))
        self.label.setText(_translate("TwoListDialog", "Select the column that represents the events in the process:"))
        self.label_10.setText(_translate("TwoListDialog", "Select the column that holds the timestamp of the event. "))
        self.label_3.setText(_translate("TwoListDialog", "Select the dependent variable that will be used as the label to train the model:"))
        self.btn_confirm.setText(_translate("TwoListDialog", "Confirm"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("TwoListDialog", "General Variable Settings"))
        self.label_7.setText(_translate("TwoListDialog", "<html><head/><body><p>Select the (independent) <span style=\" font-weight:600;\">categorical</span> variables that must be included in the training of the estimator from the left hand side list below and move them to the right hand side. Make sure to set the other variables first. Otherwise they can still show up in the list below.</p></body></html>"))
        self.label_8.setText(_translate("TwoListDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Selected Attributes</span></p></body></html>"))
        self.label_9.setText(_translate("TwoListDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Available Attributes</span></p></body></html>"))
        self.btn_cat_right.setText(_translate("TwoListDialog", ">"))
        self.btn_cat_all_right.setText(_translate("TwoListDialog", ">>"))
        self.btn_cat_all_left.setText(_translate("TwoListDialog", "<<"))
        self.btn_cat_left.setText(_translate("TwoListDialog", "<"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("TwoListDialog", "Categorical Variable Selection"))
        self.btn_con_right.setText(_translate("TwoListDialog", ">"))
        self.btn_con_all_right.setText(_translate("TwoListDialog", ">>"))
        self.btn_con_all_left.setText(_translate("TwoListDialog", "<<"))
        self.btn_con_left.setText(_translate("TwoListDialog", "<"))
        self.label_4.setText(_translate("TwoListDialog", "<html><head/><body><p>Select the (independent) <span style=\" font-weight:600;\">continuous</span> variables that must be included in the training of the estimator from the left hand side list below and move them to the right hand side. Make sure to set the other variables first. Otherwise they can still show up in the list below.</p></body></html>"))
        self.label_5.setText(_translate("TwoListDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Available Attributes</span></p></body></html>"))
        self.label_6.setText(_translate("TwoListDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Selected Attributes</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("TwoListDialog", "Continuous Variable Selection"))
        self.label_21.setText(_translate("TwoListDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Available Events for Recommendations</span></p></body></html>"))
        self.label_22.setText(_translate("TwoListDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Selected Events </span></p></body></html>"))
        self.btn_con_right_3.setText(_translate("TwoListDialog", ">"))
        self.btn_con_all_right_3.setText(_translate("TwoListDialog", ">>"))
        self.btn_con_all_left_3.setText(_translate("TwoListDialog", "<<"))
        self.btn_con_left_3.setText(_translate("TwoListDialog", "<"))
        self.label_23.setText(_translate("TwoListDialog", "<html><head/><body><p>Select the events from the list to be used in the recommender system as recommendations. All of these events will be used in the training of the model plus the events selected as the K best events. </p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("TwoListDialog", "Events for Recommendation Selection"))

    def initiateLists(self, columns):
        self.combo_uid.addItem("")
        self.combo_uid.addItems(columns)
        self.combo_label.addItem("")
        self.combo_label.addItems(columns)
        self.combo_event.addItem("")
        self.combo_event.addItems(columns)
        self.combo_time.addItem("")
        self.combo_time.addItems(columns)
        self.listWidget_Cat_Excl.addItems(columns)
        self.listWidget_Cat_Incl.addItems([])
        self.listWidget_Con_Excl.addItems(columns)
        self.listWidget_Con_Incl.addItems([])

    def initiateEvents(self):
        self.listWidget_events.addItems(self.events)
        self.listWidget_recs.addItems([])

    def buttonClickedCatRight(self):
        selection = self.listWidget_Cat_Excl.selectedItems()
        change = []
        for i in selection:
            change.append(i.text())
        self.listWidget_Cat_Incl.addItems(change)
        for item in selection:
            self.listWidget_Cat_Excl.takeItem(self.listWidget_Cat_Excl.row(item))

        for c in change:
            self.deleteItem(c, self.listWidget_Con_Excl)
        for c in change:
            self.deleteItem(c, self.listWidget_Con_Incl)

    def buttonClickedCatLeft(self):
        if not self.listWidget_Cat_Incl.selectedItems(): return
        selection = self.listWidget_Cat_Incl.selectedItems()
        change = []
        for i in selection:
            change.append(i.text())
        self.listWidget_Cat_Excl.addItems(change)
        self.listWidget_Con_Excl.addItems(change)
        for item in selection:
            self.listWidget_Cat_Incl.takeItem(self.listWidget_Cat_Incl.row(item))

    def buttonClickedCatAllRight(self):
        self.listWidget_Cat_Excl.selectAll()
        selection = self.listWidget_Cat_Excl.selectedItems()
        change = []
        for i in selection:
            change.append(i.text())
        self.listWidget_Cat_Incl.addItems(change)
        for item in selection:
            self.listWidget_Cat_Excl.takeItem(self.listWidget_Cat_Excl.row(item))
        for item in selection:
            self.listWidget_Con_Incl.takeItem(self.listWidget_Con_Incl.row(item))

        for c in change:
            self.deleteItem(c, self.listWidget_Con_Excl)
        for c in change:
            self.deleteItem(c, self.listWidget_Con_Incl)

    def buttonClickedCatAllLeft(self):
        self.listWidget_Cat_Incl.selectAll()
        selection = self.listWidget_Cat_Incl.selectedItems()
        change = []
        for i in selection:
            change.append(i.text())
        self.listWidget_Cat_Excl.addItems(change)
        self.listWidget_Con_Excl.addItems(change)
        for item in selection:
            self.listWidget_Cat_Incl.takeItem(self.listWidget_Cat_Incl.row(item))

    def buttonClickedConRight(self):
        if not self.listWidget_Con_Excl.selectedItems(): return
        selection = self.listWidget_Con_Excl.selectedItems()
        change = []
        for i in selection:
            change.append(i.text())
        self.listWidget_Con_Incl.addItems(change)
        for item in selection:
            self.listWidget_Con_Excl.takeItem(self.listWidget_Con_Excl.row(item))

        for c in change:
            self.deleteItem(c, self.listWidget_Cat_Excl)
        for c in change:
            self.deleteItem(c, self.listWidget_Cat_Incl)

    def buttonClickedConLeft(self):
        if not self.listWidget_Con_Incl.selectedItems(): return
        selection = self.listWidget_Con_Incl.selectedItems()
        change = []
        for i in selection:
            change.append(i.text())
        self.listWidget_Con_Excl.addItems(change)
        self.listWidget_Cat_Excl.addItems(change)
        for item in selection:
            self.listWidget_Con_Incl.takeItem(self.listWidget_Con_Incl.row(item))

    def buttonClickedConAllRight(self):
        self.listWidget_Con_Excl.selectAll()
        selection = self.listWidget_Con_Excl.selectedItems()
        change = []
        for i in selection:
            change.append(i.text())
        self.listWidget_Con_Incl.addItems(change)
        for item in selection:
            self.listWidget_Con_Excl.takeItem(self.listWidget_Con_Excl.row(item))

        for c in change:
            self.deleteItem(c, self.listWidget_Cat_Excl)
        for c in change:
            self.deleteItem(c, self.listWidget_Cat_Incl)

    def buttonClickedConAllLeft(self):
        self.listWidget_Con_Incl.selectAll()
        selection = self.listWidget_Con_Incl.selectedItems()
        change = []
        for i in selection:
            change.append(i.text())
        self.listWidget_Con_Excl.addItems(change)
        self.listWidget_Cat_Excl.addItems(change)
        for item in selection:
            self.listWidget_Con_Incl.takeItem(self.listWidget_Con_Incl.row(item))

    def buttonClickedEventRight(self):
        if not self.listWidget_recs.selectedItems(): return
        selection = self.listWidget_events.selectedItems()
        change = []
        for i in selection:
            change.append(i.text())
        self.listWidget_recs.addItems(change)
        for item in selection:
            self.listWidget_events.takeItem(self.listWidget_events.row(item))

        for c in change:
            self.deleteItem(c, self.listWidget_events)
        for c in change:
            self.deleteItem(c, self.listWidget_recs)

    def buttonClickedEventLeft(self):
        if not self.listWidget_recs.selectedItems(): return
        selection = self.listWidget_recs.selectedItems()
        change = []
        for i in selection:
            change.append(i.text())
        self.listWidget_Con_Excl.addItems(change)
        self.listWidget_Cat_Excl.addItems(change)
        for item in selection:
            self.listWidget_Con_Incl.takeItem(self.listWidget_Con_Incl.row(item))

    def buttonClickedEventAllRight(self):
        self.listWidget_Con_Excl.selectAll()
        selection = self.listWidget_Con_Excl.selectedItems()
        change = []
        for i in selection:
            change.append(i.text())
        self.listWidget_Con_Incl.addItems(change)
        for item in selection:
            self.listWidget_Con_Excl.takeItem(self.listWidget_Con_Excl.row(item))

        for c in change:
            self.deleteItem(c, self.listWidget_Cat_Excl)
        for c in change:
            self.deleteItem(c, self.listWidget_Cat_Incl)

    def buttonClickedEventAllLeft(self):
        self.listWidget_Con_Incl.selectAll()
        selection = self.listWidget_Con_Incl.selectedItems()
        change = []
        for i in selection:
            change.append(i.text())
        self.listWidget_Con_Excl.addItems(change)
        self.listWidget_Cat_Excl.addItems(change)
        for item in selection:
            self.listWidget_Con_Incl.takeItem(self.listWidget_Con_Incl.row(item))

    def deleteItem(self, itemName, listWidget):
        items_list = listWidget.findItems(itemName, QtCore.Qt.MatchExactly)
        for item in items_list:
            r = listWidget.row(item)
            listWidget.takeItem(r)

    def buttonConfirm(self):
        uid = self.combo_uid.currentText()
        event = self.combo_event.currentText()
        label = self.combo_label.currentText()
        timestamp = self.combo_time.currentText()
        self.events = list(self.df[event].unique())
        try:
            self.events.sort()
            self.events = [str(i) for i in self.events]
        except:
            self.events.sort()

        self.initiateEvents()
        listvariables = [uid,event,label,timestamp]

        if len(listvariables) == len(set(listvariables)):
            diff = True
        else:
            diff = False

        if diff == False:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle("Warning!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.setText("Some of the selected variables in the boxed are the same. Each box selection must be unique.\n Please change your settings.")
            msg.exec_()
            return

        if diff == True:
            self.tabWidget.setCurrentIndex(1)
            self.tab_1.setEnabled(False)
            self.tab_2.setEnabled(True)
            self.tab_3.setEnabled(True)
            self.tab_7.setEnabled(True)
            for item in listvariables:
                self.deleteItem(item, self.listWidget_Cat_Excl)
                self.deleteItem(item, self.listWidget_Con_Excl)
            return

    def getVariables(self):
        uid = self.combo_uid.currentText()
        event = self.combo_event.currentText()
        timestamp = self.combo_time.currentText()
        label = self.combo_label.currentText()
        set = True
        itemscat = []
        for index in range(self.listWidget_Cat_Incl.count()):
            itemscat.append(self.listWidget_Cat_Incl.item(index))
        labelscat = [i.text() for i in itemscat]
        itemscon = []
        for index in range(self.listWidget_Con_Incl.count()):
            itemscon.append(self.listWidget_Con_Incl.item(index))
        labelscon = [i.text() for i in itemscon]
        recs = []
        for index in range(self.listWidget_recs.count()):
            recs.append(self.listWidget_recs.item(index))
        recs = [i.text() for i in recs]

        keys = ['Events','X','UID', 'Event', 'Timestamp', 'Label', 'Cat', 'Con', 'Set']
        values = [[],[], uid, event, timestamp, label, labelscat, labelscon, set]
        variables = dict(zip(keys, values))
        return variables

    def setColumns(self, columns):
        self.columns = columns

    def setData(self, data):
        self.df = data

    # def close(self):

