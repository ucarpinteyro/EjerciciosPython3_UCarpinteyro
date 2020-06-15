
def func_sortman(lista):
    # Se verifica que la lista sea unicamente de numeros enteros o flotantes
    listaValida = True
    for elemento in lista:
        listaValida = False if (type(elemento) != int) and (type(elemento) != float) else listaValida
    # Si la lista es valida, se realiza el ordenamiento
    if listaValida:
        listaaux = lista[:]
        listanew = []
        while listaaux != []:
            auxInd = 0
            auxElem = listaaux[0]
            # Se busca el elemento mas pequeno de la lista
            for ind, elem in enumerate(listaaux):
                if elem < auxElem:
                    auxElem = elem
                    auxInd = ind
            listanew.append(auxElem)
            listaaux.pop(auxInd)
        print("Lista original:")
        print(lista)
        print("Lista ordenada:")
        print(listanew)
    else:
        print("La lista no se puede ordenar.")


# Se ingresa una lista
agregar = 'y'
lista = []
conta = 0
while agregar == 'y':
    lista.append(int(input("\nIngresa un numero a la lista : ")))
    print("\nAgregar otro numero?  y -> Si  n -> No \n")
    agregar = input()
    conta += 1
func_sortman(lista)