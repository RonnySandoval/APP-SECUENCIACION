import matplotlib.pyplot as plt
import numpy as np
import random as rdm


##################################################################################################################
########################################  GRÁFICOS PARA TÉCNICOS  ################################################
##################################################################################################################

# Diccionario global para almacenar las figuras
graficos_tecnicos = {}

# Función para crear el gráfico
def crear_gantt_tecnicos(nombre_grafico, tecnicos, horizonte):
    hbar = 10
    num_tecnicos = len(tecnicos)
    fig, gantt = plt.subplots()  # Objetos del plot

    diagrama = {
        "fig": fig,
        "ejes": gantt,
        "hbar": hbar,
        "tecnicos": tecnicos,
        "horizonte": horizonte
    }

    gantt.set_xlabel('Minutos')             # Etiqueta de eje X
    gantt.set_ylabel('Técnicos')            # Etiqueta de eje Y

    gantt.set_xlim(0, horizonte)            # Límites eje X
    gantt.set_ylim(0, num_tecnicos * hbar)  # Límites de eje Y

    gantt.set_xticks(range(0, horizonte, 10), minor=True)  # Divisiones de eje de tiempo
    gantt.grid(True, axis="x", which="both")

    gantt.set_yticks(range(hbar, num_tecnicos * hbar, hbar), minor=True)  # Divisiones de eje de técnicos
    gantt.grid(True, axis="y", which="minor")

    gantt.set_yticks(np.arange(hbar / 2, hbar * num_tecnicos - hbar / 2 + hbar, hbar))  # Etiquetas de técnicos
    gantt.set_yticklabels(tecnicos)

    # Guardar el diagrama en el diccionario global
    graficos_tecnicos[nombre_grafico] = diagrama

    return diagrama

# Función para agregar tareas
colores_vehiculos = {}
def agregar_vehiculo(nombre_grafico, t0, duracion, tecnico, nombre, color=None):
    diagrama = graficos_tecnicos.get(nombre_grafico)
    if diagrama is None:
        print(f"Error: El gráfico '{nombre_grafico}' no existe.")
        return

    tecnicos = diagrama["tecnicos"]
    gantt = diagrama["ejes"]
    hbar = diagrama["hbar"]
    horizonte = diagrama["horizonte"]

    if nombre in colores_vehiculos:
        color = colores_vehiculos[nombre]
    else:
        if color is None:
            color = (rdm.uniform(0, 0.7), rdm.uniform(0, 0.7), rdm.uniform(0, 0.7))
        colores_vehiculos[nombre] = color


    if color is None:
        color = (rdm.uniform(0, 0.7), rdm.uniform(0, 0.7), rdm.uniform(0, 0.7))

    ind_tec = tecnicos.index(tecnico)
    gantt.broken_barh([(t0, duracion)], (hbar * ind_tec, hbar), facecolors=color)
    gantt.text(x=t0 + duracion / 2, y=hbar * ind_tec + hbar / 2,
               s=f'{nombre}\n({duracion})', va="center", ha="center",
               color="w", fontsize=6)

# Función para mostrar un gráfico específico
def mostrar_grafico_tecnicos(nombre_grafico):
    diagrama = graficos_tecnicos.get(nombre_grafico)
    if diagrama is None:
        print(f"Error: El gráfico '{nombre_grafico}' no existe.")
        return

    plt.figure(diagrama["fig"].number)  # Seleccionar la figura por número
    plt.show()








"""
# Ejemplo de uso
horizonte = 500
lista_tecnicos = ['TELEQ1', 'TELEQ2', 'TELEQ3', 'PDI1', 'PDI2', 'PDI3', 'LAVAD1', 'LAVAD2', 'PINTU', 'CALID']

# Crear gráficos
crear_gantt_tecnicos("grafico1", lista_tecnicos, horizonte)
crear_gantt_tecnicos("grafico2", lista_tecnicos, horizonte)

# Agregar tareas a los gráficos
agregar_vehiculo("grafico1", 0, 55, 'TELEQ1', 'FRONTIER')
agregar_vehiculo("grafico1", 60, 55, 'PDI1', 'FRONTIER')
agregar_vehiculo("grafico2", 155, 35, 'PDI1', 'QASHQAI')
agregar_vehiculo("grafico2", 230, 78, 'PDI2', 'AUMAN')

# Mostrar gráficos específicos
mostrar_grafico("grafico1")
mostrar_grafico("grafico2")
"""






