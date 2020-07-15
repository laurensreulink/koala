from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import sys

from Widgets import mainwindow, trainingwindow, twolistdialog, home, predictor

class MainWindow_UI(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow_UI, self).__init__(parent)
        self.setupUi(self) #This is defined in design.py file automatically, it sets up layout and widgets that are defined
        self.home = Home()
        self.setCentralWidget(self.home)
        self.qclf = TrainingWidgetClassifier()
        self.qreg = TrainingWidgetRegressor()
        self.predclf = PredictorWidgetClassifier()
        self.predreg = PredictorWidgetRegressor()
        self.home.btn_qck_clf.clicked.connect(self.openClassifer)
        self.home.btn_qck_reg.clicked.connect(self.openRegressor)
        self.home.btn_pred_clf.clicked.connect(self.openPredictorClassifier)
        self.home.btn_pred_reg.clicked.connect(self.openPredictorRegressor)
        self.home.btn_recommend_clf.clicked.connect(self.openRecommenderClassifier)
        self.home.btn_recommend_reg.clicked.connect(self.openRecommenderClassifier)
        self.qclf.pushButton_finish.clicked.connect(self.openHome)
        self.qreg.pushButton_finish.clicked.connect(self.openHome)
        self.predclf.btn_finish.clicked.connect(self.openHome)
        self.predclf.btn_finish_rec.clicked.connect(self.openHome)
        self.predclf.btn_finish.clicked.connect(self.openHome)
        self.predclf.btn_finish_rec.clicked.connect(self.openHome)
        self.actionClassifier_q.triggered.connect(self.openClassifer)
        self.actionRegressor_q.triggered.connect(self.openRegressor)
        self.actionHome.triggered.connect(self.openHome)
        self.home.btn_recommend_clf.clicked.connect(self.openRecommenderClassifier)
        self.home.btn_recommend_reg.clicked.connect(self.openRecommenderRegressor)

    def openClassifer(self):
        self.qclf = TrainingWidgetClassifier()
        self.setCentralWidget(self.qclf)
        self.qclf.pushButton_finish.clicked.connect(self.openHome)

    def openRegressor(self):
        self.qreg = TrainingWidgetRegressor()
        self.setCentralWidget(self.qreg)
        self.qreg.pushButton_finish.clicked.connect(self.openHome)

    def openHome(self):
        self.home = Home()
        self.setCentralWidget(self.home)
        self.home.btn_qck_clf.clicked.connect(self.openClassifer)
        self.home.btn_qck_reg.clicked.connect(self.openRegressor)
        self.home.btn_pred_clf.clicked.connect(self.openPredictorClassifier)
        self.home.btn_pred_reg.clicked.connect(self.openPredictorRegressor)
        self.home.btn_recommend_clf.clicked.connect(self.openRecommenderClassifier)
        self.home.btn_recommend_reg.clicked.connect(self.openRecommenderRegressor)

    def openPredictorClassifier(self):
        self.predclf = PredictorWidgetClassifier()
        self.setCentralWidget(self.predclf)
        self.predclf.resetWidgetIndex()
        self.predclf.btn_finish.clicked.connect(self.openHome)
        self.predclf.btn_finish_rec.clicked.connect(self.openHome)

    def openPredictorRegressor(self):
        self.predreg = PredictorWidgetRegressor()
        self.setCentralWidget(self.predreg)
        self.predreg.resetWidgetIndex()
        self.predreg.btn_finish.clicked.connect(self.openHome)
        self.predreg.btn_finish_rec.clicked.connect(self.openHome)

    def openRecommenderClassifier(self):
        self.predclf = PredictorWidgetRegressor()
        self.setCentralWidget(self.predclf)
        self.predclf.openRecommender()
        self.predclf.btn_finish_rec.clicked.connect(self.openHome)

    def openRecommenderRegressor(self):
        self.predreg = PredictorWidgetRegressor()
        self.setCentralWidget(self.predreg)
        self.predreg.openRecommender()
        self.predreg.btn_finish_rec.clicked.connect(self.openHome)

class TrainingWidgetClassifier(QWidget, trainingwindow.Ui_Form):
    def __init__(self, parent=None):
        super(TrainingWidgetClassifier, self).__init__(parent)
        self.setupUi(self)
        self.training_type = 0
        self.scorers = []
        self.scorers = ["AUC", "Accuracy", "Precision", "Recall", "F1"]
        self.comboBox_scorer.addItems(self.scorers)
        self.lineEdit_threshold.setValidator(QIntValidator(0,50,self))
        self.lineEdit_threshold.setText("20")
        self.columns = []

class TrainingWidgetRegressor(QWidget, trainingwindow.Ui_Form):
    def __init__(self, parent=None):
        super(TrainingWidgetRegressor, self).__init__(parent)
        self.setupUi(self)
        self.training_type = 1
        self.qt_clf_text.setText("In this section the user can quickly configure a dataset to train a <b>regressor</b>. Upload a file from your computer, select the attributes you want to use, and click RUN! to start training a regressor.")
        self.scorers = []
        self.scorers = ["R2", "Variance", "RMSE"]
        self.comboBox_scorer.addItems(self.scorers)
        self.lineEdit_threshold.setValidator(QIntValidator(0, 50, self))
        self.lineEdit_threshold.setText("20")
        self.columns = []

class Home(QWidget, home.Ui_Form):
    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        self.setupUi(self)
        self.training_type = 0

class PredictorWidgetClassifier(QWidget, predictor.Ui_Form):
    def __init__(self, parent=None):
        super(PredictorWidgetClassifier, self).__init__(parent)
        self.setupUi(self)
        self.training_type=0

class PredictorWidgetRegressor(QWidget, predictor.Ui_Form):
    def __init__(self, parent=None):
        super(PredictorWidgetRegressor, self).__init__(parent)
        self.setupUi(self)
        self.training_type=1

def main():
    # app = QApplication(sys.argv) # A new instance of QApplication
    # app.setOrganizationName("Laurens Reulink")
    # app.setOrganizationDomain("UWV & TU/e")
    # app.setApplicationName("Koala")
    # app.setWindowIcon(QIcon(":/koala.png"))
    # form = MainWindow_UI()  #We set the form to be MainWindowUI design
    # form.show() #We show the form
    # sys.exit(app.exec_()) #We execute the application

    try:
        myApp = QApplication(sys.argv)
        myApp.setApplicationName("Koala")
        form = MainWindow_UI()
        form.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])

if __name__ == '__main__':  #if we're running file directly and not importing it
    main()                  #then we run the main function
    # try:
    #     myApp = QApplication(sys.argv)
    #     myApp.setApplicationName("Koala")
    #     mainWindow = MainWindow_UI
    #     myApp.exec_()
    #     sys.exit(0)
    # except NameError:
    #     print("Name Error:", sys.exc_info()[1])
    # except SystemExit:
    #     print("Closing Window...")
    # except Exception:
    #     print(sys.exc_info()[1])


