
class Figuras:
    nlados = 0
    perimetro = 0
    area = 0

    def setLados(self, num):
        self.nlados = num

    def setPerimetro(self, num):
        self.perimetro = num

    def setArea(self, num):
        self.area = num

    def mostrarDatos(self):
        print('Tiene {} lados'.format(self.nlados))
        print('Tiene un perimetro de {} '.format(self.perimetro) )
        print('Tiene un area de {}'.format(self.area))

    def reiniciar(self):
        self.nlados = 0
        self.perimetro = 0
        self.area = 0


class Rectangulo(Figuras):
    largo = 0
    ancho = 0

    def __init__(self,argLados, argLargo, argAncho):
        self.nlados = argLados
        self.largo = argLargo
        self.ancho = argAncho

    def calcPerimetro(self):
        self.perimetro = (2*self.largo) + (2*self.ancho)
        return self.perimetro

    def calcArea(self):
        self.area = self.largo * self.ancho
        return self.area

class Triangulo(Figuras):
    base = 0
    altura = 0

    def __init__(self,argLados, argBase, argAltura):
        self.nlados = argLados
        self.base = argBase
        self.altura = argAltura

    def calcPerimetro(self):
        self.perimetro = 3*self.base
        return self.perimetro

    def calcArea(self):
        self.area = (self.base * self.altura)/2
        return  self.area

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

    def mostrarDatos(self):
        print('Nombre del estudiante : ' + self.__nombre)
        print('Email del estudiante : ' + self.__email)
        print('Contrasena del estudiante : ' + self.__contrasena)




if __name__ == "__main__":
    rectangulo1 = Rectangulo(4,4,2)
    triangulo1 = Triangulo(3,5,3)

    print("RECTANGULO")
    perimetro = rectangulo1.calcPerimetro()
    print('El perimetro de tu rectangulo es de {} unidades'.format(perimetro))
    area = rectangulo1.calcArea()
    print("El area de tu cuadrado es de {} unidades".format(area))
    rectangulo1.mostrarDatos()
    print("\n\nTRIANGULO")
    perimetro = triangulo1.calcPerimetro()
    print('El perimetro de tu triangulo es de {} unidades'.format(perimetro))
    area = triangulo1.calcArea()
    print("El area de tu cuadrado es de {} unidades".format(area))
    triangulo1.mostrarDatos()

    print('\n\nPrueba de encapsulado\n')
    estudiante1 = Estudiante("Carlos", "carlos@correo.com", "Car123@!et")
    nombre1 = estudiante1.getNombre()
    print('Nombre del estudiante : ' + nombre1)
    email1 = estudiante1.getEmail()
    print('Email del estudiante : ' + email1)
    contra1 = estudiante1.getContra()
    print('Contrasena del estudiante : ' + contra1)


    estudiante1.setNombre('Rodrigo')
    estudiante1.setEmail('Rodigro@correo.net')
    estudiante1.setContra('Contrasena1234')

    estudiante1.mostrarDatos()
