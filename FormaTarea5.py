# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormaTarea5.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(470, 479)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 60, 331, 131))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.LE_Nombre_Ingreso = QLineEdit(self.formLayoutWidget)
        self.LE_Nombre_Ingreso.setObjectName(u"LE_Nombre_Ingreso")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.LE_Nombre_Ingreso)

        self.LE_Email_Ingreso = QLineEdit(self.formLayoutWidget)
        self.LE_Email_Ingreso.setObjectName(u"LE_Email_Ingreso")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.LE_Email_Ingreso)

        self.LE_Contra_Ingreso = QLineEdit(self.formLayoutWidget)
        self.LE_Contra_Ingreso.setObjectName(u"LE_Contra_Ingreso")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.LE_Contra_Ingreso)

        self.QL_Nombre_Ingreso = QLabel(self.formLayoutWidget)
        self.QL_Nombre_Ingreso.setObjectName(u"QL_Nombre_Ingreso")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.QL_Nombre_Ingreso)

        self.QL_Email_Ingreso = QLabel(self.formLayoutWidget)
        self.QL_Email_Ingreso.setObjectName(u"QL_Email_Ingreso")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.QL_Email_Ingreso)

        self.QL_Contra_Ingreso = QLabel(self.formLayoutWidget)
        self.QL_Contra_Ingreso.setObjectName(u"QL_Contra_Ingreso")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.QL_Contra_Ingreso)

        self.QL_Estatus_Ingreso = QLabel(self.formLayoutWidget)
        self.QL_Estatus_Ingreso.setObjectName(u"QL_Estatus_Ingreso")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.QL_Estatus_Ingreso)

        self.LE_Estatus_Ingreso = QLineEdit(self.formLayoutWidget)
        self.LE_Estatus_Ingreso.setObjectName(u"LE_Estatus_Ingreso")
        self.LE_Estatus_Ingreso.setEnabled(False)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.LE_Estatus_Ingreso)

        self.label_Ingreso = QLabel(self.formLayoutWidget)
        self.label_Ingreso.setObjectName(u"label_Ingreso")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_Ingreso)

        self.PB_Actualizar = QPushButton(self.centralwidget)
        self.PB_Actualizar.setObjectName(u"PB_Actualizar")
        self.PB_Actualizar.setGeometry(QRect(380, 110, 75, 23))
        self.PB_Registrar = QPushButton(self.centralwidget)
        self.PB_Registrar.setObjectName(u"PB_Registrar")
        self.PB_Registrar.setGeometry(QRect(380, 80, 75, 23))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 451, 29))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.formLayoutWidget_2 = QWidget(self.centralwidget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(20, 200, 331, 131))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.LE_Nombre_Consulta = QLineEdit(self.formLayoutWidget_2)
        self.LE_Nombre_Consulta.setObjectName(u"LE_Nombre_Consulta")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.LE_Nombre_Consulta)

        self.LE_Email_Consulta = QLineEdit(self.formLayoutWidget_2)
        self.LE_Email_Consulta.setObjectName(u"LE_Email_Consulta")
        self.LE_Email_Consulta.setEnabled(False)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.LE_Email_Consulta)

        self.LE_Contra_Consulta = QLineEdit(self.formLayoutWidget_2)
        self.LE_Contra_Consulta.setObjectName(u"LE_Contra_Consulta")
        self.LE_Contra_Consulta.setEnabled(False)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.LE_Contra_Consulta)

        self.QL_Nombre_Consulta = QLabel(self.formLayoutWidget_2)
        self.QL_Nombre_Consulta.setObjectName(u"QL_Nombre_Consulta")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.QL_Nombre_Consulta)

        self.QL_Email_Consulta = QLabel(self.formLayoutWidget_2)
        self.QL_Email_Consulta.setObjectName(u"QL_Email_Consulta")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.QL_Email_Consulta)

        self.QL_Contra_Consulta = QLabel(self.formLayoutWidget_2)
        self.QL_Contra_Consulta.setObjectName(u"QL_Contra_Consulta")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.QL_Contra_Consulta)

        self.QL_Estatus_Consulta = QLabel(self.formLayoutWidget_2)
        self.QL_Estatus_Consulta.setObjectName(u"QL_Estatus_Consulta")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.QL_Estatus_Consulta)

        self.LE_Estatus_Consulta = QLineEdit(self.formLayoutWidget_2)
        self.LE_Estatus_Consulta.setObjectName(u"LE_Estatus_Consulta")
        self.LE_Estatus_Consulta.setEnabled(False)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.LE_Estatus_Consulta)

        self.label_Consulta = QLabel(self.formLayoutWidget_2)
        self.label_Consulta.setObjectName(u"label_Consulta")

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.label_Consulta)

        self.formLayoutWidget_3 = QWidget(self.centralwidget)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(20, 340, 331, 81))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_Borrar = QLabel(self.formLayoutWidget_3)
        self.label_Borrar.setObjectName(u"label_Borrar")

        self.formLayout_3.setWidget(0, QFormLayout.SpanningRole, self.label_Borrar)

        self.QL_Nombre_Borrar = QLabel(self.formLayoutWidget_3)
        self.QL_Nombre_Borrar.setObjectName(u"QL_Nombre_Borrar")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.QL_Nombre_Borrar)

        self.LE_Nombre_Borrar = QLineEdit(self.formLayoutWidget_3)
        self.LE_Nombre_Borrar.setObjectName(u"LE_Nombre_Borrar")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.LE_Nombre_Borrar)

        self.QL_Estatus_Borrar = QLabel(self.formLayoutWidget_3)
        self.QL_Estatus_Borrar.setObjectName(u"QL_Estatus_Borrar")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.QL_Estatus_Borrar)

        self.LE_Estatus_Borrar = QLineEdit(self.formLayoutWidget_3)
        self.LE_Estatus_Borrar.setObjectName(u"LE_Estatus_Borrar")
        self.LE_Estatus_Borrar.setEnabled(False)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.LE_Estatus_Borrar)

        self.PB_Consultar = QPushButton(self.centralwidget)
        self.PB_Consultar.setObjectName(u"PB_Consultar")
        self.PB_Consultar.setGeometry(QRect(380, 220, 75, 23))
        self.PB_Eliminar = QPushButton(self.centralwidget)
        self.PB_Eliminar.setObjectName(u"PB_Eliminar")
        self.PB_Eliminar.setGeometry(QRect(380, 360, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 470, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.QL_Nombre_Ingreso.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.QL_Email_Ingreso.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.QL_Contra_Ingreso.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.QL_Estatus_Ingreso.setText(QCoreApplication.translate("MainWindow", u"Estatus", None))
        self.label_Ingreso.setText(QCoreApplication.translate("MainWindow", u"Nuevo Registro o Actualizar Registro", None))
        self.PB_Actualizar.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.PB_Registrar.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Mongo Engine Conectado a coleccion : PADTS", None))
        self.QL_Nombre_Consulta.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.QL_Email_Consulta.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.QL_Contra_Consulta.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.QL_Estatus_Consulta.setText(QCoreApplication.translate("MainWindow", u"Estatus", None))
        self.label_Consulta.setText(QCoreApplication.translate("MainWindow", u"Consultar Registro", None))
        self.label_Borrar.setText(QCoreApplication.translate("MainWindow", u"Eliminar Registro", None))
        self.QL_Nombre_Borrar.setText(QCoreApplication.translate("MainWindow", u"Nombre     ", None))
        self.QL_Estatus_Borrar.setText(QCoreApplication.translate("MainWindow", u"Estatus", None))
        self.PB_Consultar.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.PB_Eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
    # retranslateUi

