nombres_procesos = ['telequinox', 'PDI', 'lavado', 'pintura', 'calidad']                #PROCESOS EN ORDEN SECUENCIAL
orden_procesos = ['SIN PROCESAR'] + nombres_procesos + ['DESPACHO', 'ENTREGADO']        #DIFERENTES DE UN VEHÍCULO

# Modelos de vehículos agrupados por marcas
modelos = [
    "ALTIMA","FRONTIER","KICKS","QASHQAI","LEAFT","VERSA","PATHFINDER","XTRAIL",
    "CAPTUR","KOLEOS","KWID",
    "BJ20","BJ40","D50","NX55","X35","X55","U5P",
    "AUMARK","AUMAN","TUNLAND","VIEW","TOANO",
    "AZKARRA","COOLRAY",
    "RX8","RX5","MG5","ZS","ONE"
]

marcas = {
    "NISSAN":   ["ALTIMA","FRONTIER","KICKS","QASHQAI","LEAFT","VERSA","PATHFINDER","XTRAIL",],
    "RENAULT":  ["CAPTUR","KOLEOS","KWID",],
    "BAIC":     ["BJ20","BJ40","D50","NX55","X35","X55","U5P",],
    "FOTON":    ["AUMARK","AUMAN","TUNLAND","VIEW","TOANO",],
    "GEELY":    ["AZKARRA","COOLRAY",],
    "MG":       ["RX8","RX5","MG5","ZS","ONE"]
}

#Tiempo de los 5 procesos para cada modelo
tiempos = {
    "ALTIMA":       [0,   60,  60,  30,   15],
    "FRONTIER":     [420, 128, 55,  23,   15],
    "KICKS":        [150, 123, 55,  23,   15],
    "QASHQAI":      [330, 63,  55,  23,   15],
    "LEAFT":        [0,   63,  50,  23,   15],
    "VERSA":        [390, 123, 55,  23,   15],
    "PATHFINDER":   [60,  63,  60,  23,   15],
    "XTRAIL":       [60,  63,  55,  23,   15],
    "CAPTUR":       [60,  60,  60,  30,   15],
    "KOLEOS":       [60,  63,  60,  48,   15],
    "KWID":         [60,  68,  50,  48,   15],
    "BJ20":         [0,   72,  55,  52,   15],
    "BJ40":         [0,   72,  55,  52,   15],
    "D50":          [270, 72,  55,  52,   15],
    "NX55":         [240, 72,  55,  52,   15],
    "X35":          [270, 72,  55,  52,   15],
    "X55":          [0,   72,  55,  52,   15],
    "U5P":          [270, 72,  55,  52,   15],
    "AUMARK":       [0,   365, 120, 300,  15],
    "AUMAN":        [0,   960, 120, 1920, 15],
    "TUNLAND":      [270, 240, 120, 185,  15],
    "VIEW":         [240, 295, 90,  685,  15],
    "TOANO":        [240, 240, 90,  685,  15],
    "AZKARRA":      [0,   72,  55,  22,   15],
    "COOLRAY":      [0,   72,  55,  22,   15],
    "RX8":          [0,   92,  50,  15,   15],
    "RX5":          [0,   210, 50,  15,   15],
    "MG5":          [0,   105, 50,  15,   15],
    "ZS":           [0,   110, 50,  15,   15],
    "ONE":          [0,   200, 50,  15,   15]
}

personal = []





#FUNCIONES PARA BUSCAR TIEMPOS
def buscar_tiempo(modelo, proceso):         #Devuelve el tiempo de un solo proceso para un modelo dado.

    times = tiempos.get(modelo)             # Obtenemos la lista de tiempos para el modelo
    if times is None:
        return None  # Si el modelo no existe en el diccionario

    try:
        indice = nombres_procesos.index(proceso)    # Busca el índice del proceso
        return times[indice]                        # Devuelve el tiempo correspondiente al proceso
    except ValueError:
        print(f"El modelo {modelo} no existe")
        return None             # Si el proceso no se encuentra en la lista de procesos


def buscar_tiempos(modelo):     #Devuelve una lista con los tiempos de todos los procesos para un modelo dado.
    return tiempos.get(modelo)

#print(buscar_tiempo("ALTIMA","calidad"))
#print(buscar_tiempos("ALTIMA"))




