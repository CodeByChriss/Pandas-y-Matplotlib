import pandas as pd
import matplotlib.pyplot as plt

# REPOSITORIO DE GITHUB: https://github.com/CodeByChriss/Pandas-y-Matplotlib

# Variables Globales
campos = [] # va a contener los campos que el usuario defina para el diccionario con el siguiente formato: NOMBRE_CAMPO:TIPO_CAMPO
diccionarios = [] # array que va a contener los diccionarios

#############################################################################
#
#           APARTADO 1: Crear los campos del diccionario.
#
#############################################################################

# Mostramos al usuario un pequeño menú para que vaya agregando y visualizando los campos actuales del diccionario.
def initCrearCamposDiccionario():
    opt = 0
    while opt != 3:
        mostrarMenuCrearCamposDiccionario()
        opt = obtenerOpcion(1,3)
        match opt:
            case 1: agregarCampoDiccionario()
            case 2: mostrarCamposDiccionario()
            case 3: return

# Agregamos los campos que el usuario diga a la variable global campos[]
def agregarCampoDiccionario():
    global campos
    nombreNuevoCampo = input("Dime el nombre del nuevo campo: ")
    tipoNuevoCampo = recogerOpcionCampos()
    nuevoCampo = f"{nombreNuevoCampo}:{tipoNuevoCampo}"
    campos.append(nuevoCampo)
    print("Campo registrado con éxito.")

# Solicitamos al usuario un tipo de dato y lo devolvemos, en caso de error (no se cuando podría pasar porque creo que he contemplado todo) se devuelve un String
def recogerOpcionCampos():
    mostrarOpcionesCampos()
    opt = obtenerOpcion(1,3)
    match opt:
        case 1: return "String"
        case 2: return "Integer"
        case 3: return "Decimal"
        case _: return "String"
    
# Muestra las opciones de tipos de datos que permito usar
def mostrarOpcionesCampos():
    print("╔═════════════════════════ Opciones tipos de datos ═════════════════════════╗")
    print("╠ 1. String.")
    print("╠ 2. Integer.")
    print("╠ 3. Decimal (float).")
    print("╚═══════════════════════════════════════════════════════════════════════════╝")

# Mostramos todos los campos que haya en la variable global campos[]
def mostrarCamposDiccionario():
    global campos
    if len(campos) > 0:
        print("Los campos actualmente registrados son:")
        for i, campo in enumerate(campos):
            data = campo.split(":")
            nombreCampo = data[0]
            tipoCampo = data[1]
            print(f"{i+1}. \"{nombreCampo}\" y es de tipo {tipoCampo}")
    else:
        print("No hay campos registrados.")

# Muestra por terminal el Menú de Crear Campos para el Diccionario
def mostrarMenuCrearCamposDiccionario():
    print("╔═════════════════ Menú Crear Campos Diccionario ═════════════════╗")
    print("╠ 1. Agregar campo.")
    print("╠ 2. Mostrar campos registrados.")
    print("╠ 3. Volver al menú princpal.")
    print("╚═════════════════════════════════════════════════════════════════╝")

#############################################################################
#
#           APARTADO 2: Mostrar los datos del diccionario.
#
#############################################################################

# Mostramos los registros que haya en nuestro diccionario
def mostrarDatosDiccionario():
    global diccionarios, campos
    if len(diccionarios) > 0:
        for diccionario in diccionarios:
            print(diccionario)
    else:
        msg = " Usa la opción número 1 para agregar campos nuevos."
        if len(campos) > 0:
            msg = " Usa la opción número 3 para agregar nuevos elementos al diccionario."
        print(f"Actualmente el diccionario está vacío.{msg}")

#############################################################################
#
#           APARTADO 3: Añadir un nuevo elemento al diccionario.
#
#############################################################################

# Solicitamos datos para cada campo que el usuario ha registrado
def aniadirElementoDiccionario():
    global diccionarios, campos
    if len(campos) == 0:
        print("Antes de agregar elementos, debes agregar campos nuevos.")
        return
    
    nuevo = {}
    for campo in campos:
        data = campo.split(":")
        nombreCampo = data[0]
        tipoCampo = data[1]
        introducido = input(f"Introduce los datos para el campo \"{nombreCampo}\": ")
        try:
            match tipoCampo:
                case "Integer": introducido = int(introducido)
                case "Decimal": introducido = float(introducido)
        except ValueError:
            print(f"Error en la conversión a {tipoCampo}, este elemento no ha sido agregado.")
            return
        else:
            nuevo[nombreCampo] = introducido
    diccionarios.append(nuevo)
    print("Elemento agreado con éxito!")

#############################################################################
#
#           APARTADO 4: Buscar elementos por un campo.
#
#############################################################################

