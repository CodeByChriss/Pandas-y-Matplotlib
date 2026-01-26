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
        print(f"Actualmente hay un total de {len(diccionarios)} elementos.")
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
        print("No se puede filtrar porque no hay campos. Crea un nuevo campo con la opción 1.")
        return
    if len(diccionarios) == 0:
        print("No se puede filtrar porque no hay elementos. Registra un nuevo elemento con la opción 3.")
        return
    
    mostrarCamposEnMenu()
    opt = obtenerOpcion(1, len(campos))
    data = campos[opt-1].split(":")
    nombreCampo = data[0]
    tipoCampo = data[1]
    buscar = input(f"Dime el dato a buscar en el campo \"{nombreCampo}\": ")
    if tipoCampo == "String":
        mostrarFiltrosStringMenu()
        opt = obtenerOpcion(1,4)
    else:
        mostrarFiltrosNumericosMenu()
        opt = obtenerOpcion(1,3)

    mostrarElementosFiltrados(obtenerListaConEntradaQueTenganCampo(diccionarios, nombreCampo), buscar, nombreCampo, tipoCampo, opt)

# Mostramos los filtros que el usuario va a poder usar para el tipo de dato String
def mostrarFiltrosStringMenu():
    print("╔═══════════════ Filtros para Strings ════════════════╗")
    print("╠ 1. Que sea igual.")
    print("╠ 2. Que lo contenga.")
    print("╠ 3. Que sea diferente.")
    print("╠ 4. Que no lo contenga.")
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
            if tipoFiltro == 1 and dato == buscar: # si dato es igual a buscar
                cnt += 1
                print(f"{cnt}. {entrada}")
            elif tipoFiltro == 2 and buscar in dato: # si dato contiene buscar
                cnt += 1
                print(f"{cnt}. {entrada}")
            elif tipoFiltro == 3 and buscar != dato: # si dato es diferente a buscar
                cnt += 1
                print(f"{cnt}. {entrada}")
            elif not buscar in dato: # si dato no contiene buscar
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
        print("No se puede generar el top N porque no hay campos. Crea un nuevo campo con la opción 1.")
        return
    if len(diccionarios) == 0:
        print("No se puede generar el top N porque no hay elementos. Registra un nuevo elemento con la opción 3.")
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

#############################################################################
#
#               APARTADO 8: Cargar archivo XLSX o CSV.
#
#############################################################################

# Le mostramos al usuario un menú en el que están las opciones de ficheros que ofrecemos, preguntamos por el nombre del archivo y leemos el fichero
def cargarArchivo():
    global diccionarios, campos
    mostrarMenuTiposArchivos()
    opt = obtenerOpcion(1,2)
    nombreArchivo = input("Introduce el nombre del archivo (sin la extensión): ")
    try:
        if opt == 1:
            df = pd.read_excel(f"{nombreArchivo}.xlsx")
        else:
            df = pd.read_csv(f"{nombreArchivo}.csv")
    except FileNotFoundError:
        print("No se ha podido encontrar el fichero, puede ser que no se llame como has indicado. Operación cancelada.")
        return
    else:
        # Agregamos los campos del fichero a campos[] para que el usuario pueda modificarlos y verlos luego
        primeraFila = df.iloc[0]
        agregados = 0
        for campo in df:
            agregados+=1
            tipoDeDato = str(type(primeraFila[campo]))
            if "int" in tipoDeDato: # Si "int" o "float" o "str" esta en <class 'numpy.int64'> o <class 'numpy.float64'> o <class 'str'>
                campos.append(f"{campo}:Integer")
            elif "float" in tipoDeDato:
                campos.append(f"{campo}:Decimal")
            else:
                campos.append(f"{campo}:String")
        print(f"Se han agregado un total de {agregados} campos.")
        # Agregamos todas las filas (el contenido del fichero) a diccionarios
        agregados = 0
        for i, row in df.iterrows(): # recorremos cada fila del fichero
            nuevoDiccionario = {}
            for campo in df: # recorremos cada campo que hay en el fichero por cada fila del mismo
                nuevoDiccionario[campo] = row[campo]
            diccionarios.append(nuevoDiccionario)
            agregados+=1
        print(f"Se han agregado un total de {agregados} elementos al diccionario.")