class VehiculoBase:             # Son los tipos de vehiculos, es decir los modelos, con sus tiempos de proceso
    def __init__(self, modelo):
        self.modelo = modelo
        self.tiempos_proceso = buscar_tiempos(modelo)

    def obtener_tiempo_proceso(self, proceso):      #Obtiene el tiempo del proceso en cuestion para ese objeto vehiculo
        return buscar_tiempo(self.modelo, proceso)

    def __repr__(self):
        return f"Modelo: {self.modelo} - Tiempos {self.tiempos_proceso} \n"    #formato de impresión para cada modelo de vehículo


#print(AUMAN.obtener_tiempo_proceso('PDI'))
#print(ONE.obtener_tiempo_proceso('PDI'))
#print(PATHFINDER)



class Vehiculo(VehiculoBase):               #Es cada vehiculo único que pasa por los procesos de la planta
    def __init__(self, id_chasis, modelo, pedido, estado='SIN PROCESAR', plazo='None'):
        super().__init__(modelo)
        self.id_chasis = id_chasis
        self.pedido = pedido
        self.estado = estado
        self.inicio = 0             #Tiempo en minutos en que el vehículo inicia cierto proceso
        self.fin = 0                #Tiempo en minutos en que el vehículo termina cierto proceso
        self.tecnico_actual= None   #Tecnico que atendió determinaedo proceso del vehículo
        self.plazo = None
        self.historico_estados = [(estado, self.inicio, self.fin, self.tecnico_actual),]  # Guarda la historia de estado, el técnico que atendió cada proceso y sus momentos de inicio y fin de proceso

    def avanzar_estado(self, tecnico):
        # Avanza al siguiente estado del vehículo en el proceso secuencial;
        #solo puede avanzar el estado si se especifica el técnico que lo atenderá
        try:
            self.tecnico_actual = tecnico                       #Asigna  al vehículo el técnico pasado por parámetro. El parámetro "tecnico" es un objeto de la clase Tecnico()
            estado_actual = self.estado                         #Extrae el ultimo estado en el constructor
            siguiente_estado = orden_procesos[orden_procesos.index(estado_actual) + 1]      #Obtiene el siguiente estado o proceso de la secuencia
            self.estado = siguiente_estado                      #Actualiza el estado

            tiempo_proceso = self.obtener_tiempo_proceso(self.estado)  # Obtiene el tiempo de proceso para el estado actual, a partir del metodo de la clase padre VehiculoBase()
            self.inicio=tecnico.comienza                                # Obtiene el tiempo en el que terminó su anterior asignación el técnico en cuestión y actualiza el momento de inicio del vehículo para el proceso actual. El tiempo es un atributo del objeto Tecnico()
            self.fin = tecnico.termina                          # Calcula el tiempo en que terminará el proceso actual
            self.historico_estados.append((self.estado, self.inicio, self.fin, self.tecnico_actual.nombre))  # Agrega la asignación al histórico de estados del vehículo

        except IndexError:                          # Si no encuentra másprocesos en lista, arrojará un mensaje informando que el vehícuylo estará listo
            print(f"Vehículo {self.id_chasis} ha completado todos los procesos.")

    def __repr__(self):
        return f"Vehiculo(chasis: {self.id_chasis}, Modelo: {self.modelo}, Estado: {self.estado}, tiempos: {self.tiempos_proceso}, Resumen: {self.historico_estados}, Plazo: {self.plazo} \n"
        #Formato de impresión de vehículo
    