# Buscamos elementos por un campo, la idea es mostrar al usuario un menú con los campos que puede elegir y buscar según el campo elegido
def buscarElementosPorUnCampo():
    global campos
    if len(campos) == 0:
        print("No se puede buscar elementos por un campo porque no hay campos. Crea un nuevo campo con la opción 1.")
        return
    
    mostrarCamposEnMenu()
    opt = obtenerOpcion(1,len(campos))
    data = campos[opt-1].split(":")
    nombreCampo = data[0]
    buscar = input("Introduce el contenido a buscar: ")
    mostrarElementoEncontrado(buscar, nombreCampo)

# Mostramos unicamente el diccionario en el que su nombreCampo (en caso de contenerlo) sea igual a buscar
def mostrarElementoEncontrado(buscar, nombreCampo):
    global diccionarios
    print(f"Los diccionarios que son igual a \"{buscar}\" en su campo \"{nombreCampo}\" son:")
    cnt = 0
    for diccionario in diccionarios:
        try:
            if str(diccionario[nombreCampo]) == buscar:
                print(diccionario)
                cnt+=1
        except KeyError: # Debemos usar el except porque existe la posibilidad de que el usuario haya agregado un campo nuevo después de hacer algún registro
            continue

#############################################################################
#
#           APARTADO 5: Calcular estadísticas.
#
#############################################################################

# Calculamos estadísticas de un campo
def calcularEstadisticas():
    global diccionarios, campos
    if len(campos) == 0:
        print("No se puede calcular ninguna estadística porque no hay campos. Crea un nuevo campo con la opción 1.")
        return
    if len(diccionarios) == 0:
        print("No se puede calcular ninguna estadística porque no hay elementos. Registra un nuevo elemento con la opción 3.")
        return

    mostrarMenuEstadisticas()
    opt = obtenerOpcion(1,4)
    mostrarCamposDiccionario()
    optCampo = obtenerOpcion(1,len(campos))
    data = campos[optCampo-1].split(":")
    nombreCampo = data[0]
    tipoCampo = data[1]
    match opt:
        case 1: # Media
            if tipoCampo != "Integer" and tipoCampo != "Decimal":
                print("No se puede hacer la media de un campo que no es numérico.")
                return
            else:
                obtenerMedia(nombreCampo)
        case 2: # Máximo
            if tipoCampo != "Integer" and tipoCampo != "Decimal":
                print("No se puede obtener el máximo de un campo que no es numérico.")
                return
            else:
                obtenerMaximo(nombreCampo)
        case 3: # Mínimo
            if tipoCampo != "Integer" and tipoCampo != "Decimal":
                print("No se puede obtener el mínimo de un campo que no es numérico.")
                return
            else:
                obtenerMinimo(nombreCampo)
        case 4: # Recuento
            buscar = input("Introduce el dato a buscar: ")
            obtenerRecuento(nombreCampo,buscar)

def obtenerMedia(nombreCampo):
    global diccionarios
    diccionariosLimpios = obtenerListaConEntradaQueTenganCampo(diccionarios, nombreCampo)
    cntTotal = 0
    cnt = 0
    for diccionario in diccionariosLimpios:
        cnt+=1
        cntTotal += diccionario[nombreCampo]
    print(f"La media del campo \"{nombreCampo}\" es de: {cntTotal/cnt}")

def obtenerMaximo(nombreCampo):
    global diccionarios
    diccionario = max(obtenerListaConEntradaQueTenganCampo(diccionarios, nombreCampo), key=lambda x: x[nombreCampo])
    print(f"El diccionario con el campo \"{nombreCampo}\" que es el máximo es: {diccionario}")

def obtenerMinimo(nombreCampo):
    global diccionarios
    diccionario = min(obtenerListaConEntradaQueTenganCampo(diccionarios, nombreCampo), key=lambda x: x[nombreCampo])
    print(f"El diccionario con el campo \"{nombreCampo}\" que es el mínimo es: {diccionario}")

# Mostramos la cantidad de diccionarios que en su campo <nombreCampo> tienen el valor <buscar>
def obtenerRecuento(nombreCampo,buscar):
    global diccionarios
    cnt = 0
    for diccionario in diccionarios:
        try:
            if str(diccionario[nombreCampo]) == buscar:
                cnt+=1
        except KeyError: # Debemos usar el except porque existe la posibilidad de que el usuario haya agregado un campo nuevo después de hacer algún registro
            continue
    print(f"La cantidad de diccionarios que en su campo \"{nombreCampo}\" es igual a \"{buscar}\" es de: {cnt}")

