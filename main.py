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
    opt = obtenerOpcion(1,4)
    match opt:
        case 1: return "String"
        case 2: return "Integer"
        case 3: return "Decimal"
        case 4: return "Boolean"
        case _: return "String"
    
# Muestra las opciones de tipos de datos que permito usar
def mostrarOpcionesCampos():
    print("╔═════════════════════════ Opciones tipos de datos ═════════════════════════╗")
    print("╠ 1. String.")
    print("╠ 2. Integer.")
    print("╠ 3. Decimal (float).")
    print("╠ 4. Boolean.")
    print("╚═══════════════════════════════════════════════════════════════════════════╝")

# Mostramos todos los campos que haya en la variable global campos[]
def mostrarCamposDiccionario():
    global campos
    if len(campos) > 0:
        print("Los campos actualmente registrados son:")
        for i, campo in enumerate(campos):
            data = campo.split(":")
            try: # Hay que hacerlo dentro de un try porque existe la posibilidad de que el usuario haya puesto "" al nombre
                nombreCampo = data[0]
                tipoCampo = data[1]
            except IndexError:
                print("Error en mostrarCampoDiccionario")
            else:
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
        try: # Hay que hacerlo dentro de un try porque existe la posibilidad de que el usuario haya puesto "" (nada) al nombre
            nombreCampo = data[0]
            tipoCampo = data[1]
        except IndexError:
            print("Error en aniadirElementoDiccionario")
        else:
            introducido = input(f"Introduce los datos para el campo \"{nombreCampo}\": ")
            try:
                match tipoCampo:
                    case "Integer": introducido = int(introducido)
                    case "Boolean": introducido = bool(introducido) # bool == Boolean
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
#                           Funciones Principales
#
#############################################################################

# Muestra por terminal el Menú Principal de la aplicación
def mostrarMenuPrincipal():
    print("╔═══════════════════════════════════ Menú Principal ═══════════════════════════════════╗")
    print("╠ 1. Crear los campos del diccionario.")
    print("╠ 2. Mostrar los datos del diccionario.")
    print("╠ 3. Añadir un nuevo elemento al diccionario.")
    print("╠ 4. Buscar elementos por un campo.")
    print("╠ 5. Calcular estadísticas.")
    print("╠ 6. Filtrar elementos por campo.")
    print("╠ 7. Generar top N (solo para campos numéricos).")
    print("╠ 8. Buscar elementos por un campo.")
    print("╠ 9. Añadir columnas nuevas con estadísticas o cálculos sobre los datos.")
    print("╠ 10. Aplicar filtros y agrupaciones.")
    print("╠ 11. Generar 3 tipos de gráficos..")
    print("╠ 12. Exportar los resultados.")
    print("╠ 13. Salir de la aplicación.")
    print("╚══════════════════════════════════════════════════════════════════════════════════════╝")

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
    while opt != 13: # Mientras que la opción elegida por el usuario sea distinta a la opción de salir
        mostrarMenuPrincipal()
        opt = obtenerOpcion(1,13)
        match opt:
            case 1: initCrearCamposDiccionario()
            case 2: mostrarDatosDiccionario()
            case 3: aniadirElementoDiccionario()
            case 4: print("opcion 4")
            case 5: print("opcion 5")
            case 6: print("opcion 6")
            case 7: print("opcion 7")
            case 8: print("opcion 8")
            case 9: print("opcion 9")
            case 10: print("opcion 10")
            case 11: print("opcion 11")
            case 12: print("opcion 12")
            case 13 : print("¡Hasta pronto!")

    print("Programa finalizado.")

if __name__ == '__main__':
    init()