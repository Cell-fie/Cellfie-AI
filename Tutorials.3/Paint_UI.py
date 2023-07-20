# Form implementation generated from reading ui file 'Paint_UI.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(992, 468)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 992, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuBrush_Size = QtWidgets.QMenu(parent=self.menubar)
        self.menuBrush_Size.setObjectName("menuBrush_Size")
        self.menuBrush_Color = QtWidgets.QMenu(parent=self.menubar)
        self.menuBrush_Color.setObjectName("menuBrush_Color")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtGui.QAction(parent=MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionClear = QtGui.QAction(parent=MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.action3px = QtGui.QAction(parent=MainWindow)
        self.action3px.setObjectName("action3px")
        self.action5px = QtGui.QAction(parent=MainWindow)
        self.action5px.setObjectName("action5px")
        self.action7px = QtGui.QAction(parent=MainWindow)
        self.action7px.setObjectName("action7px")
        self.action9px = QtGui.QAction(parent=MainWindow)
        self.action9px.setObjectName("action9px")
        self.actionBlack = QtGui.QAction(parent=MainWindow)
        self.actionBlack.setObjectName("actionBlack")
        self.actionWhite = QtGui.QAction(parent=MainWindow)
        self.actionWhite.setObjectName("actionWhite")
        self.actionRed = QtGui.QAction(parent=MainWindow)
        self.actionRed.setObjectName("actionRed")
        self.actionGreen = QtGui.QAction(parent=MainWindow)
        self.actionGreen.setObjectName("actionGreen")
        self.actionBlue = QtGui.QAction(parent=MainWindow)
        self.actionBlue.setObjectName("actionBlue")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionClear)
        self.menuBrush_Size.addAction(self.action3px)
        self.menuBrush_Size.addAction(self.action5px)
        self.menuBrush_Size.addAction(self.action7px)
        self.menuBrush_Size.addAction(self.action9px)
        self.menuBrush_Color.addAction(self.actionBlack)
        self.menuBrush_Color.addAction(self.actionWhite)
        self.menuBrush_Color.addAction(self.actionRed)
        self.menuBrush_Color.addAction(self.actionGreen)
        self.menuBrush_Color.addAction(self.actionBlue)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuBrush_Size.menuAction())
        self.menubar.addAction(self.menuBrush_Color.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuBrush_Size.setTitle(_translate("MainWindow", "Brush Size"))
        self.menuBrush_Color.setTitle(_translate("MainWindow", "Brush Color"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionClear.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.action3px.setText(_translate("MainWindow", "3px"))
        self.action3px.setShortcut(_translate("MainWindow", "Ctrl+3"))
        self.action5px.setText(_translate("MainWindow", "5px"))
        self.action5px.setShortcut(_translate("MainWindow", "Ctrl+5"))
        self.action7px.setText(_translate("MainWindow", "7px"))
        self.action7px.setShortcut(_translate("MainWindow", "Ctrl+7"))
        self.action9px.setText(_translate("MainWindow", "9px"))
        self.action9px.setShortcut(_translate("MainWindow", "Ctrl+9"))
        self.actionBlack.setText(_translate("MainWindow", "Black"))
        self.actionWhite.setText(_translate("MainWindow", "White"))
        self.actionRed.setText(_translate("MainWindow", "Red"))
        self.actionGreen.setText(_translate("MainWindow", "Green"))
        self.actionBlue.setText(_translate("MainWindow", "Blue"))
