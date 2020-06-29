
from mongoengine import *
from PySide2.QtWidgets import QApplication, QMainWindow
from FormaTarea5 import  Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.PB_Registrar.clicked.connect(self.Registrar)
        self.ui.PB_Actualizar.clicked.connect(self.Acutalizar)
        self.ui.PB_Consultar.clicked.connect(self.Consultar)
        self.ui.PB_Eliminar.clicked.connect(self.Eliminar)

    def Registrar(self):
        nombre = self.ui.LE_Nombre_Ingreso.text()
        email = self.ui.LE_Email_Ingreso.text()
        contra = self.ui.LE_Contra_Ingreso.text()
        res = saveMongo(nombre, email, contra)
        if res:
            self.ui.LE_Estatus_Ingreso.setPlaceholderText('Guardado con exito')
        else:
            self.ui.LE_Estatus_Ingreso.setPlaceholderText('El registro ya existe')

    def Acutalizar(self):
        nombre = self.ui.LE_Nombre_Ingreso.text()
        email = self.ui.LE_Email_Ingreso.text()
        contra = self.ui.LE_Contra_Ingreso.text()
        res = updateMongo(nombre, email, contra)
        if res:
            self.ui.LE_Estatus_Ingreso.setPlaceholderText('Actualizado con exito')
        else:
            self.ui.LE_Estatus_Ingreso.setPlaceholderText('No se encontró el registro para Actualizar')


    def Consultar(self):
        nombre = self.ui.LE_Nombre_Consulta.text()
        res = readMongo(nombre)
        if res != False:
            self.ui.LE_Email_Consulta.setPlaceholderText(res.email)
            self.ui.LE_Contra_Consulta.setPlaceholderText(res.contrasena)
            self.ui.LE_Estatus_Consulta.setPlaceholderText('Leido con exito')
        else:
            self.ui.LE_Email_Consulta.setPlaceholderText('-')
            self.ui.LE_Contra_Consulta.setPlaceholderText('-')
            self.ui.LE_Estatus_Consulta.setPlaceholderText('No se Encontró el registro para Consultar')


    def Eliminar(self):
        nombre = self.ui.LE_Nombre_Borrar.text()
        res = deleteMongo(nombre)
        if res:
            self.ui.LE_Estatus_Borrar.setPlaceholderText('Eliminado con exito')
        else:
            self.ui.LE_Estatus_Borrar.setPlaceholderText('No se Encontró el registro para Eliminar')



class estudiantes(Document):
    nombre      = StringField(required=True)
    email       = StringField(required=True)
    contrasena  = StringField(required=True)

def saveMongo(nombre,email,contrasena):
    estudiante_db = estudiantes(nombre = nombre,
                                email = email,
                                contrasena= contrasena)
    datos = estudiantes.objects
    for e in datos:
        if e.nombre == nombre:
            return False

    estudiante_db.save()
    return True

def updateMongo(nombre,email,contrasena):
    datos = estudiantes.objects
    for e in datos:
        if e.nombre == nombre:
            e.modify(nombre = nombre,
                     email = email,
                     contrasena= contrasena)
            return True
    return False

def readMongo(nombre):
    datos = estudiantes.objects
    for e in datos:
        if e.nombre == nombre:
            return e
    return False

def deleteMongo(nombre):
    datos = estudiantes.objects
    for e in datos:
        if e.nombre == nombre:
            e.delete()
            return True
    return False



if __name__ == '__main__':
    connect('padts')

    app = QApplication()
    window = MainWindow()
    window.show()

    app.exec_()