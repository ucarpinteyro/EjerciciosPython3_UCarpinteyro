# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'proyecto.ui'
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
        MainWindow.resize(422, 450)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(422, 450))
        MainWindow.setMaximumSize(QSize(422, 450))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 401, 111))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 130, 401, 151))
        self.verticalLayoutWidget_2 = QWidget(self.groupBox_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 20, 381, 125))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_Nombre = QLabel(self.verticalLayoutWidget_2)
        self.label_Nombre.setObjectName(u"label_Nombre")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_Nombre)

        self.label_Correo = QLabel(self.verticalLayoutWidget_2)
        self.label_Correo.setObjectName(u"label_Correo")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_Correo)

        self.label_Contrasena = QLabel(self.verticalLayoutWidget_2)
        self.label_Contrasena.setObjectName(u"label_Contrasena")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_Contrasena)

        self.LE_Nombre = QLineEdit(self.verticalLayoutWidget_2)
        self.LE_Nombre.setObjectName(u"LE_Nombre")
        self.LE_Nombre.setEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.LE_Nombre)

        self.LE_Correo = QLineEdit(self.verticalLayoutWidget_2)
        self.LE_Correo.setObjectName(u"LE_Correo")
        self.LE_Correo.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.LE_Correo)

        self.LE_Contrasena = QLineEdit(self.verticalLayoutWidget_2)
        self.LE_Contrasena.setObjectName(u"LE_Contrasena")
        self.LE_Contrasena.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.LE_Contrasena)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.PB_EnviarEstudiante = QPushButton(self.verticalLayoutWidget_2)
        self.PB_EnviarEstudiante.setObjectName(u"PB_EnviarEstudiante")
        self.PB_EnviarEstudiante.setEnabled(False)

        self.verticalLayout_2.addWidget(self.PB_EnviarEstudiante)

        self.label_Estudiante = QLabel(self.verticalLayoutWidget_2)
        self.label_Estudiante.setObjectName(u"label_Estudiante")

        self.verticalLayout_2.addWidget(self.label_Estudiante)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 290, 401, 111))
        self.verticalLayoutWidget_3 = QWidget(self.groupBox_3)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 20, 381, 81))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.PB_Buscar = QPushButton(self.verticalLayoutWidget_3)
        self.PB_Buscar.setObjectName(u"PB_Buscar")
        self.PB_Buscar.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.PB_Buscar)

        self.LE_Buscar = QLineEdit(self.verticalLayoutWidget_3)
        self.LE_Buscar.setObjectName(u"LE_Buscar")
        self.LE_Buscar.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.LE_Buscar)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.PB_EnviarArchivo = QPushButton(self.verticalLayoutWidget_3)
        self.PB_EnviarArchivo.setObjectName(u"PB_EnviarArchivo")
        self.PB_EnviarArchivo.setEnabled(False)

        self.verticalLayout_3.addWidget(self.PB_EnviarArchivo)

        self.label_Archivo = QLabel(self.verticalLayoutWidget_3)
        self.label_Archivo.setObjectName(u"label_Archivo")

        self.verticalLayout_3.addWidget(self.label_Archivo)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 30, 381, 91))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_IP = QLabel(self.verticalLayoutWidget)
        self.label_IP.setObjectName(u"label_IP")

        self.horizontalLayout.addWidget(self.label_IP)

        self.LE_IP = QLineEdit(self.verticalLayoutWidget)
        self.LE_IP.setObjectName(u"LE_IP")

        self.horizontalLayout.addWidget(self.LE_IP)

        self.label_Puerto = QLabel(self.verticalLayoutWidget)
        self.label_Puerto.setObjectName(u"label_Puerto")

        self.horizontalLayout.addWidget(self.label_Puerto)

        self.LE_Puerto = QLineEdit(self.verticalLayoutWidget)
        self.LE_Puerto.setObjectName(u"LE_Puerto")

        self.horizontalLayout.addWidget(self.LE_Puerto)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.PB_Conectar = QPushButton(self.verticalLayoutWidget)
        self.PB_Conectar.setObjectName(u"PB_Conectar")

        self.verticalLayout.addWidget(self.PB_Conectar)

        self.label_Servidor = QLabel(self.verticalLayoutWidget)
        self.label_Servidor.setObjectName(u"label_Servidor")
        self.label_Servidor.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.label_Servidor)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 422, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cliente Ulises Carpinteyro", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Servidor", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Estudiante", None))
        self.label_Nombre.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_Correo.setText(QCoreApplication.translate("MainWindow", u"Correo: ", None))
        self.label_Contrasena.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a:", None))
        self.PB_EnviarEstudiante.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.label_Estudiante.setText(QCoreApplication.translate("MainWindow", u"En espera", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.PB_Buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.PB_EnviarArchivo.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.label_Archivo.setText(QCoreApplication.translate("MainWindow", u"En espera", None))
        self.label_IP.setText(QCoreApplication.translate("MainWindow", u"IP:", None))
        self.label_Puerto.setText(QCoreApplication.translate("MainWindow", u"Puerto:", None))
        self.PB_Conectar.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.label_Servidor.setText(QCoreApplication.translate("MainWindow", u"Desconectado", None))
    # retranslateUi

