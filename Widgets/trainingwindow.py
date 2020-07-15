from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets
from Widgets import pandasmodel as pm
from Widgets.twolistdialog import Ui_TwoListDialog
from DataMiningMethods import SimpleClassifier, SimpleRegressor
from sklearn.tree import DecisionTreeClassifier

import pandas as pd
import pickle

class Ui_Form(object):
    training_type = 0
    scorers = []
    filename = ""
    metadata = {}
    transsys = {}
    datatable = pd.DataFrame
    result = []

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1207, 621)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1201, 501))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.qt_clf_text = QtWidgets.QLabel(self.page1)
        self.qt_clf_text.setGeometry(QtCore.QRect(12, 12, 1151, 32))
        self.qt_clf_text.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.qt_clf_text.setWordWrap(True)
        self.qt_clf_text.setObjectName("qt_clf_text")
        self.groupBox = QtWidgets.QGroupBox(self.page1)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 1181, 381))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 351, 351))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(-10, 10, 362, 326))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 6, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 3, 0, 1, 1)
        self.selectUID_btn_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.selectUID_btn_4.setObjectName("selectUID_btn_4")
        self.gridLayout_4.addWidget(self.selectUID_btn_4, 4, 0, 1, 1)
        self.selectFile_btn_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.selectFile_btn_4.setObjectName("selectFile_btn_4")
        self.gridLayout_4.addWidget(self.selectFile_btn_4, 1, 0, 1, 1)
        self.comboBox_scorer = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_scorer.setObjectName("comboBox_scorer")
        self.comboBox_scorer.addItem("")
        self.comboBox_scorer.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_scorer, 7, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.groupBox_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_4.addWidget(self.line_3, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 9, 0, 1, 1)
        self.lineEdit_threshold = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_threshold.setEnabled(False)
        self.lineEdit_threshold.setObjectName("lineEdit_threshold")
        self.gridLayout_4.addWidget(self.lineEdit_threshold, 10, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.groupBox_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_4.addWidget(self.line_2, 5, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 8, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setEnabled(False)
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.datatable = QtWidgets.QTableView(self.groupBox)
        self.datatable.setGeometry(QtCore.QRect(380, 20, 791, 341))
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 789, 339))
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # self.scrollArea_dataset.setWidget(self.scrollAreaWidgetContents)
        self.btn_continue = QtWidgets.QPushButton(self.page1)
        self.btn_continue.setGeometry(QtCore.QRect(740, 440, 113, 32))
        self.btn_continue.setObjectName("btn_continue")
        self.stackedWidget.addWidget(self.page1)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setGeometry(QtCore.QRect(10, 40, 221, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.treeWidget = QtWidgets.QTreeWidget(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.treeWidget.setFont(font)
        self.treeWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.treeWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setWordWrap(True)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.header().setVisible(False)
        self.treeWidget.header().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.treeWidget, 0, QtCore.Qt.AlignLeft)
        self.btn_continue_2 = QtWidgets.QPushButton(self.frame)
        self.btn_continue_2.setObjectName("btn_continue_2")
        self.verticalLayout_3.addWidget(self.btn_continue_2)
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(10, 10, 751, 16))
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.page)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.frame_2 = QtWidgets.QFrame(self.page_7)
        self.frame_2.setGeometry(QtCore.QRect(10, 40, 1181, 301))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tableView_3 = QtWidgets.QTableView(self.frame_2)
        self.tableView_3.setGeometry(QtCore.QRect(10, 10, 1151, 151))
        self.tableView_3.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectColumns)
        self.tableView_3.setObjectName("tableView_3")
        self.run_btn_4 = QtWidgets.QPushButton(self.frame_2)
        self.run_btn_4.setGeometry(QtCore.QRect(960, 170, 209, 32))
        self.run_btn_4.setToolTip("")
        self.run_btn_4.setToolTipDuration(1)
        self.run_btn_4.setStatusTip("")
        self.run_btn_4.setAutoDefault(False)
        self.run_btn_4.setDefault(False)
        self.run_btn_4.setFlat(False)
        self.run_btn_4.setObjectName("run_btn_4")
        self.label_2 = QtWidgets.QLabel(self.page_7)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 961, 16))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page_7)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.plainTextEdit_output = QtWidgets.QPlainTextEdit(self.page_2)
        self.plainTextEdit_output.setGeometry(QtCore.QRect(20, 60, 1151, 321))
        self.plainTextEdit_output.setObjectName("plainTextEdit_output")
        self.label_14 = QtWidgets.QLabel(self.page_2)
        self.label_14.setGeometry(QtCore.QRect(20, 30, 421, 16))
        self.label_14.setObjectName("label_14")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_15 = QtWidgets.QLabel(self.page_3)
        self.label_15.setGeometry(QtCore.QRect(20, 50, 611, 16))
        self.label_15.setObjectName("label_15")
        self.pushButton_finish = QtWidgets.QPushButton(self.page_3)
        self.pushButton_finish.setGeometry(QtCore.QRect(1070, 380, 113, 32))
        self.pushButton_finish.setObjectName("pushButton_finish")
        self.tableView = QtWidgets.QTableView(self.page_3)
        self.tableView.setGeometry(QtCore.QRect(20, 80, 1161, 291))
        self.tableView.setWordWrap(True)
        self.tableView.setObjectName("tableView")
        self.btn_save_best = QtWidgets.QPushButton(self.page_3)
        self.btn_save_best.setGeometry(QtCore.QRect(900, 380, 151, 32))
        self.btn_save_best.setObjectName("btn_save_best")
        self.stackedWidget.addWidget(self.page_3)

        # Connect slots/callbacks and events
        self.run_btn_4.clicked.connect(self.runClicked)
        self.selectFile_btn_4.clicked.connect(self.inInputFileButtonClicked)
        self.selectUID_btn_4.clicked.connect(self.selectUIDButtonClicked)
        self.btn_save_best.clicked.connect(self.saveButtonClicked)
        self.btn_continue.clicked.connect(self.continue1Clicked)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.qt_clf_text.setText(_translate("Form",
                                            "In this section the user can quickly configure a dataset to train a classifier. Upload a file from your computer, select the attributes you want to use, and click RUN! to start training a classifier. "))
        self.label_11.setText(_translate("Form", "Select a .csv data file:"))
        self.label_13.setText(_translate("Form", "Select scorer to optimize for:"))
        self.label_12.setText(_translate("Form",
                                         "Select the unique identifier, the independent attributes, and the dependent attributes to include in the training. "))
        self.selectUID_btn_4.setText(_translate("Form", "Select Attributes"))
        self.selectFile_btn_4.setText(_translate("Form", "Select .csv file"))
        self.comboBox_scorer.setItemText(0, _translate("Form", "AUC"))
        self.comboBox_scorer.setItemText(1, _translate("Form", "Accuracy"))
        self.label_10.setText(_translate("Form", "Set maximum feature importance threshold:"))
        self.lineEdit_threshold.setText(_translate("Form", "n.e."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Advanced"))
        self.btn_continue.setText(_translate("Form", "Continue"))
        self.treeWidget.headerItem().setText(0, _translate("Form", "Event"))
        self.treeWidget.headerItem().setText(1, _translate("Form", "Weight"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Form", "Event 1"))
        self.treeWidget.topLevelItem(0).setText(1, _translate("Form", "1"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Form", "Event 2"))
        self.treeWidget.topLevelItem(1).setText(1, _translate("Form", "1"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.btn_continue_2.setText(_translate("Form", "Continue"))
        self.label.setText(
            _translate("Form", "Add weights to each event, to emphasize event importance. Default weight is 1. "))
        self.run_btn_4.setText(_translate("Form", "RUN!"))
        self.label_2.setText(_translate("Form",
                                        "The feature  imporatnce for each of the independent variables is shown in the table below. Select the ones to be excluded from the training."))
        self.plainTextEdit_output.setPlainText(_translate("Form", "Process started!\n"
                                                                  "Preprocessing started!"))
        self.label_14.setText(_translate("Form", "Koala is running..."))
        self.label_15.setText(_translate("Form",
                                         "Koala has finished training the estimator. General statistics of the final model are shown below:"))
        self.pushButton_finish.setText(_translate("Form", "Finish"))
        self.btn_save_best.setText(_translate("Form", "Save Best Model"))

    def continue1Clicked(self):
        if self.training_type==0:
            if self.metadata['Set']==True:
                self.stackedWidget.setCurrentIndex(2)
                self.focus = str(self.comboBox_scorer.currentText())
                self.data, self.metadata, self.transsys = SimpleClassifier.runPreprocessing(self.metadata, self.filename)
                self.fimp = self.createFeatureImportances()
                self.dffi = pm.PandasModel(self.fimp)
                self.tableView_3.setModel(self.dffi)
                self.tableView_3.resizeColumnsToContents()

        if self.training_type==1:
            if self.metadata['Set']==True:
                self.stackedWidget.setCurrentIndex(2)
                self.focus = str(self.comboBox_scorer.currentText())
                self.data, self.metadata, self.transsys = SimpleRegressor.runPreprocessing(self.metadata, self.filename)
                self.fimp = self.createFeatureImportances()
                self.dffi = pm.PandasModel(self.fimp)
                self.tableView_3.setModel(self.dffi)
                self.tableView_3.resizeColumnsToContents()

    def runClicked(self):
        self.leaveout = self.tableView_3.selectionModel().selectedColumns()
        removecolumns = []
        for i in range(0, len(self.leaveout)):
            slce = self.leaveout[i].column()
            col1 = self.fimp.iloc[:, slce]
            name = col1.name
            removecolumns.append(name)

        for i in range(0,len(removecolumns)):
            try:
                removecolumns[i] = int(removecolumns[i])
                break
            except ValueError:
                break

        self.data = self.data.drop(columns=removecolumns)

        if self.training_type == 0:
            if self.metadata['Set'] == True:
                self.stackedWidget.setCurrentIndex(3)
                self.focus = str(self.comboBox_scorer.currentText())
                finished, self.model, self.metadata, self.df = SimpleClassifier.runAlgorithm(self.metadata, self.data,
                                                                                             self.focus)
                if finished == True:
                    self.stackedWidget.setCurrentIndex(4)
                    self.df1 = pm.PandasModel(self.df)
                    self.tableView.setModel(self.df1)
                    self.tableView.resizeColumnsToContents()
        if self.training_type == 1:
            if self.metadata['Set'] == True:
                self.stackedWidget.setCurrentIndex(3)
                self.focus = str(self.comboBox_scorer.currentText())
                finished, self.model, self.metadata, self.df = SimpleRegressor.runAlgorithm(self.metadata, self.data,
                                                                                            self.focus)
                if finished == True:
                    self.stackedWidget.setCurrentIndex(4)
                    self.df1 = pm.PandasModel(self.df)
                    self.tableView.setModel(self.df1)
                    self.tableView.resizeColumnsToContents()

    def inInputFileButtonClicked(self):
        self.filename, self.filter = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        if self.filename:
            self.df = pd.read_csv(self.filename, ';')
            model = pm.PandasModel(self.df)
            self.datatable.setModel(model)
            self.columns = list(self.df.columns.values)

    def selectUIDButtonClicked(self):
        columns = self.columns
        if self.filename:
            if self.result!=QtWidgets.QDialog.Accepted:
                dialog = twoListDialog(self)
                dialog.setColumns(self.columns)
                dialog.setData(self.df)
                dialog.initiateLists(self.columns)
                self.result = dialog.exec_()
                self.metadata = dialog.getVariables()
                if result==QtWidgets.QDialog.Accepted:
                    return(self.metadata, result==QtWidgets.QDialog.Accepted)
            ## insert warning pop up here

    def saveButtonClicked(self):
        name, filter = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')
        pickle.dump((self.model, self.metadata, self.transsys), open(name, "wb"))

    def createFeatureImportances(self):
        uid = self.metadata['UID']
        dffi = self.data.drop(columns=['TraceID',uid,'Milestone'])
        tree = DecisionTreeClassifier(random_state=0)
        X = dffi.drop(columns=['Label'])
        Y = dffi['Label']
        tree.fit(X, Y)
        print('Tree Fitted')
        fi = list(tree.feature_importances_)
        feats = list(X.columns.values)
        feats = map(lambda e: str(e), feats)
        print(feats)
        fimptable = pd.DataFrame(fi).T
        fimptable.columns = feats
        return fimptable

class twoListDialog(QtWidgets.QDialog, Ui_TwoListDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)

    def initiateLists2(self, columns):
        self.combo_uid.addItem("")
        self.combo_uid.addItems(columns)
        self.combo_label.addItem("")
        self.combo_label.addItems(columns)
        self.combo_event.addItem("")
        self.combo_event.addItems(columns)
        self.listWidget_Cat_Excl.addItems(columns)
        self.listWidget_Con_Excl.addItems(columns)