# Mostramos las opciones que se le dan al usuario para calcular las estadísticas
def mostrarMenuEstadisticas():
    print("╔═════════════════ Menú Estadísticas ═════════════════╗")
    print("╠ 1. Media.")
    print("╠ 2. Máximo.")
    print("╠ 3. Mínimo.")
    print("╠ 4. Recuento.")
    print("╚═════════════════════════════════════════════════════╝")

#############################################################################
#
#           APARTADO 6: Filtrar elementos por campo.
#
#############################################################################

#############################################################################
#
#           APARTADO 7: Generar top N (solo para campos numéricos).
#
#############################################################################

#############################################################################
#
#           APARTADO 8: Añadir columnas nuevas con estadísticas o cálculos sobre los datos.
#
#############################################################################

#############################################################################
#
#           APARTADO 9: Aplicar filtros y agrupaciones.
#
#############################################################################

#############################################################################
#
#           APARTADO 10: Generar 3 tipos de gráficos.
#
#############################################################################

#############################################################################
#
#           APARTADO 11: Exportar los resultados.
#
#############################################################################

#############################################################################
#
#                           Funciones Principales
#
#############################################################################

# Como existe la posibilidad de que el usuario haya creado nuevos campos después de registrar algún elemento necesito filtrar las entradas que tengan ese campo
def obtenerListaConEntradaQueTenganCampo(listaOriginal, nombreCampo):
    listaCorrecta = []
    excluidos = 0
    for entrada in listaOriginal:
        try:
            data = entrada[nombreCampo]
        except KeyError:
            excluidos+=1
            continue
        else:
            listaCorrecta.append(entrada)
    print(f"Se han excluido un total de {excluidos} diccionarios por no tener el campo deseado.")
    return listaCorrecta

# Muestra por terminal el Menú Principal de la aplicación
def mostrarMenuPrincipal():
    print("╔═══════════════════════════════════ Menú Principal ═══════════════════════════════════╗")
    print("╠ 1. Crear y ver los campos del diccionario.")
    print("╠ 2. Mostrar los datos del diccionario.")
    print("╠ 3. Añadir un nuevo elemento al diccionario.")
    print("╠ 4. Buscar elementos por un campo.")
    print("╠ 5. Calcular estadísticas.")
    print("╠ 6. Filtrar elementos por campo.")
    print("╠ 7. Generar top N (solo para campos numéricos).")
    print("╠ 8. Añadir columnas nuevas con estadísticas o cálculos sobre los datos.")
    print("╠ 9. Aplicar filtros y agrupaciones.")
    print("╠ 10. Generar 3 tipos de gráficos.")
    print("╠ 11. Exportar los resultados.")
    print("╠ 12. Salir de la aplicación.")
    print("╚══════════════════════════════════════════════════════════════════════════════════════╝")

# Aquí no compruebo si hay elementos o no en el Array ya que lo compruebo justo antes de llamarlo
# Lo que hace es mostrar en forma de menú los campos que hay y su tipo de dato
def mostrarCamposEnMenu(): 
    print("╔═══════════════════════════════════ Campos Actuales ═══════════════════════════════════╗")
    for i, campo in enumerate(campos):
        data = campo.split(":")
        nombreCampo = data[0]
        tipoCampo = data[1]
        print(f"╠ {i+1}. \"{nombreCampo}\" de tipo {tipoCampo}")
    print("╚═══════════════════════════════════════════════════════════════════════════════════════╝")

# Obtenemos la opción elegida por el usuario siempre y cuando esté entre el mínimo y el máximo
def obtenerOpcion(min,max):
    opt = min-1
    msg = ""
    while opt < min or opt > max:
        try:
            opt = int(input(f"{msg}Seleccione una opción: "))
        except ValueError:
            msg = "Debes introducir un número. "
            opt = min-1
        else:
            if opt < min or opt > max:
                msg = "Esa opción no existe. "
            else:
                return opt

# Método principal que llama a mostrar el menú y recoge la respuesta
def init():
    opt = 0
    while opt != 12: # Mientras que la opción elegida por el usuario sea distinta a la opción de salir
        mostrarMenuPrincipal()
        opt = obtenerOpcion(1,12)
        match opt:
            case 1: initCrearCamposDiccionario()
            case 2: mostrarDatosDiccionario()
            case 3: aniadirElementoDiccionario()
            case 4: buscarElementosPorUnCampo()
            case 5: calcularEstadisticas()
            case 6: print("opcion 6")
            case 7: print("opcion 7")
            case 8: print("opcion 9")
            case 9: print("opcion 10")
            case 10: print("opcion 11")
            case 11: print("opcion 12")
            case 12 : print("¡Hasta pronto!")

    print("Programa finalizado.")

if __name__ == '__main__':
    init()