class Tecnico:                                  # Es cada técnico con nombre e ID
    
    def __init__(self, id_tecnico, nombre, especializacion):

        # Asegurar que el técnico no esté en la lista
        #print(f"{len(personal)} {id_tecnico}")
        if len(personal) != 0:
            if not any(tecnico.id_tecnico == id_tecnico for tecnico in personal):
                self.id_tecnico = id_tecnico
                self.nombre = nombre
                self.especializacion = especializacion
                self.comienza = 0
                self.termina = 0
                self.vehiculo_actual = None
                self.historico_asignacion = []
            else:
                print(f"Técnico con ID {id_tecnico} ya está en la lista.")
                return
        
        else:
            self.id_tecnico = id_tecnico
            self.nombre = nombre
            self.especializacion = especializacion
            self.comienza = 0
            self.termina = 0
            self.vehiculo_actual = None
            self.historico_asignacion = []
        
        personal.append(self)        
        #print(f"se agregó {id_tecnico}")




    def asignar_vehiculo(self, vehiculo):       # Asigna el vehículo al técnico que se pasa pro parámetro, actualiza los momentos de inicio, fin y estado y agrega esta infomación al resumen de asignaciones

        try:
            self.vehiculo_actual = vehiculo         #Cambia el vehículo que está atendiendo al que se asignará

            #CASO VEHICULO DEBE ESPERAR AL TÉCNICO
            if  vehiculo.fin <= self.termina:               # Evalua si el momento en que el vehículo a asignar terminó el proceso anterior OCURRE ANTES que el momento en que el técnico terminó la última asignación
            
                tiempo_proceso = vehiculo.obtener_tiempo_proceso(self.especializacion)          # obtiene eltiempo del proceso del vehículo
                self.comienza = self.termina                # Actualiza el momento de inicio (del técnico) del proceso actual al momento de fin (del técnico) del proceso anterior 
                #print(tiempo_proceso)
                self.termina += tiempo_proceso              # Calcula el momento de fin (del tecnico) del proceso actual
                vehiculo.avanzar_estado(self)               # Actualiza el estado usando el método de la clase Vehiculo
                self.historico_asignacion.append((self.vehiculo_actual.id_chasis, self.comienza, self.termina))  # Agrega el nuevo estado con sus caracteríticas al resumen de asignaciones
                return True
            

            #CASO TÉCNICO DEBE ESPERAR AL VEHÍCULO
            elif vehiculo.fin > self.termina:               # Evalua si el momento en que el vehículo a asignar terminó el proceso anterior OCURRE DESPUES que el momento en que el técnico terminó la última asignación
    
                tiempo_proceso = vehiculo.obtener_tiempo_proceso(self.especializacion)          # obtiene eltiempo del proceso del vehículo
                self.comienza= vehiculo.fin                 # Actualiza el momento de inicio (del técnico) del proceso actual al momento de fin (del vehículo) del proceso anterior 
                self.termina = vehiculo.fin+tiempo_proceso  # Calcula el momento de fin (del tecnico) del proceso actual
                vehiculo.avanzar_estado(self)               # Actualiza el estado usando el método de la clase Vehiculo
                self.historico_asignacion.append((self.vehiculo_actual.id_chasis, self.comienza, self.termina))  # Agrega el nuevo estado con sus caracteríticas al resumen de asignaciones
                return True
                
            return False
        
        except:
            print("No se ejecutó el método asignar_vehiculo")


    def __repr__(self):
        return f"Tecnico(ID: {self.id_tecnico}, Nombre: {self.nombre}, Especialización: {self.especializacion}, Asignaciones: {self.historico_asignacion}) \n"
        #Formato de impresión del técnico





class Pedido:
    def __init__(self, id_pedido, plazo_entrega, vehiculos, estado ="PENDIENTE"):
        self.id_pedido = id_pedido
        self.plazo_entrega = plazo_entrega
        self.vehiculos = vehiculos
        self.estado = estado
        for vehiculo in vehiculos:
            vehiculo.plazo = plazo_entrega
    
    def cambia_estado():
        pass

    def __repr__(self):
        return f"Pedido(ID: {self.id_pedido}, Fecha Entrega: {self.plazo_entrega}, Vehículos: {self.vehiculos}), Estado: {self.estado}"






def programa_inmediato(pedido, tecnicos, horizonte):

    vehiculos_por_programar = pedido.vehiculos.copy()                   # Extrae una copia de la lista de vehiculos

    while len(vehiculos_por_programar) > 0 :

        tiempos_restantes = list(map(lambda vh: sum(vh.tiempos_proceso), vehiculos_por_programar))                      #crea una lista con solo el total de tiempos restante de cada vehiculo
        indice_min_time = tiempos_restantes.index(min(tiempos_restantes))                                               #busca el índice con tiempo restante menor
        vehiculo_min_time = vehiculos_por_programar[indice_min_time]                                                    #busca el índice con tiempo restante menor

        ultimo_estado = vehiculo_min_time.estado                                        #Extrae el ultimo estado en el constructor
        siguiente_estado = orden_procesos[orden_procesos.index(ultimo_estado) + 1]      #Obtiene el siguiente estado o proceso de la secuencia

        tecnicos_disponibles = list(filter(lambda persona: siguiente_estado in persona.especializacion, tecnicos))      # incluye soloaquellos técnicos de la especialidad correcta
        tecnicos_disponibles.sort(key = lambda op: op.termina)                                                          #ordena técnicos por tiempo de menor a mayor

        tiempos_disponibles = list(map(lambda operario: operario.termina, tecnicos_disponibles))                        #crea una lista solo con los tiempos
        tiempos_disponibles.sort()                                                                                      #ordena tiempos de menor a mayor
        tecnico_min_time = tecnicos_disponibles[0]

        #print(tiempos_disponibles)
        #print(tecnicos_disponibles)


        for times in tiempos_disponibles:                                                               #buscamos en la lista de técnicos
            print(f"{times}+{vehiculo_min_time.obtener_tiempo_proceso(siguiente_estado)}")

            asignado = False

            if times + vehiculo_min_time.obtener_tiempo_proceso(siguiente_estado) <= horizonte:         #verificamos que el tiempo asignado no supere el horizonte
                print("sí se cumple la condición\n\n")
                tecnico_min_time.asignar_vehiculo(vehiculo_min_time)                                    #SE ASIGNA VEHICULO A TÉCNICO desde el método en la clase técnico
                asignado = True
                break
        
        if asignado == False:
            print(f"No se asignó {vehiculo_min_time.id_chasis}")

                
        vehiculos_por_programar.remove(vehiculo_min_time)        #REMOVEMOS DE LA LISTA EL VEHICULO QUE SE ACABA DE ASIGNAR               

    return pedido.vehiculos

