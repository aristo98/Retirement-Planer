# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'retirement_plan.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from maincode import Retirement_Plan as RP
import os

class GUI(object):
    def setupUi(self, MainWindow):
        '''Main Window'''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(552, 811)
        MainWindow.setMinimumSize(QtCore.QSize(552, 811))
        MainWindow.setMaximumSize(QtCore.QSize(552, 811))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        '''Create tabs'''
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 552, 811))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.addTab(self.tab_2, "")
        
        '''Set Font'''
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font2 = QtGui.QFont()
        font2.setFamily("Times New Roman")
        font2.setPointSize(10)
        
        '''Savings plan tab'''
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(41, 41, 99, 23))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(41, 85, 100, 23))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(41, 129, 145, 24))
        self.label_3.setFont(font)
        self.label_3.setWordWrap(False)
        self.label_3.setIndent(-1)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(41, 173, 151, 23))
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(211, 41, 129, 23))
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(370, 41, 111, 23))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setToolTip("Immediate: Savings is done in the beginning of each period"+\
                                 "\nDue: Savings is done at the end of each period\n\n"+\
                                     "This option plays a role if and only if interest is paid at least \n"+\
                                         "as frequent as savings intervall."+\
                                             " Otherwise, immediate-option is chosen")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 85, 129, 23))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(211, 129, 61, 24))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(211, 173, 129, 23))
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(370, 85, 111, 23))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setToolTip("Choose your savings intervall")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(275, 129, 21, 23))
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab)
        self.comboBox_3.setGeometry(QtCore.QRect(370, 129, 111, 23))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setToolTip("Choose the period of interest payment")
        self.comboBox_3.setCurrentIndex(1)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(370, 170, 121, 51))
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.savingsPlan)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(50, 230, 451, 301))
        self.label_4.setStyleSheet("border: 1px solid black;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(font2)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(50, 550, 451, 180))
        self.label_7.setStyleSheet("border: 1px solid black;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_7.setFont(font2)
        
        '''Withdrawal plan tab'''
        self.label_sh = QtWidgets.QLabel(self.tab_2)
        self.label_sh.setGeometry(QtCore.QRect(41, 41, 99, 23))
        self.label_sh.setFont(font)
        self.label_sh.setObjectName("label_sh")
        self.label_2_sh = QtWidgets.QLabel(self.tab_2)
        self.label_2_sh.setGeometry(QtCore.QRect(41, 85, 141, 23))
        self.label_2_sh.setFont(font)
        self.label_2_sh.setObjectName("label_2_sh")
        self.label_3_sh = QtWidgets.QLabel(self.tab_2)
        self.label_3_sh.setGeometry(QtCore.QRect(41, 129, 145, 24))
        self.label_3_sh.setFont(font)
        self.label_3_sh.setWordWrap(False)
        self.label_3_sh.setIndent(-1)
        self.label_3_sh.setObjectName("label_3_sh")
        self.label_5_sh = QtWidgets.QLabel(self.tab_2)
        self.label_5_sh.setGeometry(QtCore.QRect(41, 173, 151, 23))
        self.label_5_sh.setFont(font)
        self.label_5_sh.setObjectName("label_5_sh")
        self.lineEdit_sh = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_sh.setGeometry(QtCore.QRect(211, 41, 129, 23))
        self.lineEdit_sh.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_sh.setObjectName("lineEdit_sh")
        self.comboBox_sh = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_sh.setGeometry(QtCore.QRect(370, 41, 111, 23))
        self.comboBox_sh.setObjectName("comboBox_sh")
        self.comboBox_sh.addItem("")
        self.comboBox_sh.addItem("")
        self.comboBox_sh.setToolTip("Immediate: Withdrawal is done in the beginning of each period"+\
                                 "\nDue: Withdrawal is done at the end of each period\n\n"+\
                                     "This option plays a role if and only if interest is paid at least \n"+\
                                         "as frequent as savings intervall."+\
                                             " Otherwise, due-option is chosen")
        self.lineEdit_2_sh = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2_sh.setGeometry(QtCore.QRect(210, 85, 129, 23))
        self.lineEdit_2_sh.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_2_sh.setObjectName("lineEdit_2_sh")
        self.lineEdit_3_sh = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3_sh.setGeometry(QtCore.QRect(211, 129, 61, 24))
        self.lineEdit_3_sh.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_3_sh.setObjectName("lineEdit_3_sh")
        self.lineEdit_4_sh = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4_sh.setGeometry(QtCore.QRect(211, 173, 129, 23))
        self.lineEdit_4_sh.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_4_sh.setObjectName("lineEdit_4_sh")
        self.comboBox_2_sh = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2_sh.setGeometry(QtCore.QRect(370, 85, 111, 23))
        self.comboBox_2_sh.setObjectName("comboBox_2_sh")
        self.comboBox_2_sh.addItem("")
        self.comboBox_2_sh.addItem("")
        self.comboBox_2_sh.addItem("")
        self.comboBox_2_sh.addItem("")
        self.comboBox_2_sh.setToolTip("Choose your savings intervall")
        self.label_6_sh = QtWidgets.QLabel(self.tab_2)
        self.label_6_sh.setGeometry(QtCore.QRect(275, 129, 21, 23))
        self.label_6_sh.setFont(font)
        self.label_6_sh.setObjectName("label_6_sh")
        self.comboBox_3_sh = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_3_sh.setGeometry(QtCore.QRect(370, 129, 111, 23))
        self.comboBox_3_sh.setObjectName("comboBox_3_sh")
        self.comboBox_3_sh.addItem("")
        self.comboBox_3_sh.addItem("")
        self.comboBox_3_sh.addItem("")
        self.comboBox_3_sh.addItem("")
        self.comboBox_3_sh.addItem("")
        self.comboBox_3_sh.setToolTip("Choose the period of interest payment")
        self.comboBox_3_sh.setCurrentIndex(1)
        self.pushButton_sh = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_sh.setGeometry(QtCore.QRect(370, 170, 121, 51))
        self.pushButton_sh.setFont(font)
        self.pushButton_sh.setObjectName("pushButton_sh")
        self.pushButton_sh.clicked.connect(self.withdrawalPlan)
        self.label_4_sh = QtWidgets.QLabel(self.tab_2)
        self.label_4_sh.setGeometry(QtCore.QRect(50, 230, 451, 301))
        self.label_4_sh.setStyleSheet("border: 1px solid black;")
        self.label_4_sh.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4_sh.setObjectName("label_4_sh")
        self.label_4_sh.setFont(font2)
        self.label_7_sh = QtWidgets.QLabel(self.tab_2)
        self.label_7_sh.setGeometry(QtCore.QRect(50, 550, 451, 180))
        self.label_7_sh.setStyleSheet("border: 1px solid black;")
        self.label_7_sh.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7_sh.setObjectName("label_7_sh")
        self.label_7_sh.setFont(font2)
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def savingsPlan(self):
        try:float(self.lineEdit.text()) and float(self.lineEdit_2.text()) and float(self.lineEdit_3.text())
        except:"Please insert only non-negative numbers in start capital, savings rate, and interest rate"
        assert float(self.lineEdit.text())>=0 and float(self.lineEdit_2.text())>=0 and float(self.lineEdit_3.text())>=0 ,\
            "Please insert only non-negative numbers in start capital, savings rate, and interest rate"
        assert float(self.lineEdit_4.text())-int(self.lineEdit_4.text())==0, "Please insert only integers in duration"
        self.savPlan=RP(float(self.lineEdit.text()),self.comboBox.currentText().lower(),float(self.lineEdit_2.text()),self.comboBox_2.currentText()[0],\
                        float(self.lineEdit_3.text())/100,self.comboBox_3.currentText()[0],int(self.lineEdit_4.text()))
        self.savPlan.calculate_and_plot()
        fname=os.getcwd()+"\\image.png"
        self.pixmap=QtGui.QPixmap(fname).scaledToWidth(451)
        self.label_4.setPixmap(self.pixmap)
        self.label_7.setText(self.savPlan.tb_displayed)
        
        self.lineEdit_sh.setText(str(self.savPlan.savings[-1]*1000))
        self.lineEdit_2_sh.setText(str(int(self.savPlan.savings[-1]*1000*0.05/12)))
        
        
    def withdrawalPlan(self):
        try:float(self.lineEdit_sh.text()) and float(self.lineEdit_2_sh.text()) and float(self.lineEdit_3_sh.text())
        except:"Please insert only non-negative numbers in start capital, withdrawal rate, and interest rate"
        assert float(self.lineEdit_sh.text())>=0 and float(self.lineEdit_2_sh.text())>=0 and float(self.lineEdit_3_sh.text())>=0 ,\
            "Please insert only non-negative numbers in start capital, withdrawal rate, and interest rate"
        assert float(self.lineEdit_4_sh.text())-int(self.lineEdit_4_sh.text())==0, "Please insert only integers in duration"
        self.withdrawPlan=RP(float(self.lineEdit_sh.text()),self.comboBox_sh.currentText().lower(),-float(self.lineEdit_2_sh.text()),\
                             self.comboBox_2_sh.currentText()[0],float(self.lineEdit_3_sh.text())/100,self.comboBox_3_sh.currentText()[0],\
                                 int(self.lineEdit_4_sh.text()))
        self.withdrawPlan.calculate_and_plot()
        fname=os.getcwd()+"\\image2.png"
        self.pixmap=QtGui.QPixmap(fname).scaledToWidth(451)
        self.label_4_sh.setPixmap(self.pixmap)
        self.label_7_sh.setText(self.withdrawPlan.tb_displayed)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Retirement Plan"))
        
        '''Savings plan'''
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Savings plan"))
        self.label.setText(_translate("MainWindow", "Start capital"))
        self.label_2.setText(_translate("MainWindow", "Savings rate"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Interest rate (p.a.)</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Duration (years)"))
        self.lineEdit.setText(_translate("MainWindow", "5000"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Immediate"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Due"))
        self.lineEdit_2.setText(_translate("MainWindow", "500"))
        self.lineEdit_3.setText(_translate("MainWindow", "5.0"))
        self.lineEdit_4.setText(_translate("MainWindow", "15"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Monthly"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Quarterly"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Half-yearly"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Yearly"))
        self.label_6.setText(_translate("MainWindow", "%"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Continuosly"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Monthly"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Quarterly"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Half-yearly"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Yearly"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.label_4.setText(_translate("MainWindow", "empty"))
        self.label_7.setText(_translate("MainWindow", "empty"))
        
        '''Withdrawal plan'''
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Withdrawal plan"))
        self.label_sh.setText(_translate("MainWindow", "Start capital"))
        self.label_2_sh.setText(_translate("MainWindow", "Withdrawal rate"))
        self.label_3_sh.setText(_translate("MainWindow", "<html><head/><body><p>Interest rate (p.a.)</p></body></html>"))
        self.label_5_sh.setText(_translate("MainWindow", "Duration (years)"))
        self.lineEdit_sh.setText(_translate("MainWindow", "200000"))
        self.comboBox_sh.setItemText(0, _translate("MainWindow", "Immediate"))
        self.comboBox_sh.setItemText(1, _translate("MainWindow", "Due"))
        self.lineEdit_2_sh.setText(_translate("MainWindow", "300"))
        self.lineEdit_3_sh.setText(_translate("MainWindow", "5.0"))
        self.lineEdit_4_sh.setText(_translate("MainWindow", "20"))
        self.comboBox_2_sh.setItemText(0, _translate("MainWindow", "Monthly"))
        self.comboBox_2_sh.setItemText(1, _translate("MainWindow", "Quarterly"))
        self.comboBox_2_sh.setItemText(2, _translate("MainWindow", "Half-yearly"))
        self.comboBox_2_sh.setItemText(3, _translate("MainWindow", "Yearly"))
        self.label_6_sh.setText(_translate("MainWindow", "%"))
        self.comboBox_3_sh.setItemText(0, _translate("MainWindow", "Continuosly"))
        self.comboBox_3_sh.setItemText(1, _translate("MainWindow", "Monthly"))
        self.comboBox_3_sh.setItemText(2, _translate("MainWindow", "Quarterly"))
        self.comboBox_3_sh.setItemText(3, _translate("MainWindow", "Half-yearly"))
        self.comboBox_3_sh.setItemText(4, _translate("MainWindow", "Yearly"))
        self.pushButton_sh.setText(_translate("MainWindow", "Calculate"))
        self.label_4_sh.setText(_translate("MainWindow", "empty"))
        self.label_7_sh.setText(_translate("MainWindow", "empty"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
