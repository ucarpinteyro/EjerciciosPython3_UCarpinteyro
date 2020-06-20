
import StudentIO

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

filePickle = 'Tarea3_pickle.db'

Estudiante1 = Estudiante('ABARCA INGRID', 'iabarcae@yahoo.es', 'ABARCA')
Estudiante2 = Estudiante('BANTO MARCELO', 'mfbanto@gmail.com', 'BANTO')
Estudiante3 = Estudiante('CAMPOS GERMAN', 'campos.onfray@gmail.com', 'CAMPOS')
Estudiante4 = Estudiante('DIAZ CAROLINA', 'Karito_1404@hotmail.com', 'DIAZ')
Estudiante5 = Estudiante('KATALINIC VERONICA', 'verocakatalinic@hotmail.com', 'KATALINIC')
Estudiante6 = Estudiante('MORALES SUSANA', 'susa.mora@gmail.com', 'MORALES')
Estudiante7 = Estudiante('ROBERTSON MARTIN', 'tin.robertson@gmail.com', 'ROBERTSON')

# Se crea un diccionario con los objetos generados anteriormente para usarlos con pickle
dict_Estudiantes = {"Estudiante1": Estudiante1,
                    "Estudiante2": Estudiante2,
                    "Estudiante3": Estudiante3,
                    "Estudiante4": Estudiante4,
                    "Estudiante5": Estudiante5}

StudentIO.savePickle(filePickle,dict_Estudiantes)
leido = StudentIO.readPickle(filePickle)

#Se muestra lo leido con pickle
print("\nSe realiza lectura con pickle\n")
for i in leido.keys():
    print("nombre=>"+leido[i].getNombre()+"  "+
          "email=>"+leido[i].getEmail()+"  "+
          "contrasena=>"+leido[i].getContra())

#Se sustituyen los datos de estudiante 1 y se agrega un registro
StudentIO.updatePicke(filePickle,"Estudiante6", Estudiante6)
StudentIO.updatePicke(filePickle,"Estudiante1", Estudiante7)
leido = StudentIO.readPickle(filePickle)

#Se muestra lo leido con pickle
print("\nSe realiza lectura con modificaciones pickle\n")
for i in leido.keys():
    print("nombre=>"+leido[i].getNombre()+"  "+
          "email=>"+leido[i].getEmail()+"  "+
          "contrasena=>"+leido[i].getContra())


#Guardado de datos con Shelve
fileShelve = 'Tarea3_shelve'
StudentIO.saveShelve(fileShelve,'Estudiante1', Estudiante1)
StudentIO.saveShelve(fileShelve,'Estudiante2', Estudiante2)
StudentIO.saveShelve(fileShelve,'Estudiante3', Estudiante3)
StudentIO.saveShelve(fileShelve,'Estudiante4', Estudiante4)
StudentIO.saveShelve(fileShelve,'Estudiante5', Estudiante5)

leidoS = StudentIO.readShelve(fileShelve)
print(leidoS)
print(type(leidoS))

print("\nSe realiza lectura con Shelve\n")
for i in leidoS.keys():
    print("nombre=>"+leidoS[i].getNombre()+"  "+
          "email=>"+leidoS[i].getEmail()+"  "+
          "contrasena=>"+leidoS[i].getContra())

#Se sustituyen los datos de estudiante 4 y se agrega un registro
StudentIO.updateShelve(fileShelve,"Estudiante6", Estudiante6)
StudentIO.updateShelve(fileShelve,"Estudiante4", Estudiante7)
leidoS = StudentIO.readShelve(fileShelve)
print("\nSe realiza lectura con modificaciones shelve\n")
for i in leidoS.keys():
    print("nombre=>"+leidoS[i].getNombre()+"  "+
          "email=>"+leidoS[i].getEmail()+"  "+
          "contrasena=>"+leidoS[i].getContra())
