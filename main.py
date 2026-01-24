import pandas as pd
import matplotlib.pyplot as plt

# REPOSITORIO DE GITHUB: https://github.com/CodeByChriss/Pandas-y-Matplotlib

# Variables Globales
campos = [] # va a contener los campos que el usuario defina para el diccionario con el siguiente formato: NOMBRE_CAMPO:TIPO_CAMPO
diccionarios = [] # array que va a contener los diccionarios

#############################################################################
#
#               APARTADO 1: Crear los campos del diccionario.
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
#               PARTADO 4: Buscar elementos por un campo.
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
#                   APARTADO 5: Calcular estadísticas.
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
#               APARTADO 6: Filtrar elementos según condición.
#
#############################################################################

# Ofrecemos al usuario varias opciones para filtrar dependiendo de si el campo es de tipo String o numérico (Integer o Decimal)
def filtrarElementosCondicion():
    global diccionarios, campos
    if len(campos) == 0:
        print("No se puede calcular ninguna estadística porque no hay campos. Crea un nuevo campo con la opción 1.")
        return
    if len(diccionarios) == 0:
        print("No se puede calcular ninguna estadística porque no hay elementos. Registra un nuevo elemento con la opción 3.")
        return
    
    mostrarCamposEnMenu()
    opt = obtenerOpcion(1, len(campos))
    data = campos[opt-1].split(":")
    nombreCampo = data[0]
    tipoCampo = data[1]
    buscar = input(f"Dime el dato a buscar en el campo \"{nombreCampo}\": ")
    if tipoCampo == "String":
        mostrarFiltrosStringMenu()
        opt = obtenerOpcion(1,2)
    else:
        mostrarFiltrosNumericosMenu()
        opt = obtenerOpcion(1,3)

    mostrarElementosFiltrados(obtenerListaConEntradaQueTenganCampo(diccionarios, nombreCampo), buscar, nombreCampo, tipoCampo, opt)

# Mostramos los filtros que el usuario va a poder usar para el tipo de dato String
def mostrarFiltrosStringMenu():
    print("╔═══════════════ Filtros para Strings ════════════════╗")
    print("╠ 1. Que sea igual.")
    print("╠ 2. Que lo contenga.")
    print("╚═════════════════════════════════════════════════════╝")

# Mostramos los filtros que el usuario va a poder usar para el tipo de dato Integer y Decimal (Float)
def mostrarFiltrosNumericosMenu():
    print("╔═══════════ Filtros para Integer y Decimal ═══════════╗")
    print("╠ 1. Que sea mayor.")
    print("╠ 2. Que sea menos.")
    print("╠ 3. Que sea igual.")
    print("╚══════════════════════════════════════════════════════╝")

# Unicamente vamos a mostrar los elementos que cumplan las condiciones seleccionadas por el usuario
def mostrarElementosFiltrados(lista, buscar, nombreCampo, tipoCampo, tipoFiltro):
    # Primero comprobamos si tipo de campo es numérico y si el dato a buscar es un número
    buscarNum = 0
    if tipoCampo != "String":
        try:
            buscarNum = int(buscar) if tipoCampo == "Integer" else float(buscar)
        except ValueError:
            print("El campo en el que estas intentando filtrar es numérico pero el dato introducido no lo es.")
            return

    cnt = 0
    print("Las entradas que cumplen con el filtro son:")
    for entrada in lista:
        dato = entrada[nombreCampo]
        if tipoCampo == "String":
            if tipoFiltro == 1 and dato == buscar:
                cnt += 1
                print(f"{cnt}. {entrada}")
            elif buscar in dato: # si dato contiene buscar
                cnt += 1
                print(f"{cnt}. {entrada}")
        else:
            if tipoFiltro == 1 and dato > buscarNum:
                cnt += 1
                print(f"{cnt}. {entrada}")
            elif tipoFiltro == 2 and dato < buscarNum:
                cnt += 1
                print(f"{cnt}. {entrada}")
            elif dato == buscarNum:
                cnt += 1
                print(f"{cnt}. {entrada}")