# Muestra en forma de menú las opciones de ficheros que el usuario tiene para elegir
def mostrarMenuTiposArchivos():
    print("╔══════════ Tipos de archivos disponibles ═════════╗")
    print("╠ 1. .xlsx")
    print("╠ 2. .csv")
    print("╚══════════════════════════════════════════════════╝")

############################################################################################################################
#
#                   APARTADO 9: Añadir columnas nuevas con estadísticas o cálculos sobre los datos.
#
############################################################################################################################

# Recogemos algunos datos que introduzca el usuario y con eso calculamos y agregamos la columna necesaria
def aniadirEstadisticaOCalculo():
    # Primero comprobamos que haya contenido
    global diccionarios, campos
    if len(campos) == 0:
        print("No se puede realizar estadísticas o cálculos porque no hay campos. Crea un nuevo campo con la opción 1.")
        return
    if len(diccionarios) == 0:
        print("No se puede realizar estadísticas o cálculos porque no hay elementos. Registra un nuevo elemento con la opción 3.")
        return
    
    mostrarMenuEstadisticasCalculos()
    opt = obtenerOpcion(1,5)
    # Aprovechamos la libreria pandas para no tener que recorrer fila por fila haciendo el calculo
    df = pd.DataFrame(diccionarios) # Convertimos nuestra lista de diccionarios a DataFrame
    try:
        match opt:
            case 1: # Contribución de gol (Goals scored + Assists)
                df["Contribucion de gol"] = df["Goals scored"] + df["Assists"]
            case 2: # Efectividad (%) (Goals scored / Shots on target)
                df["Efectividad"] = round(df["Goals scored"] / df["Shots on target"] * 100)
            case 3: # Puntería (%) (Goals scored / Shots on target * 100)
                df["Punteria"] = round(df["Goals scored"] / df["Shots on target"] * 100)
            case 4: # Cantidad de tarjetas recibidas (Yellow Cards + Red Cards)
                df["Cantidad de tarjetas recibidas"] = df["Yellow Cards"] + df["Red Cards"]
            case 5: # Media goles por partido (Goals scored / Games played)
                df["Media goles por partido"] = df["Goals scored"] / df["Games played"]
    except KeyError: # Si no se ha cargado antes del fichero va a dar error.
        print("Ha ocurrido un error, asegúrate de haber cargar antes el fichero y que cumpla con los nombres de los campos. Operación cancelada.")
        return
    else:
        diccionarios = df.to_dict() # Lo pasamos de nuevo al array de diccionarios
        print("Operación realizada con éxito.")

# Mostramos los cálculos que le ofrecemos al usuario
def mostrarMenuEstadisticasCalculos():
    print("╔═════════════════════════ Tipos de estadísticas y cálculos ════════════════════════╗")
    print("╠ 1. Contribución de gol (Goals scored + Assists).")
    print("╠ 2. Efectividad (%) (Goals scored / Shots on target).")
    print("╠ 3. Puntería (%) (Goals scored / Shots on target * 100).")
    print("╠ 4. Cantidad de tarjetas recibidas (Yellow Cards + Red Cards).")
    print("╠ 5. Media goles por partido (Goals scored / Games played).")
    print("╚═══════════════════════════════════════════════════════════════════════════════════╝")

#############################################################################
#
#               APARTADO 10: Aplicar filtros y agrupaciones.
#
#############################################################################

