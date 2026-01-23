# 🚀 ¿Cómo puedo ejecutarlo?

1. Creamos el entorno virtual (doy por hecho que ya está instalado python)

```bash
python -m venv venv
```

2. Accedemos al entorno virtual

```bash
.\venv\Scripts\activate
```

3. Instalamos las dependencias

```bash
pip install pandas openpyxl matplotlib
```

4. Ejecutamos el fichero main.py
```bash
python main.py
```

Si queremos salir del entorno virtual:

```bash
deactivate
```

# ✍️ Enunciado
Desarrollar un programa en Python que permita estionar datos de un pequeño estudio (dataset propio inventado o real). Representar la información usando:

- listas de diccionarios
- funciones
- pandas

Generar gráficos con matplotlib.

El proyecto debe estar organizado en funciones y el usuario debe poder elegir opciones mediante un pequeño menú interactivo.

La temática es libre.

### Parte A — Gestión manual usando listas de diccionarios y funciones

Esta parte NO usa pandas. El usuario, mediante un menú por consola o visual (TKinter) debe poder:

- Crear una lista de diccionarios (cada diccionario representa un elemento).
- Mostrar datos (listar elementos)
- Añadir un elemento nuevo
- Buscar un elemento por un campo
- Calcular estadísticas (media, máximo, mínimo, recuentos...)
- Filtrar elementos según una condición
- Generar un top N (mayores valores)

### Parte B — Análisis avanzado con pandas y matplotlib

El usuario debe poder cargar un archivo XLXS o CSV para generar los datos de la parte A o para exportarlo.

Se deben añadir las siguientes funcionalidades:

- Añadir columnas nuevas con estadísticas o cálculos sobre los datos.
- Aplicar filtros y agrupaciones.
- Generar 3 tipos de gráficos distintos a partir de los datos.
- Exportar los resultados.

Se valorará que el código esté comentado y el desarrollo y avance en clase.