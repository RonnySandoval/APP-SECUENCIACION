from planta import personal
from funcionesGANTT import crear_gantt_vehiculos, agregar_proceso, mostrar_grafico_vehiculos, colores_tecnicos
from funcionesGANTT import crear_gantt_tecnicos, agregar_vehiculo, mostrar_grafico_tecnicos, colores_tecnicos
from Objetos import pedido_quito06, horizonte_calculado


#######GANTT DE VEHICULOS#########
def generar_gantt_vehiculos(pedido):

    lista_vehiculos =[]
    for tarea in pedido.vehiculos:
        datos_vehiculo = [tarea.id_chasis, tarea.modelo]                         #extrae la lista con nombres de vehículos
        lista_vehiculos.append(tarea.id_chasis)

    #generación de gráfico con etiquetas de ejes
    crear_gantt_vehiculos("GRAFICO_DE_VEHICULOS_01",lista_vehiculos, horizonte_calculado)

    for tarea in pedido.vehiculos:

        for proceso in tarea.historico_estados:         #busca los parámetros de entrada para cada tarea del grafico
            nombre_proceso = proceso[0]                 #extrae el nombre del proceso del 1er elemento del atributo historico estados (proceso)
            inicio = proceso[1]                         #extrae el nombre del proceso del 2do elemento del atributo historico estados (inicio de proceso)
            duracion = proceso[2]- proceso[1]           #extrae el nombre del proceso del 2do y 3er elemento del atributo historico estados (inicio y fin de proceso)
            encargado = proceso[3]                      #extrae el nombre del proceso del 4to elemento del atributo historico estados (tecnico)
            if duracion == 0:                           #evalua si la tarea no ocupa tiempo
                pass
            else:    
                agregar_proceso("GRAFICO_DE_VEHICULOS_01",inicio, duracion, tarea.id_chasis, nombre_proceso, encargado)
                print(f"Se agregó {nombre_proceso} en {tarea.id_chasis}")
        
    mostrar_grafico_vehiculos("GRAFICO_DE_VEHICULOS_01")



#######GANTT DE TECNICOS#########
def generar_gantt_tecnicos(personal):
    lista_personas =[]
    print(personal)
    for persona in personal:
        datos_tecnico = [persona.id_tecnico, persona.nombre]                         #extrae la lista con nombres de vehículos
        lista_personas.append(persona.id_tecnico)

    #generación de gráfico con etiquetas de ejes
    crear_gantt_tecnicos("GRAFICO_DE_TECNICOS_02", lista_personas, horizonte_calculado)

    for tarea in personal:

        for vehiculo in tarea.historico_asignacion:         #busca los parámetros de entrada para cada tarea del grafico
            id_vehiculo = vehiculo[0]                       #extrae el nombre del proceso del 1er elemento del atributo asignacion estados (vehiculo)
            inicio = vehiculo[1]                            #extrae el nombre del proceso del 2do elemento del atributo asignacion estados (inicio de vehiculo)
            duracion = vehiculo[2]- vehiculo[1]             #extrae el nombre del proceso del 2do y 3er elemento del atributo asignacion estados (inicio y fin de vehiculo)
            if duracion == 0:                               #evalua si la tarea no ocupa tiempo
                pass
            else:    
                agregar_vehiculo("GRAFICO_DE_TECNICOS_02",inicio, duracion, tarea.id_tecnico, id_vehiculo)
                print(f"Se agregó {id_vehiculo} en {tarea.id_tecnico}")
        
    mostrar_grafico_tecnicos("GRAFICO_DE_TECNICOS_02")

generar_gantt_tecnicos(personal)
generar_gantt_vehiculos(pedido_quito06)