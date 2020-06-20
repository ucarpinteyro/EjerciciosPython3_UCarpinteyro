
import pickle
import shelve

def savePickle(file, x):
    if type(x) == dict:
        archivo = open(file, 'wb')
        pickle.dump(x,archivo)
        archivo.close()
    else:
        print("Se debe guardar un diccionario cuando usa Pickle")

def updatePicke(file, etiqueta, x):
    archivo = open(file, 'rb')
    leido = pickle.load(archivo)
    archivo.close()

    leido[etiqueta] = x

    archivo = open(file, 'wb')
    pickle.dump(leido, archivo)
    archivo.close()

def readPickle(file):
    archivo = open(file, 'rb')
    leido = pickle.load(archivo)
    archivo.close()
    return leido

def saveShelve(file, etiqueta, x):
    with shelve.open(file) as db:
        db[etiqueta] = x

def updateShelve(file, etiqueta, x):
    with shelve.open(file) as db:
        db[etiqueta] = x

def readShelve(file):
    diccionario = {}
    with shelve.open(file) as db:
        for i in db:
            diccionario[i] = db[i]
    return diccionario