#############################################################################
#
#           APARTADO 7: Generar top N (solo para campos numéricos).
#
#############################################################################

# Generamos y mostramos el top N dependiendo de lo que el usuario elija y nos diga
def generarTopN():
    global diccionarios, campos
    if len(campos) == 0:
        print("No se puede calcular ninguna estadística porque no hay campos. Crea un nuevo campo con la opción 1.")
        return
    if len(diccionarios) == 0:
        print("No se puede calcular ninguna estadística porque no hay elementos. Registra un nuevo elemento con la opción 3.")
        return
    
    correcto, cnt = mostrarCamposNumericosEnMenu()
    if correcto:
        opt = obtenerOpcion(1,cnt)
        data = obtenerCampoNumeroEnCampos(opt).split(":")
        nombreCampo = data[0]
        try:
            n = int(input("Dime la cantidad que quieres que sea el top: "))
            reverse = input(f"Quieres que sea de forma ascendente (el top 1 será el que más tiene del campo \"{nombreCampo}\") [y/n]: ")
        except ValueError:
            print("Debes introducir un número. Operación cancelada.")
            return
        else:
            lista = sorted(obtenerListaConEntradaQueTenganCampo(diccionarios, nombreCampo), key=lambda x: x[nombreCampo], reverse=True if reverse == 'y' or reverse == 'Y' else False)[:n]
            if len(lista) > 0:
                # Mostramos el top N
                print(f"╔═══════════════════════════════════ Top {n} por el campo \"{nombreCampo}\" ═══════════════════════════════════")
                for i, entrada in enumerate(lista):
                    print(f"╠ {i+1}. {entrada}")
                print("╚═══════════════════════════════════════════════════════════════════════════════════════════════════")
            else:
                print(f"No existen registros con el campo \"{nombreCampo}\"")
    else:
        print("No existen campos numéricos. Puedes agregar uno nuevo con la opción 1.")

############################################################################################################################
#
#                   APARTADO 8: Añadir columnas nuevas con estadísticas o cálculos sobre los datos.
#
############################################################################################################################

#############################################################################
#
#               APARTADO 9: Aplicar filtros y agrupaciones.
#
#############################################################################

#############################################################################
#
#               APARTADO 10: Generar 3 tipos de gráficos.
#
#############################################################################

#############################################################################
#
#               APARTADO 11: Exportar los resultados.
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
    print("╠ 6. Filtrar elementos según condición.")
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

# Mostramos unicamente los campos numéricos que hay en el menú
def mostrarCamposNumericosEnMenu():
    cnt = 0
    print("╔═══════════════════════════════════ Campos Numéricos Actuales ═══════════════════════════════════╗")
    for campo in campos:
        data = campo.split(":")
        tipoCampo = data[1]
        if tipoCampo != "String":
            nombreCampo = data[0]
            cnt += 1
            print(f"╠ {cnt}. \"{nombreCampo}\" de tipo {tipoCampo}")
    print("╚═══════════════════════════════════════════════════════════════════════════════════════╝")

    return (True if cnt > 0 else False,cnt) # si no hay campos numéricos devuelvo un False para que no se siga con el proceso

# En la función generarTopN() de la opción 7 unicamente queremos los campos numéricos por lo que debemos recorrer campos[] en busca del campo numérico que se corresponda con el número que se ha mostrado en mostrarCamposNumericosEnMenu()
def obtenerCampoNumeroEnCampos(index):
    global campos
    cnt = 0
    for campo in campos:
        data = campo.split(":")
        tipoCampo = data[1]
        if tipoCampo != "String":
            cnt += 1
            if cnt == index:
                return campo
    return "ERROR:ERROR"

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
            case 6: filtrarElementosCondicion()
            case 7: generarTopN()
            case 8: print("opcion 9")
            case 9: print("opcion 10")
            case 10: print("opcion 11")
            case 11: print("opcion 12")
            case 12 : print("¡Hasta pronto!")

    print("Programa finalizado.")

if __name__ == '__main__':
    init()