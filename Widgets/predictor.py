from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets
import pickle
import pandas as pd
import numpy as np
from Widgets import pandasmodel as pm

class Ui_Form(object):
    min = 0
    max = 100
    dsset = False
    modelset = False
    windowat3 = False
    training_type = 0

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1214, 663)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1201, 641))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.groupBox = QtWidgets.QGroupBox(self.page)
        self.groupBox.setGeometry(QtCore.QRect(20, 40, 301, 561))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_select_file = QtWidgets.QPushButton(self.groupBox)
        self.btn_select_file.setObjectName("btn_select_file")
        self.verticalLayout.addWidget(self.btn_select_file)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.btn_select_cases = QtWidgets.QPushButton(self.groupBox)
        self.btn_select_cases.setObjectName("btn_select_cases")
        self.verticalLayout.addWidget(self.btn_select_cases)
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(30, 20, 1121, 16))
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.page)
        self.groupBox_2.setGeometry(QtCore.QRect(320, 40, 800, 561))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.texteditor = QtWidgets.QTextEdit(self.groupBox_2)
        self.texteditor.setObjectName("texteditor")
        self.verticalLayout_2.addWidget(self.texteditor)
        self.datatable = QtWidgets.QTableView(self.groupBox_2)
        self.datatable.setObjectName("datatable")
        self.verticalLayout_2.addWidget(self.datatable)
        self.btn_continue1 = QtWidgets.QPushButton(self.page)
        self.btn_continue1.setGeometry(QtCore.QRect(1000, 600, 113, 32))
        self.btn_continue1.setObjectName("btn_continue1")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setEnabled(False)
        self.page_3.setObjectName("page_3")
        self.comboBox = QtWidgets.QComboBox(self.page_3)
        self.comboBox.setGeometry(QtCore.QRect(30, 40, 201, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 531, 16))
        self.label_3.setObjectName("label_3")
        self.btn_continue2 = QtWidgets.QPushButton(self.page_3)
        self.btn_continue2.setGeometry(QtCore.QRect(1080, 590, 113, 32))
        self.btn_continue2.setObjectName("btn_continue2")
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.tableView = QtWidgets.QTableView(self.page_2)
        self.tableView.setGeometry(QtCore.QRect(10, 40, 1191, 551))
        self.tableView.setObjectName("tableView")
        self.tableView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(10, -30, 971, 91))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.btn_finish = QtWidgets.QPushButton(self.page_2)
        self.btn_finish.setGeometry(QtCore.QRect(1090, 590, 113, 32))
        self.btn_finish.setObjectName("btn_finish")
        self.btn_save_to_disk = QtWidgets.QPushButton(self.page_2)
        self.btn_save_to_disk.setGeometry(QtCore.QRect(600, 590, 201, 32))
        self.btn_save_to_disk.setObjectName("btn_save_to_disk")
        self.btn_cont_to_rec = QtWidgets.QPushButton(self.page_2)
        self.btn_cont_to_rec.setGeometry(QtCore.QRect(800, 590, 291, 32))
        self.btn_cont_to_rec.setObjectName("btn_cont_to_rec")
        self.stackedWidget.addWidget(self.page_2)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_4 = QtWidgets.QLabel(self.page_4)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 991, 16))
        self.label_4.setObjectName("label_4")
        self.frame = QtWidgets.QFrame(self.page_4)
        self.frame.setGeometry(QtCore.QRect(0, 30, 401, 281))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_select_estimator = QtWidgets.QPushButton(self.frame)
        self.btn_select_estimator.setObjectName("btn_select_estimator")
        self.verticalLayout_3.addWidget(self.btn_select_estimator)
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.btn_select_use_case_dataset = QtWidgets.QPushButton(self.frame)
        self.btn_select_use_case_dataset.setObjectName("btn_select_use_case_dataset")
        self.verticalLayout_3.addWidget(self.btn_select_use_case_dataset)
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.btn_rec_quick = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_rec_quick.setFont(font)
        self.btn_rec_quick.setObjectName("btn_rec_quick")
        self.verticalLayout_3.addWidget(self.btn_rec_quick)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.tableView_4 = QtWidgets.QTableView(self.page_5)
        self.tableView_4.setGeometry(QtCore.QRect(10, 50, 1191, 501))
        self.tableView_4.setObjectName("tableView_4")
        self.tableView_4.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.label_5 = QtWidgets.QLabel(self.page_5)
        self.label_5.setGeometry(QtCore.QRect(10, -20, 1121, 91))
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.btn_save_rec = QtWidgets.QPushButton(self.page_5)
        self.btn_save_rec.setGeometry(QtCore.QRect(980, 560, 113, 32))
        self.btn_save_rec.setObjectName("btn_save_rec")
        self.btn_finish_rec = QtWidgets.QPushButton(self.page_5)
        self.btn_finish_rec.setGeometry(QtCore.QRect(1090, 560, 113, 32))
        self.btn_finish_rec.setObjectName("btn_finish_rec")
        self.stackedWidget.addWidget(self.page_5)

        # EVENTS / TRIGGERS
        self.btn_select_file.clicked.connect(self.InputModelClicked)
        self.btn_select_cases.clicked.connect(self.InputDataClicked)
        self.btn_continue1.clicked.connect(self.Continue1Clicked)
        self.btn_select_estimator.clicked.connect(self.selectModelRec)
        self.btn_select_use_case_dataset.clicked.connect(self.openUseCaseDataset)
        self.btn_rec_quick.clicked.connect(self.createQuickRecommendations)
        self.btn_save_rec.clicked.connect(self.saveRecToDisk)
        self.btn_save_to_disk.clicked.connect(self.saveToDisk)
        self.btn_cont_to_rec.clicked.connect(self.continueToRecSystem)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_select_file.setText(_translate("Form", "Select Estimator Model"))
        self.btn_select_cases.setText(_translate("Form", "Select New Case Datafile"))
        self.label.setText(_translate("Form", "To predict the outcomes of new cases, trained models can be used. Select a Koala-trained model from your local storage, and a .csv file with new cases to start making predictions. "))
        self.btn_continue1.setText(_translate("Form", "Continue"))
        self.comboBox.setItemText(0, _translate("Form", "Predicted Value"))
        self.comboBox.setItemText(1, _translate("Form", "Predicted Value x Probability"))
        self.label_3.setText(_translate("Form", "Select how you want to define the risk value of each case.  "))
        self.btn_continue2.setText(_translate("Form", "Continue"))
        self.label_2.setText(_translate("Form", "The predicted outcomes are shown below. Select the rows you need for further analysis and save the dataframe to your local storage as a .csv file.  A subset of the originial dataset is stored as well, based on this selection. This dataset is needed for making recommendations.  "))
        self.btn_finish.setText(_translate("Form", "Finish"))
        self.btn_save_to_disk.setText(_translate("Form", "Save DataFrame to Disk"))
        self.btn_cont_to_rec.setText(_translate("Form", "Continue to Recommendation System"))
        self.label_4.setText(_translate("Form", "With a trained model and a set of risky cases, recommendations can be given for each of these cases. Upload an estimator and a dataset with risky cases below. "))
        self.btn_select_estimator.setText(_translate("Form", "Select Estimator"))
        self.btn_select_use_case_dataset.setText(_translate("Form", "Select Use Case Dataset"))
        self.btn_rec_quick.setText(_translate("Form", "Create Recommendations"))
        self.label_5.setText(_translate("Form", "Below the top 5 recommendations for each case are shown. The set of all recommendations per case can be exported into a .csv file for further analysis and integration with a database. "))
        self.btn_save_rec.setText(_translate("Form", "Save to Disk"))
        self.btn_finish_rec.setText(_translate("Form", "Finish"))

    def openRecommender(self):
        self.stackedWidget.setCurrentIndex(3)

    def InputModelClicked(self):
        self.filename, filter = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        if self.filename:
            self.model, self.metadata, self.transsys = pickle.load(open(self.filename, "rb" ))
            self.list_of_events = list(self.metadata['Events'])
            self.X_attributes = list(self.metadata['X'])
            self.attributes = list(set(self.X_attributes) - set(self.list_of_events))
            self.uid = self.metadata['UID']
            self.events = list(set(self.list_of_events) - set([self.uid, 'TraceID', 'Milestone']))
            self.timestamp = self.metadata['Timestamp']
            self.event = self.metadata['Event']
            self.attributes_categorical = self.metadata['Cat']
            self.attributes_continuous = self.metadata['Con']
            self.label = self.metadata['Label']
            self.texteditor.append('UID: ' + str(self.uid))
            self.texteditor.append('Events: ' + str(self.events))
            self.texteditor.append('Categorical Attributes used in Model: ' + str(self.attributes_categorical))
            self.texteditor.append('Continuous Attributes used in Model: ' + str(self.attributes_continuous))
            self.texteditor.append('Label Used: ' + str(self.label))
            self.texteditor.append('X Attributes: ' + str(self.X_attributes))
            self.modelset = True

    def InputDataClicked(self):
        self.filename, self.filter = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        if self.filename:
            self.df = pd.read_csv(self.filename, ';')
            self.dataset = pm.PandasModel(self.df)
            self.datatable.setModel(self.dataset)
            self.dsset = True

