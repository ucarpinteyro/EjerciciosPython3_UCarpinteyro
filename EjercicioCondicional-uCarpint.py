# Scrip de ejercicios sobre condicionales, Clase 2 de python PADTS
# El script contiene la funcion validaciones(num) que tiene como parameto un
# numero al cual se le aplican todas las validaciones solicitadas.
# Tambien se agrega la funcion sortman(lista) que realiza el mismo proceso
# que realizaria la funcion SORT de una lista de python.

def func_validaciones(num):
    # Checar si el numero es positivo, negativo o cero.
    if num > 0:
        print(str(num) + " es positivo.")
    elif num < 0:
        print(str(num) + " es negativo.")
    else:
        print(str(num) + " es cero.")

    # Validar si un numero es par o impar.
    if num != 0:
        print(str(num) + " es par.") if (num % 2) == 0 else print(str(num) + " es impar.")
    else:
        print("El cero no esta definido como par o impar")

    # Validar si es primo.
    if num > 0:
        primo = True
        for i in range(2,num):
            primo = False if (num%(i))==0 else primo

        if primo:
            print(str(num) + " es primo.")
        else:
            print(str(num) + " no es primo.")
    else:
        print("Los numeros primos solo estan definidos para enteros positivos")

    # Valida si un anio es bisiesto
    if num > 0:
        bisiesto = False
        if (num%4) == 0:
            if (num%100) == 0:
                if (num%400) == 0:
                    bisiesto = True
            else:
                bisiesto = True
        print("el anio "+str(num) + " es bisiesto.") if bisiesto else print("el anio "+str(num) + " no es bisiesto.")
    else:
        print("los anios solo pueden ser numeros positivos")


# Se pide un numero y se manda llama la funcion validaciones
num = int(input("Ingrese un Numero Entero: "))
func_validaciones(num)