def filtrosAgrupaciones():
    # Primero comprobamos que haya contenido
    global diccionarios, campos
    if len(campos) == 0:
        print("No se puede realizar estadísticas o cálculos porque no hay campos. Crea un nuevo campo con la opción 1.")
        return
    if len(diccionarios) == 0:
        print("No se puede realizar estadísticas o cálculos porque no hay elementos. Registra un nuevo elemento con la opción 3.")
        return
    
    # Preguntamos si quiere filtrar o agrupar
    mostrarMenuFiltrarAgrupar()
    opt = obtenerOpcion(1,2)
    
    if opt == 1: # Si quiere filtrar
        mostrarCamposEnMenu()
        optCampo = obtenerOpcion(1,len(campos))
        data = campos[optCampo-1].split(":")
        nombreCampo = data[0]
        tipoCampo = data[1]
        palabra = input("Dime la palabra/palabras/número/números por los que quieres filtrar: ")
        try:
            if tipoCampo == "Integer":
                palabra = int(palabra)
            elif tipoCampo == "Decimal":
                palabra = float(palabra)
        except ValueError:
            print(f"No puedes filtrar el campo \"{nombreCampo}\" que es de tipo {tipoCampo} por un tipo distinto. Operación cancelada.")
            return
        else:
            df = pd.DataFrame(diccionarios) # Aprovechamos la librería Pandas para no tener que estar nosotros comprobando linea por linea
            if tipoCampo == "String":
                mostrarFiltrosStringMenu()
                optFiltro = obtenerOpcion(1,4)
                if optFiltro == 1: # El usuario quiere filtrar si es igual
                    listaFiltrada = df[df[nombreCampo] == palabra]
                    mostrarDataFrame(listaFiltrada)
                elif optFiltro == 2: # El usuario quiere filtrar si lo contiene
                    listaFiltrada = df[palabra in df[nombreCampo]]
                    mostrarDataFrame(listaFiltrada)
                elif optFiltro == 3: # El usuario quiere filtrar si no es igual
                    listaFiltrada = df[df[nombreCampo] != palabra]
                    mostrarDataFrame(listaFiltrada)
                else: # El usuario quiere filtrar si no lo contiene
                    listaFiltrada = df[not palabra in df[nombreCampo]]
                    mostrarDataFrame(listaFiltrada)
            elif tipoCampo == "Integer" or tipoCampo == "Decimal":
                mostrarFiltrosNumericosMenu()
                optFiltro = obtenerOpcion(1,3)
                if optFiltro == 1: # El usuario quiere filtrar si es mayor que
                    listaFiltrada = df[df[nombreCampo] > palabra]
                    mostrarDataFrame(listaFiltrada)
                elif optFiltro == 2: # El usuario quiere filtrar si es menor que
                    listaFiltrada = df[df[nombreCampo] < palabra]
                    mostrarDataFrame(listaFiltrada)
                else: # El usuario quiere filtrar si es igual
                    listaFiltrada = df[df[nombreCampo] == palabra]
                    mostrarDataFrame(listaFiltrada)
            else:
                print(f"Ha ocurrido un error. Operación cancelada. {nombreCampo} -- {tipoCampo}")
                return
    else: # Si quiere agrupar
        todoBien, cnt = mostrarCamposNumericosEnMenu()
        if todoBien:
            df = pd.DataFrame(diccionarios) # Aprovechamos la librería Pandas para no tener que estar nosotros comprobando linea por linea
            optCampo = obtenerOpcion(1,cnt)
            data = obtenerCampoNumeroEnCampos(optCampo).split(":")
            nombreCampo = data[0]
            mediaEquipo = df.groupby("Team")[nombreCampo].mean() # Calculamos la media de los equipos en el campo indicado por el usuario
            print(f"La media por equipo del campo \"{nombreCampo}\" es: {mediaEquipo}", end="\n\n")
            mediaPosicion = df.groupby("Position")[nombreCampo].mean() # Calculamos la media por posición de jugadores del campo indicado por el usuario
            print(f"La media por posición del campo \"{nombreCampo}\" es: {mediaPosicion}")
        else:
            print("No se han encontrado campos numéricos. Operación cancelada.")
            return

def mostrarMenuFiltrarAgrupar():
    print("╔══════════ Filtrar o Agrupar ═════════╗")
    print("╠ 1. Filtrar.")
    print("╠ 2. Agrupar (Solo campos numéricos).")
    print("╚══════════════════════════════════════╝")

#############################################################################
#
#               APARTADO 11: Generar 3 tipos de gráficos.
#
#############################################################################