###################################################################################################################
########################################  GRÁFICOS PARA VEHÍCULOS  ################################################
###################################################################################################################
# Diccionario global para almacenar las figuras
graficos_vehiculos = {}         # Diccionario global para almacenar las figuras

# Función para crear el gráfico
def crear_gantt_vehiculos(nombre_grafico, vehiculos, horizonte):
    hbar = 10
    num_vehiculos = len(vehiculos)
    fig, gantt = plt.subplots()  # Objetos del plot

    diagrama = {
        "fig": fig,
        "ejes": gantt,
        "hbar": hbar,
        "tecnicos": vehiculos,
        "horizonte": horizonte
    }

    gantt.set_xlabel('Minutos')             # Etiqueta de eje X
    gantt.set_ylabel('Vehículos')            # Etiqueta de eje Y

    gantt.set_xlim(0, horizonte)            # Límites eje X
    gantt.set_ylim(0, num_vehiculos * hbar)  # Límites de eje Y

    gantt.set_xticks(range(0, horizonte, 20), minor=True)  # Divisiones de eje de tiempo
    gantt.grid(True, axis="x", which="both")

    gantt.set_yticks(range(hbar, num_vehiculos * hbar, hbar), minor=True)  # Divisiones de eje de técnicos
    gantt.grid(True, axis="y", which="minor")

    gantt.set_yticks(np.arange(hbar / 2, hbar * num_vehiculos - hbar / 2 + hbar, hbar))  # Etiquetas de técnicos
    gantt.set_yticklabels(vehiculos)

    # Guardar el diagrama en el diccionario global
    graficos_vehiculos[nombre_grafico] = diagrama

    return diagrama

# Diccionario para almacenar los colores de cada técnico
colores_tecnicos = {}

# Función para agregar tareas
def agregar_proceso(nombre_grafico, t0, duracion, vehiculo, nombre, tecnico, color=None):
    diagrama = graficos_vehiculos.get(nombre_grafico)
    if diagrama is None:
        print(f"Error: El gráfico '{nombre_grafico}' no existe.")
        return

    tecnicos = diagrama["tecnicos"]
    gantt = diagrama["ejes"]
    hbar = diagrama["hbar"]

    if tecnico in colores_tecnicos:
        color = colores_tecnicos[tecnico]
    else:
        if color is None:
            color = (rdm.uniform(0, 0.7), rdm.uniform(0, 0.7), rdm.uniform(0, 0.7))
        colores_tecnicos[tecnico] = color

    ind_tec = tecnicos.index(vehiculo)
    gantt.broken_barh([(t0, duracion)], (hbar * ind_tec, hbar), facecolors=color)
    gantt.text(x=t0 + duracion / 2, y=hbar * ind_tec + hbar / 2, 
               s=f'{nombre}\n{duracion}"\n({tecnico})', 
               va="center", ha="center", color="w", fontsize=6)
    

# Función para mostrar un gráfico específico
def mostrar_grafico_vehiculos(nombre_grafico):
    diagrama = graficos_vehiculos.get(nombre_grafico)
    if diagrama is None:
        print(f"Error: El gráfico con '{nombre_grafico}' no existe.")
        return

    plt.figure(diagrama["fig"].number)  # Seleccionar la figura por número
    plt.show()


"""
horizonte = 500
lista_vehiculos = ['VH11', 'VH22', 'VH33', 'VH44']

# Crear gráficos
crear_gantt_vehiculos("grafico1", lista_vehiculos, horizonte)
crear_gantt_vehiculos("grafico2", lista_vehiculos, horizonte)

# Agregar tareas a los gráficos
agregar_proceso("grafico1", 0, 55, 'VH11', 'TELEQUINOX', 'David')
agregar_proceso("grafico1", 60, 55, 'VH22', 'PDI', 'Cristian')
agregar_proceso("grafico2", 155, 35, 'VH33', 'lAVADO', 'Jesus')
agregar_proceso("grafico2", 230, 78, 'VH44', 'PINTURA', 'Luis')

# Mostrar gráficos específicos
mostrar_grafico_vehiculos("grafico1")
mostrar_grafico_vehiculos("grafico2")
"""