#MAIN ALGORITHM 1

    def Continue1Clicked(self):
        if self.training_type==0:
            if self.dsset==True:
                self.stackedWidget.setCurrentIndex(2)
                self.windowat3 = True
            if self.windowat3==True:
                if self.modelset == True:
                    self.prepdata = self.runPreprocessing(self.df)
                    self.preddata = self.correctColumns(self.prepdata)
                    self.predictions = self.runPredictorClassifier(self.preddata)
                    self.predictions = self.predictions.sort_values(by=['Risk'], ascending=False)
                    datatableclf = pm.PandasModel(self.predictions)
                    self.tableView.setModel(datatableclf)
        if self.training_type==1:
            if self.dsset==True:
                self.stackedWidget.setCurrentIndex(2)
                self.windowat3 = True
            if self.windowat3==True:
                if self.modelset == True:
                    self.prepdata = self.runPreprocessing(self.df)
                    self.preddata = self.correctColumns(self.prepdata)
                    self.predictions = self.runPredictorRegressor(self.preddata)
                    self.predictions = self.predictions.sort_values(by=['Prediction'], ascending=False)
                    datatablereg = pm.PandasModel(self.predictions)
                    self.tableView.setModel(datatablereg)

        # if self.training_type == 0:
        #     if self.dsset == True:
        #         if self.modelset == True:
        #             self.stackedWidget.setCurrentIndex(2)

    def runPreprocessing(self, dataset):
        self.prepdata = dataset
        labels_to_keep = [self.uid, self.event, self.timestamp]
        labels_to_keep.extend(self.attributes_categorical)
        labels_to_keep.extend(self.attributes_continuous)
        self.prepdata = self.prepdata[labels_to_keep]

        self.prepdata = self.createMilestones(self.prepdata)
        dfa = self.createAttributeDataFrame(self.prepdata)
        dfa.to_csv('dfa.csv')
        df = self.count_events(self.prepdata)
        df.to_csv('df.csv')

        df_merged = pd.merge(df, dfa, on='TraceID')
        df_merged = pd.get_dummies(df_merged, columns=self.attributes_categorical)
        uidcolumn = df_merged[self.uid]
        df_merged.drop(labels=[self.uid], axis=1, inplace=True)
        df_merged.insert(0, self.uid, uidcolumn)
        traceid = df_merged['TraceID']
        df_merged.drop(labels=['TraceID'], axis=1, inplace=True)
        df_merged.insert(0, 'TraceID', traceid)
        prepdata = df_merged.loc[df_merged['Milestone'] == df_merged['Max Milestone']]
        prepdata = prepdata.drop(columns=['LastEventTime', 'Max Milestone', 'LastEventTimeMilestone'])
        prepdata = prepdata.drop(columns=self.timestamp)

        return prepdata
        self.prepdata.to_csv('prepdata-final.csv')

    def createMilestones(self, data):
        uid = self.uid
        timestamp = self.timestamp
        cids = self.prepdata[self.uid].unique()

        for id in cids:
            mini = data.loc[data[uid] == id, timestamp].min(axis=0)
            data.loc[data[uid] == id, 'FirstEventTime'] = mini
        for id in cids:
            maxi = data.loc[data[uid] == id, timestamp].max(axis=0)
            data.loc[data[uid] == id, 'LastEventTime'] = maxi

        t = 28
        data[timestamp] = pd.to_datetime(data[timestamp])
        data['FirstEventTime'] = pd.to_datetime(data['FirstEventTime'])
        data['LastEventTime'] = pd.to_datetime(data['LastEventTime'])

        data['Prefix Time Elapsed'] = data[timestamp] - data['FirstEventTime']
        data['Prefix Time Elapsed'] = data['Prefix Time Elapsed'].dt.total_seconds()

        data['Milestone'] = data['Prefix Time Elapsed'].apply(lambda x: x / (t * 86400))
        data['Milestone'] = np.floor(data['Milestone'])
        for id in cids:
            maxm = data.loc[data[uid] == id, 'Milestone'].max(axis=0)
            data.loc[data[uid] == id, 'Max Milestone'] = maxm
        data['Prefix Time Elapsed'] = data['Prefix Time Elapsed'].apply(lambda x: x / (86400))

        return data

    def createAttributeDataFrame(self, data):
        event_column = self.event
        uid = self.uid
        mini = self.min
        maxi = self.max
        timestamp = self.timestamp

        atts = ['FirstEventTime', 'Prefix Time Elapsed']
        event = [event_column]
        droplist = atts + event

        dfaf = data
        dfaf = dfaf.drop(columns=droplist)

        min_milestone = mini
        max_milestone = maxi

        frames_a = []

        dfa_list_milestones = []
        dfa_milestones = []
        for m in range(min_milestone, max_milestone):
            dfa_milestones.append(m)
            dfa_list_milestones.append('dfm_' + str(m))
        dict_dfa = dict(zip(dfa_milestones, dfa_list_milestones))

        for m in range(0, max_milestone):
            dfsa = dfaf.loc[dfaf['Milestone'] <= m]  # split on milestone value
            dfsa = dfsa.loc[dfsa['Max Milestone'] >= m]
            dfsa = dfsa.reset_index(drop=True)
            mcids = dfsa[uid].unique()
            for i in range(0, len(mcids)):
                new_id = str(mcids[i]) + '-' + str(m)
                dfsa.loc[dfsa[uid] == mcids[i], 'TraceID'] = new_id
                maxi = dfsa.loc[dfsa[uid] == mcids[i], timestamp].max(axis=0)
                dfsa.loc[dfsa[uid] == mcids[i], 'LastEventTimeMilestone'] = maxi

            dict_dfa[m] = dfsa
            frames_a.append(dict_dfa[m])
            print('Milestone ' + str(m) + ' done!')

        dfa = pd.concat(frames_a, ignore_index=True)
        dfa = dfa.loc[dfa[timestamp] == dfa['LastEventTimeMilestone']]
        droplist2 = ['Milestone']
        droplist2.append(self.uid)
        dfa = dfa.drop(columns=droplist2)

        return dfa

    def count_events(self, data):
        mini = self.min
        maxi = self.max
        uid = self.uid
        event = self.event
        features = self.events

        df_list_milestones = []
        min_milestone = mini
        max_milestone = maxi
        milestones_a = []
        frames = []
        for m in range(min_milestone, max_milestone):
            milestones_a.append(m)
            df_list_milestones.append('dfm_' + str(m))
        dict_df = dict(zip(milestones_a, df_list_milestones))

        for m in range(0, max_milestone):
            dfs = data.loc[data['Milestone'] <= m]  # split on milestone value
            dfs = dfs.loc[dfs['Max Milestone'] >= m]
            dfs = dfs.reset_index(drop=True)
            mcids = dfs[uid].unique()
            dfm = pd.DataFrame(0, index=np.arange(len(mcids)), columns=features)
            for i in range(0, len(mcids)):
                new_id = str(mcids[i]) + '-' + str(m)
                dfm.loc[i, uid] = mcids[i]
                dfm.loc[i, 'TraceID'] = new_id
                dfm.loc[i, 'Milestone'] = m
            print('loop 1 done!')
            for i in mcids:
                rows = dfs.loc[dfs[uid] == i]
                activities = rows[event].unique()
                for a in activities:
                    if a in features:
                        total = len(rows.loc[rows[event] == a])
                        dfm.loc[dfm[uid] == i, a] = total
            print('loop 2 done!')
            dict_df[m] = dfm
            frames.append(dict_df[m])
            print('Milestone ' + str(m) + ' done!')

        df = pd.concat(frames, ignore_index=True)
        df.to_csv('df.csv')

        return df

    def correctColumns(self, data):
        uid = self.uid
        self.cids = list(data[self.uid].unique())
        self.cids.sort()
        self.predlenght = len(self.cids)

        curr_cols = list(data.columns.values)
        needed_cols = list(self.X_attributes)
        missing_cols = list(set(needed_cols) - set(curr_cols))
        cols_too_much = list(set(curr_cols) - set(needed_cols))
        length = len(data)

        final_data = data
        for m in missing_cols:
            final_data[m] = 0
        cols_too_much = list(set(curr_cols) - set(needed_cols))
        final_data = final_data.drop(columns=cols_too_much)
        final_data.reset_index()

        return final_data

