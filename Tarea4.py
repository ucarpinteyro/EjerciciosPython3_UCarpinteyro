from mongoengine import *

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
            print('El registro ya existe, si desea actualizarlo use "updateMongo()"')
            return

    estudiante_db.save()
    return

def updateMongo(nombre,email,contrasena):
    datos = estudiantes.objects
    for e in datos:
        if e.nombre == nombre:
            e.modify(nombre = nombre,
                     email = email,
                     contrasena= contrasena)
    return e

def readMongo(nombre):
    datos = estudiantes.objects
    for e in datos:
        if e.nombre == nombre:
            return e

def deleteMongo(nombre):
    datos = estudiantes.objects
    for e in datos:
        if e.nombre == nombre:
            e.delete()
    return estudiantes.objects

if __name__ == '__main__':
    connect('padts')

    datos = [('ABARCA INGRID', 'iabarcae@yahoo.es', 'ABARCA'),
         ('BANTO MARCELO', 'mfbanto@gmail.com', 'BANTO'),
         ('CAMPOS GERMAN', 'campos.onfray@gmail.com', 'CAMPOS'),
         ('DIAZ CAROLINA', 'Karito_1404@hotmail.com', 'DIAZ'),
         ('KATALINIC VERONICA', 'verocakatalinic@hotmail.com', 'KATALINIC'),
         ('MORALES SUSANA', 'susa.mora@gmail.com', 'MORALES'),
         ('ROBERTSON MARTIN', 'tin.robertson@gmail.com', 'ROBERTSON'),
         ]

    # Guardado de los estudiantes
    for nom, email, contra in datos:
        saveMongo(nom,email,contra)

    # Eliminamos el registro el primer y el ultimo registro
    deleteMongo('ABARCA INGRID')
    restantes = deleteMongo('ROBERTSON MARTIN')

    for index, p in enumerate(restantes):
        print(f'{index + 1} - Nombre: {p.nombre}\nLugar: {p.email}\nFecha: {p.contrasena}\n ')

    # Se cambia actualiza la informacion para el segundo y tercer elemento
    updateMongo('BANTO MARCELO', 'nuevo@correo.com', 'NUEVA')
    updateMongo('CAMPOS GERMAN', 'Sin Email', 'None')

    # Leemos la informacion actualizada del segundo y tercer elemento desde la base de datos
    leido = readMongo('BANTO MARCELO')
    print(f'\nNombre: {leido.nombre}\nLugar: {leido.email}\nFecha: {leido.contrasena}\n ')
    leido = readMongo('CAMPOS GERMAN')
    print(f'\nNombre: {leido.nombre}\nLugar: {leido.email}\nFecha: {leido.contrasena}\n ')