#programa_inmediato(pedido_quito06, personal, 700)



def programa_completo(pedido, tecnicos, horizonte):

    vehiculos_por_programar = pedido.vehiculos.copy()                   # Extrae una copia de la lista de vehiculos

    while len(vehiculos_por_programar) > 0 :

        ind_est_actuales = list(map(lambda vh: orden_procesos.index(vh.estado),vehiculos_por_programar))                                      # encuentra una lista con los estado actual de cada vehículo
        for vehi in vehiculos_por_programar:
            print(vehi)

        tiempos_restantes = [
            sum(vh.tiempos_proceso[ind_est:] if ind_est < len(vh.tiempos_proceso) else 0)
            for vh, ind_est in zip(vehiculos_por_programar, ind_est_actuales)
            ]
            #crea una lista con solo el total de tiempos restante de cada vehiculo



        indice_min_time = tiempos_restantes.index(max(tiempos_restantes))                                               #busca el índice con tiempo mayor
        vehiculo_min_time = vehiculos_por_programar[indice_min_time]                                                    #busca el vehiculo con tiempo restante mayor

        ultimo_estado = vehiculo_min_time.estado                                        #Extrae el ultimo estado en el constructor
        siguiente_estado = orden_procesos[orden_procesos.index(ultimo_estado) + 1]      #Obtiene el siguiente estado o proceso de la secuencia

        tecnicos_disponibles = list(filter(lambda persona: siguiente_estado in persona.especializacion, tecnicos))      # incluye soloaquellos técnicos de la especialidad correcta
        tecnicos_disponibles.sort(key = lambda op: op.termina)                                                          #ordena técnicos por tiempo de menor a mayor

        tiempos_disponibles = list(map(lambda operario: operario.termina, tecnicos_disponibles))                        #crea una lista solo con los tiempos
        tiempos_disponibles.sort()                                                                                      #ordena tiempos de menor a mayor
        tecnico_min_time = tecnicos_disponibles[0]

        #print(tiempos_disponibles)
        #print(tecnicos_disponibles)


        for times in tiempos_disponibles:                                                               #buscamos en la lista de técnicos
            print(f"{times}+{vehiculo_min_time.obtener_tiempo_proceso(siguiente_estado)}")

            asignado = False

            if times + vehiculo_min_time.obtener_tiempo_proceso(siguiente_estado) <= horizonte:         #verificamos que el tiempo asignado no supere el horizonte
                print("sí se cumple la condición")
                tecnico_min_time.asignar_vehiculo(vehiculo_min_time)                                    #SE ASIGNA VEHICULO A TÉCNICO desde el método en la clase técnico
                print(f"Se asignó {vehiculo_min_time.id_chasis} a {tecnico_min_time.id_tecnico}\n\n")
                asignado = True
                break
        
        if asignado == False:
            print(f"No se asignó {vehiculo_min_time.id_chasis}")

        if vehiculo_min_time.estado == 'calidad':

            vehiculos_por_programar.remove(vehiculo_min_time)        #REMOVEMOS DE LA LISTA EL VEHICULO QUE SE ACABA DE ASIGNAR               

    return pedido.vehiculos


def calcular_horizonte(pedido):
    return max(map(lambda vh: vh.fin, pedido.vehiculos))