#MAIN ALGORTHM 2 /3
    def runPredictorClassifier(self, final_data):
        columns = [self.uid, 'Prediction', 'Probability Outcome 0', 'Probability Outcome 1', 'Risk',
                   'Risk Category']
        self.predictions = pd.DataFrame(index=range(self.predlenght), columns=columns)
        pred = self.model.predict(final_data)
        predprob = self.model.predict_proba(final_data)

        for i in range(0, self.predlenght):
            self.predictions.loc[i, self.uid] = self.cids[i]
        for i in range(0, len(final_data)):
            if pred[i] == 0:
                self.predictions.loc[i, 'Prediction'] = 'Outcome: 0'
            if pred[i] == 1:
                self.predictions.loc[i, 'Prediction'] = 'Outcome 1'
            self.predictions.loc[i, 'Probability Outcome 0'] = predprob[i, 0]
            prob = predprob[i, 1]
            self.predictions.loc[i, 'Probability Outcome 1'] = prob
            risk = prob * 1
            self.predictions.loc[i, 'Risk'] = risk
        return self.predictions

    def runPredictorRegressor(self, final_data):
        columns = [self.uid, 'Prediction','Risk',
                   'Risk Category']
        self.predictions = pd.DataFrame(index=range(self.predlenght), columns=columns)
        pred = self.model.predict(final_data)
        # predprob = self.model.predict_proba(final_data)

        for i in range(0, self.predlenght):
            self.predictions.loc[i, self.uid] = self.cids[i]
        for i in range(0, len(final_data)):
            self.predictions.loc[i, 'Prediction'] = pred[i]
            # self.predictions.loc[i, 'Probability Outcome 0'] = predprob[i, 0]
            # prob = predprob[i, 1]
            # self.predictions.loc[i, 'Probability Outcome 1'] = prob
            risk = 'TBD'
            self.predictions.loc[i, 'Risk'] = risk
        return self.predictions

