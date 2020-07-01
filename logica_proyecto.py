
from PySide2.QtWidgets import QApplication, QMainWindow
from ui_proyecto import Ui_MainWindow
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import socket as s
import pickle
import time

class Estudiante:
    __nombre = ''
    __email = ''
    __contrasena = ''

    def __init__(self, nombre, email, contrasena):
        self.__nombre = nombre
        self.__email = email
        self.__contrasena = contrasena

    def setNombre(self,nom):
        self.__nombre = nom

    def setEmail(self,mail):
        self.__email = mail

    def setContra(self,contra):
        self.__contrasena=contra

    def getNombre(self):
        return self.__nombre

    def getEmail(self):
        return self.__email

    def getContra(self):
        return self.__contrasena

class ClienteTCP:

    def __init__(self,ip =  '127.0.0.1', port = 35491):
        self.cliente = s.socket()
        self.cliente.connect((ip, port))


    def clntEscribir(self, mensaje):
        #bytess = mensaje.encode()
        self.cliente.send(mensaje)


    def clntRecibir(self):
        self.data = self.cliente.recv(1024)
        print(self.data)
        return self.data

    def Close(self):
        ##Cerrar conexion
        bytess = 'exit'.encode()
        self.cliente.send(bytess)
        self.cliente.close()

class MainWindow(QMainWindow):
    def  __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.filename = r''

        #Eliminar estas sentencias
        self.ui.LE_IP.setText('127.0.0.1')
        self.ui.LE_Puerto.setText('35491')
        ####################################


        self.ui.PB_Conectar.clicked.connect(self.Conectar)
        self.ui.PB_EnviarEstudiante.clicked.connect(self.EnviarEstudiante)
        self.ui.PB_Buscar.clicked.connect(self.Buscar)
        self.ui.PB_EnviarArchivo.clicked.connect(self.EnviarArchivo)


    def Conectar(self):
        if self.ui.PB_Conectar.text() == 'Conectar':
            ip = self.ui.LE_IP.text()
            port = int(self.ui.LE_Puerto.text())
            self.cliente = ClienteTCP(ip, port)

            self.ui.PB_Conectar.setText('Desconectar')
            self.ui.label_Servidor.setText('Conectado')
            self.ui.LE_IP.setDisabled(True)
            self.ui.LE_Puerto.setDisabled(True)

            self.ui.LE_Nombre.setEnabled(True)
            self.ui.LE_Correo.setEnabled(True)
            self.ui.LE_Contrasena.setEnabled(True)
            self.ui.PB_EnviarEstudiante.setEnabled(True)

        else:
            self.cliente.Close()
            self.ui.PB_Conectar.setText('Conectar')
            self.ui.label_Servidor.setText('Desconectado')
            self.ui.LE_IP.setEnabled(True)
            self.ui.LE_Puerto.setEnabled(True)

            self.ui.LE_Buscar.setDisabled(True)
            self.ui.LE_Nombre.setDisabled(True)
            self.ui.LE_Correo.setDisabled(True)
            self.ui.LE_Contrasena.setDisabled(True)
            self.ui.PB_EnviarEstudiante.setDisabled(True)
            self.ui.PB_Buscar.setDisabled(True)
            self.ui.PB_EnviarArchivo.setDisabled(True)

    def EnviarEstudiante(self):
        nombre = self.ui.LE_Nombre.text()
        correo = self.ui.LE_Correo.text()
        contrasena = self.ui.LE_Contrasena.text()
        objEstudiante = Estudiante(nombre,correo,contrasena)
        serEstudiante = pickle.dumps(objEstudiante)
        self.cliente.clntEscribir(serEstudiante)

        self.ui.PB_EnviarEstudiante.setDisabled(True)
        self.ui.LE_Nombre.setDisabled(True)
        self.ui.LE_Correo.setDisabled(True)
        self.ui.LE_Contrasena.setDisabled(True)
        self.ui.label_Estudiante.setText('Enviando...')

        envio = self.cliente.clntRecibir()

        self.ui.PB_EnviarEstudiante.setEnabled(True)
        self.ui.LE_Nombre.setEnabled(True)
        self.ui.LE_Correo.setEnabled(True)
        self.ui.LE_Contrasena.setEnabled(True)
        self.ui.label_Estudiante.setText('Enviado')

        if envio == b'enviararchivo':
            self.ui.PB_EnviarArchivo.setEnabled(True)
            self.ui.PB_Buscar.setEnabled(True)
            self.ui.LE_Buscar.setEnabled(True)
            self.ui.label_Archivo.setText('Peticion recibida')

    def Buscar(self):
        Tk().withdraw()
        self.filename = askopenfilename()
        print(self.filename)
        self.ui.LE_Buscar.setText(self.filename)
        self.ui.label_Archivo.setText('Archivo listo para enviar')

    def EnviarArchivo(self):
        if self.filename != r'':

            self.ui.PB_EnviarArchivo.setDisabled(True)
            self.ui.PB_Buscar.setDisabled(True)
            self.ui.LE_Buscar.setDisabled(True)
            self.ui.label_Archivo.setText('Enviando...')

            file = open(self.filename, 'rb')
            fileData = file.read()
            serFileData = pickle.dumps(fileData)

            self.cliente.clntEscribir('iniciozip'.encode())

            tamano = len(serFileData);
            limite = 0
            while limite < tamano:

                if limite+500 <= tamano:
                    self.cliente.clntEscribir(serFileData[limite: limite+500])
                    limite = limite+500
                else:
                    self.cliente.clntEscribir(serFileData[limite: limite+500])
                    limite = len(serFileData)

            #time.sleep(.20)
            self.cliente.clntEscribir('finzip'.encode())

            self.ui.PB_EnviarArchivo.setEnabled(True)
            self.ui.PB_Buscar.setEnabled(True)
            self.ui.LE_Buscar.setEnabled(True)
            self.ui.label_Archivo.setText('Enviado')
            file.close()
        else:
            self.ui.label_Archivo.setText('Debes seleccionar un archivo primero')
