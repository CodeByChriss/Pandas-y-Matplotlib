import pandas as pd
import matplotlib.pyplot as plt

# Muestra por terminal el Menú Principal de la aplicación
def mostrarMenuPrincipal():
    print("╔═════════════════ Menú Principal ═════════════════╗")
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
    print("╚══════════════════════════════════════════════════╝")

# Método principal que llama a mostrar el menú y recoge la respuesta
def init():
    opt = 0
    msg = ""
    while opt != 13: # Mientras que la opción elegida por el usuario sea distinta a la opción de salir
        mostrarMenuPrincipal()
        try:
            opt = int(input(f"{msg}Seleccione una opción: "))
        except ValueError:
            msg = "Debes introducir un número. "
            opt = 0
        else:
            if opt < 1 or opt > 13:
                msg = "Esa opción no existe. "
            else:
                msg = "" # Limpiamos el mensaje para que luego no aparezca de forma no deseada
                match opt:
                    case 1: print("opcion 1")
                    case 2: print("opcion 2")
                    case 3: print("opcion 3")
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