def generarGraficos():
    # Primero comprobamos que haya contenido
    global diccionarios, campos
    if len(campos) == 0:
        print("No se puede realizar estadísticas o cálculos porque no hay campos. Crea un nuevo campo con la opción 1.")
        return
    if len(diccionarios) == 0:
        print("No se puede realizar estadísticas o cálculos porque no hay elementos. Registra un nuevo elemento con la opción 3.")
        return
    
    mostrarMenuGraficos()
    opt = obtenerOpcion(1,4)
    df = pd.DataFrame(diccionarios)
    match opt:
        case 1: # Cantidad de goles por equipo (gráfico de barras)
            golesPorEquipo = df.groupby("Team")["Goals scored"].sum() # sumamos la cantidad de goles marcados por cada jugador por equipo
            plt.bar(golesPorEquipo.index,golesPorEquipo) # eje_x, eje_y | golesPorEquipo es una serie y por defecto ya devuelve los varios y usa como index el contenido del campo por el que ha agrupado
            plt.title("Cantidad de goles por equipo.")
            plt.xlabel("Equipos")
            plt.ylabel("Goles")
            plt.xticks(rotation=45, ha='right') # rotamos un poco los nombres para poder leerlos
            plt.grid(True, alpha=0.6)
            plt.show()
            plt.close()
        case 2: # Cantidad de pases por equipo (gráfico de barras)
            pasesPorEquipo = df.groupby("Team")["Passes"].sum()
            plt.bar(pasesPorEquipo.index,pasesPorEquipo)
            plt.title("Cantidad de pases por equipo.")
            plt.xlabel("Equipos")
            plt.ylabel("Pases")
            plt.xticks(rotation=45, ha='right')
            plt.grid(True, alpha=0.6)
            plt.show()
            plt.close()
        case 3: # Goles marcados por cada posición (gráfico de sectores)
            golesMarcadosPorPorteros = df[df["Position"] == "Goalkeeper"]["Goals scored"].sum()
            golesMarcadosPorDefensas = df[df["Position"] == "Defender"]["Goals scored"].sum()
            golesMarcadosPorMediocentros = df[df["Position"] == "Midfielder"]["Goals scored"].sum()
            golesMarcadosPorDelanteros = df[df["Position"] == "Forward"]["Goals scored"].sum()
            print(f"{golesMarcadosPorDelanteros} frente a {golesMarcadosPorDefensas}")
            plt.pie(
                [golesMarcadosPorDelanteros, golesMarcadosPorMediocentros, golesMarcadosPorDefensas, golesMarcadosPorPorteros],
                labels=["Goles marcados por delanteros", "Goles marcados por mediocentros", "Goles marcados por defensas", "Goles marcados por porteros"],
                autopct="%1.1f%%"
            )
            plt.title("Comparativa de goles marcados en cada posición.")
            plt.show()
            plt.close()
        case 4: # Jugadores con estilo de juego agresivo (gráfico de dispersión)
            x = df["Recoveries"]
            y = df["Yellow Cards"]
            nombres = df["Name"]
            plt.figure(figsize=(10, 6))
            plt.scatter(x, y, alpha=0.6)
            plt.title("Jugadores con estilo de juego agresivo (entradas vs tarjetas amarillas).")
            plt.xlabel("Cantidad de Recuperaciones")
            plt.ylabel("Tarjetas Amarillas")

            # Agregamos los nombres a los puntos de cada jugador
            for i, txt in enumerate(nombres):
                plt.annotate(txt, (x[i], y[i]), fontsize=8, rotation=45,xytext=(5,0), textcoords='offset points')

            plt.show()
            plt.close()

def mostrarMenuGraficos():
    print("╔═════════════════════════════════════════════ Gráficos Disponibles ════════════════════════════════════════════╗")
    print("╠ 1. Cantidad de goles por equipo (gráfico de barras).")
    print("╠ 2. Cantidad de pases por equipo (gráfico de barras).")
    print("╠ 3. Goles marcados por cada posición (gráfico de sectores).")
    print("╠ 4. Jugadores con estilo de juego agresivo (gráfico de dispersión).")
    print("╠═══ Esto se calcula comparando la cantidad de recuperaciones y tarjetas amarillas recibidas por jugador.")
    print("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")