#REC SYSTEM
    def continueToRecSystem(self):
        self.stackedWidget.setCurrentIndex(4)
        selectionindexout = self.tableView.selectionModel().selectedRows()
        selectionindex = []
        for i in range(0, len(selectionindexout)):
            row = selectionindexout[i].row()
            selectionindex.append(row)
        subset = self.predictions.iloc[selectionindex]
        self.selection = subset[self.uid]
        if self.training_type == 0:
            self.recommendations = self.makeRecommendationsClassifier(self.selection)
        if self.training_type ==1:
            self.recommendations = self.makeRecommendationsRegressor(self.selection)
        recmodel = pm.PandasModel(self.recommendations)
        self.tableView_4.setModel(recmodel)

    def saveToDisk(self):
        name, filter = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')
        selectionindexout = self.tableView.selectionModel().selectedRows()
        selectionindex = []
        for i in range(0, len(selectionindexout)):
            row = selectionindexout[i].row()
            selectionindex.append(row)
        subset = self.predictions.iloc[selectionindex]
        subset.to_csv(name)

    def makeRecommendationsClassifier(self, selection):
        recdata = self.prepdata[self.prepdata[self.uid].isin(selection)]
        recdata[self.uid] = recdata[self.uid].astype(int)

        self.recdata = self.countExtraEvents(recdata, selection) #generate, next events according to transition system
        ids = self.recdata[self.uid]
        interventions = self.recdata['Intervention']
        # riskbefore = self.predictions[self.predictions[self.uid].isin(selection)]
        # riskbefore = riskbefore['Risk']
        # print(type(riskbefore))
        self.recdata = self.fixDifferences()

        columns =  [self.uid,'Intervention','Next Event in Transition System?','Prediction', 'Prob. Outcome 0', 'Prob. Outcome 1', 'Risk','Predicted Risk','Risk Difference','Risk Category']
        reclength = len(self.recdata)

        self.recommendations = pd.DataFrame(index=range(reclength), columns=columns)
        rec = self.model.predict(self.recdata)
        recprob = self.model.predict_proba(self.recdata)


        for i in range(0, reclength):
            id = ids[i]
            self.recommendations.loc[i, self.uid] = id
            intv = interventions[i]
            self.recommendations.loc[i, 'Intervention'] = intv
            trace = recdata.loc[recdata[self.uid]==id]
            trace = trace[self.events]
            trace = tuple(list(trace.iloc[0].values))
            pred_event_ts = self.return_next_events(trace, self.transsys)
            if pred_event_ts != 'None':
                keys1 = pred_event_ts.keys()
                if intv in keys1:
                    self.recommendations.loc[i, 'Next Event in Transition System?'] = ('Yes', pred_event_ts[intv])
                else:
                    self.recommendations.loc[i, 'Next Event in Transition System?'] = 'No'
            else:
                self.recommendations.loc[i, 'Next Event in Transition System?'] = 'No'
            if rec[i] == 0:
                self.recommendations.loc[i, 'Prediction'] = 'Outcome 0'
            if rec[i] == 1:
                self.recommendations.loc[i, 'Prediction'] = 'Outcome 1'
            self.recommendations.loc[i, 'Prob. Outcome 0'] = recprob[i, 0]
            prob = recprob[i, 1]
            self.recommendations.loc[i, 'Prob. Outcome 1'] = prob
            risk = prob * 1
            self.recommendations.loc[i, 'Risk'] = risk
            self.recommendations.loc[i, 'Predicted Risk'] = self.predictions[self.predictions[uid]==self.recommendationsloc[i, uid], 'Risk']
            self.recommendations.loc[i, 'Risk Difference'] = self.recommendations.loc[i, 'Predicted Risk'] - self.recommendations.loc[i, 'Risk']

        return self.recommendations

    def makeRecommendationsRegressor(self, selection):
        recdata = self.prepdata[self.prepdata[self.uid].isin(selection)]
        recdata[self.uid] = recdata[self.uid].astype(int)

        self.recdata = self.countExtraEvents(recdata, selection)
        ids = self.recdata[self.uid]
        interventions = self.recdata['Intervention']
        # riskbefore = self.predictions[self.predictions[self.uid].isin(selection)]
        # riskbefore = riskbefore['Risk']
        # print(type(riskbefore))
        self.recdata = self.fixDifferences()
        columns =  [self.uid,'Intervention','Prediction','Risk','Risk Difference','Risk Category']
        reclength = len(self.recdata)

        self.recommendations = pd.DataFrame(index=range(reclength), columns=columns)
        rec = self.model.predict(self.recdata)
        # recprob = self.model.predict_proba(self.recdata)

        for i in range(0, reclength):
            self.recommendations.loc[i, self.uid] = ids[i]
            self.recommendations.loc[i, 'Intervention'] = interventions[i]
            # self.recommendations.loc[i, 'Risk Before Intervention'] = riskbefore.loc[riskbefore[self.uid]==ids[i]]
        for i in range(0, len(self.recdata)):
            self.recommendations.loc[i, 'Prediction'] = rec[i]
            # self.recommendations.loc[i, 'Prob. Outcome 0'] = recprob[i, 0]
            # # prob = recprob[i, 1]
            # self.recommendations.loc[i, 'Prob. Outcome 1'] = prob
            risk = 'TBD'
            self.recommendations.loc[i, 'Risk'] = risk

        return self.recommendations

    def countExtraEvents(self, data, selection):
        datalist = []
        for i in selection:
            for e in self.events:
                row = data.loc[data[self.uid] == i]
                row[e] += 1
                row['Intervention'] = e
                trace = str(i) + '-' + str(e)
                row['TraceID'] = trace
                keys = row.columns.values
                values = row.iloc[0]
                dy = dict(zip(keys, values))
                datalist.append(dy)
        d = pd.DataFrame(datalist)
        return d

    def fixDifferences(self):
        curr_cols = list(self.recdata.columns.values)
        needed_cols = list(self.X_attributes)
        missing_cols = list(set(needed_cols) - set(curr_cols))
        cols_too_much = list(set(curr_cols) - set(needed_cols))
        length = len(self.recdata)

        final_data = self.recdata
        for m in missing_cols:
            final_data[m] = 0
        cols_too_much = list(set(curr_cols) - set(needed_cols))
        final_data = final_data.drop(columns=cols_too_much)
        final_data.reset_index()
        return final_data

    def selectModelRec(self):
        self.filename, filter = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        if self.filename:
            self.model, self.metadata = pickle.load(open(self.filename, "rb"))
            self.list_of_events = list(self.metadata['Events'])
            self.X_attributes = list(self.metadata['X'])
            self.attributes = list(set(self.X_attributes) - set(self.list_of_events))
            self.uid = self.metadata['UID']
            self.events = set(self.list_of_events) - set([self.uid, 'TraceID', 'Milestone'])
            self.timestamp = self.metadata['Timestamp']
            self.event = self.metadata['Event']
            self.attributes_categorical = self.metadata['Cat']
            self.attributes_continuous = self.metadata['Con']
            self.label = self.metadata['Label']
            self.modelset = True

    def openUseCaseDataset(self):
        self.filename, self.filter = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        if self.filename:
            self.df = pd.read_csv(self.filename, ';')
            self.dsset = True

    def createQuickRecommendationsClassifier(self):
        self.stackedWidget.setCurrentIndex(4)
        ids = list(self.df[self.uid].unique())
        self.prepdata = self.runPreprocessing(self.df)
        self.preddata = self.correctColumns(self.prepdata)
        self.recommendations = self.makeRecommendationsClassifier(ids)
        recmodel = pm.PandasModel(self.recommendations)
        print
        self.tableView_4.setModel(recmodel)

    def createQuickRecommendationsRegressor(self):
        self.stackedWidget.setCurrentIndex(4)
        ids = list(self.df[self.uid].unique())
        self.prepdata = self.runPreprocessing(self.df)
        self.preddata = self.correctColumns(self.prepdata)
        self.recommendations = self.makeRecommendationsClassifier(ids)
        recmodel = pm.PandasModel(self.recommendations)
        print
        self.tableView_4.setModel(recmodel)

    def createQuickRecommendations(self):
        self.stackedWidget.setCurrentIndex(4)
        ids = list(self.df[self.uid].unique())
        self.prepdata = self.runPreprocessing(self.df)
        self.preddata = self.correctColumns(self .prepdata)
        if self.training_type ==0:
            self.recommendations = self.makeRecommendationsClassifier(ids)
        if self.training_type==1:
            self.recommendations = self.makeRecommendationsRegressor(ids)
        recmodel = pm.PandasModel(self.recommendations)
        self.tableView_4.setModel(recmodel)

    def saveRecToDisk(self):
        name, filter = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')
        selectionindexout = self.tableView_4.selectionModel().selectedRows()
        selectionindex = []
        for i in range(0, len(selectionindexout)):
            row = selectionindexout[i].row()
            selectionindex.append(row)
        subset = self.recommendations.iloc[selectionindex]
        subset.to_csv(name)

    def resetWidgetIndex(self):
        self.stackedWidget.setCurrentIndex(0)

    def return_next_events(self, prefix, dictx):
        lookup = tuple(prefix)
        if lookup in dictx.keys():
            next_events = dictx[lookup]
        else:
            included_keys = []
            keys = []
            for j in range(1, 4):
                print('LoopStarted')
                for i in range(0, len(prefix)):
                    tpl = list(prefix)
                    value = tpl[i]
                    new_value = value + j
                    tpl[i] = new_value
                    to_tuple = tuple(tpl)
                    print(to_tuple)
                    if to_tuple in dictx.keys():
                        included_keys.append(to_tuple)
                        keys.append(i)
                if not included_keys == []:
                    break
            if included_keys == []:
                next_events = 'None'
            else:
                sum_dict = dict()
                for i in range(0, len(included_keys)):
                    sum_dict = dict(Counter(sum_dict) + Counter(dictx[included_keys[i]]))
                next_events = sum_dict
            print(included_keys)
            for i in keys:
                print(events[i])
        print(next_events)
        return next_events


















