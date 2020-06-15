import re
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
# validar correo electronico
#                 valido               valido               no valido por simbolos      no valido dominio          valido
correos = ['iabarcae@yahoo.es','mae_illanes@hotmail.com','Sb.nashxo=+.sk8@hotmail.com','ikis_rojo@hotmail','martacam2002@yahoo.com.mx']
correoRe =  re.compile('([a-zA-Z0-9_.]*[@][a-zA-Z]*[.][a-zA-Z]*.?([a-zA-Z]*)?)')
print('\n\nValidar Correo Electronico\n\n')

for n in correos:
    correoValido = re.match(correoRe, n)

    if correoValido != None:
        print(n+' es un correo VALIDO')
    else:
        print(n + ' es un correo INCORRECTO')


#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
# Validar un numero de telefono
#                 valido            valido         valido         valido           no valido      no valido     no valido
telefonos = ['(72) 2317-3200', '(383)-820-9965', '7222106061', '(922)225 8846', '(55)11-24-9471', '55112494', '(5529)968481']
telefonosRe = re.compile('([0-9]{10})|([(][0-9]{2}[)][ -]?[0-9]{4}[ -]?[0-9]{4})|([(][0-9]{3}[)][ -]?[0-9]{3}[ -]?[0-9]{4})')
print('\n\nValidar Numero Telefonico\n\n')

for n in telefonos:
    telefonoValido = re.match(telefonosRe, n)

    if telefonoValido != None:
        print(n+' es un telefono VALIDO')
    else:
        print(n + ' es un telefono INCORRECTO')


#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
# Validar un RFC
#          valido           incorrecto        valido          incorrecto       valido           incorrecto       valido            incorrecto
rfcs = ['JISG880124915', 'JUH0910902SH3', 'MEID861110UN8', 'QES150112V734', 'PAGL950727HP7', 'PA5G720510MZ5', 'PULA8703242IA', 'QUVA8907042_8']
rfcRe = re.compile('[a-zA-Z]{4}[0-9]{6}[a-zA-Z0-9]{3}')
print('\n\nValidar RFC\n\n')

for n in rfcs:
    rfcValido = re.match(rfcRe, n)

    if rfcValido != None:
        print(n+' es un RFC VALIDO')
    else:
        print(n + ' es un RFC INCORRECTO')


#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
# Validar un CURP
#              valido               valido                 incorrecto            valido               incorrecto              valido             incorrecto           valido               incorrecto
curps = ['AECJ940429HCHRRS01', 'COCA761007MDGRNN02', 'MAPJ77G702HCHRNS08', 'VIRF890629HSLZBR06', 'F8AJ780210HGRLDR09', 'VALC711208MGRZPN02', 'AECM820304XGRCMG01', 'UARJ650317HMCGVS07', 'CUVO770914MGR']
curpRe = re.compile('[a-zA-Z]{4}[0-9]{6}[mMhH][a-zA-Z]{5}[0-9]{2}')
print('\n\nValidar CURP\n\n')

for n in curps:
    curpValido = re.match(curpRe, n)

    if curpValido != None:
        print(n+' es un CURP VALIDO')
    else:
        print(n + ' es un CURP INCORRECTO')