#############################################################################
#
#               APARTADO 12: Exportar los resultados.
#
#############################################################################

# Le ofrecemos al usuario las opciones de ficheros en los que puede exportar y luego convertimos diccionarios[] a dataframe y lo pasamos al fichero correspondiente
def exportarResultados():
    # Primero, comprobamos que haya contenido porque si no vamos a crear un fichero vacío
    global diccionarios, campos
    if len(campos) == 0:
        print("No se puede exportar porque no hay campos. Crea un nuevo campo con la opción 1.")
        return
    if len(diccionarios) == 0:
        print("No se puede exportar porque no hay elementos. Registra un nuevo elemento con la opción 3.")
        return
    
    # Solicitamos los datos necesarios
    mostrarMenuTiposArchivos()
    opt = obtenerOpcion(1,2)
    nombre = input("Introduce el nombre que le quieres dar al fichero (no ponga la extensión): ")
    # Pasamos nuestra lista de diccionarios a DataFrame
    df = pd.DataFrame(diccionarios)
    # Creamos el fichero según los datos introducidos
    if opt == 1: # si es .xlsx
        df.to_excel(f"{nombre}.xlsx", index=False, encoding="utf-8") # index=False para que no exporte el número de cada fila
        print("¡Resultados exportados con éxito!")
    else:
        df.to_csv(f"{nombre}.csv", index=False) # index=False para que no exporte el número de cada fila
        print("¡Resultados exportados con éxito!")

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
    print("╔════════════════════════════════════════════ Menú Principal ════════════════════════════════════════════╗")
    print("╠ 1. Crear y ver los campos del diccionario.")
    print("╠ 2. Mostrar los datos del diccionario.")
    print("╠ 3. Añadir un nuevo elemento al diccionario.")
    print("╠ 4. Buscar elementos por un campo.")
    print("╠ 5. Calcular estadísticas.")
    print("╠ 6. Filtrar elementos según condición.")
    print("╠ 7. Generar top N (solo para campos numéricos).")
    print("╠ 8. Cargar archivo XLSX o CSV.")
    print("╠ 9. Añadir columnas nuevas con estadísticas o cálculos sobre los datos laliga_player_stats_19_20.")
    print("╠ 10. Aplicar filtros y agrupaciones.")
    print("╠ 11. Generar 3 tipos de gráficos.")
    print("╠ 12. Exportar los resultados.")
    print("╠ 13. Salir de la aplicación.")
    print("╚════════════════════════════════════════════════════════════════════════════════════════════════════════╝")

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

# Mostramos el DataFrame que nos pasan en forma de tabla
def mostrarDataFrame(dataFrame):
    print("╔══════════════════════════════════ Contenido de la lista ═══════════════════════════════════")
    cnt=0
    for i, entrada in dataFrame.iterrows():
        print(f"╠ {entrada}")
        cnt+=1
    print("╚════════════════════════════════════════════════════════════════════════════════════════════")
    print(f"Se han mostrado un total de {cnt} elementos.")

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
    while opt != 13: # Mientras que la opción elegida por el usuario sea distinta a la opción de salir
        mostrarMenuPrincipal()
        opt = obtenerOpcion(1,13)
        match opt:
            case 1: initCrearCamposDiccionario()
            case 2: mostrarDatosDiccionario()
            case 3: aniadirElementoDiccionario()
            case 4: buscarElementosPorUnCampo()
            case 5: calcularEstadisticas()
            case 6: filtrarElementosCondicion()
            case 7: generarTopN()
            case 8: cargarArchivo()
            case 9: aniadirEstadisticaOCalculo()
            case 10: filtrosAgrupaciones()
            case 11: generarGraficos()
            case 12: exportarResultados()
            case 13 : print("¡Hasta pronto!")

    print("Programa finalizado.")

if __name__ == '__main__':
    init()