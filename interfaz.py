import  tkinter as tk
from    tkinter import ttk
from    CRUD import calcula_modelos, leer_modelos, leer_tiempo
import  eventos as eventos
import  re
import  dicc_variables
from    estilos import *


#####################################################################################################################################################
#####################################################################  RAIZ  ########################################################################
#####################################################################################################################################################

root = tk.Tk()
root.title("Programación de Planta")
root.config(bg=grisOscuro)
root.iconbitmap("logo5.ico")
root.geometry("800x600")
root.state('zoomed')

# Creación de los frames principales
frameVHyTEC = tk.Frame(root, bg=grisOscuro)
frameVehiculos = tk.Frame(frameVHyTEC, bg=grisOscuro)
frameTecnicos = tk.Frame(frameVHyTEC, bg=grisOscuro)
framePedido = tk.Frame(root, bg=grisClaro)

# Posicionar los frames 
frameVHyTEC.pack(expand=True, side="left", fill="both", padx = 3, pady= 3)
frameVehiculos.pack(expand=True, side="top", fill="both", padx = 3, pady= 3)
frameTecnicos.pack(expand=True, side="bottom", fill="both", padx = 3, pady= 3)
framePedido.pack(expand=True, side="right", fill="both", padx = 3, pady= 3)


#####################################################################################################################################################
####################################################### FRAME DE VEHICULOS (ARRIBA)###############################################################
#####################################################################################################################################################


# Crear un Canvas en el frame de Vehículos
canvasVehiculos = tk.Canvas(frameVehiculos, bg=moradoClaro)
canvasVehiculos.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Crear un Scrollbar y conectarlo con el Canvas
scrollbarVehiculos = tk.Scrollbar(frameVehiculos, orient=tk.VERTICAL, command=canvasVehiculos.yview)
scrollbarVehiculos.pack(side=tk.LEFT, fill=tk.Y)

canvasVehiculos.configure(yscrollcommand=scrollbarVehiculos.set)
canvasVehiculos.bind('<Configure>', lambda e: canvasVehiculos.configure(scrollregion=canvasVehiculos.bbox("all")))

# Crear un frame dentro del Canvas
frameVehiculosInterior = tk.Frame(canvasVehiculos, bg=grisOscuro)
canvasVehiculos.create_window((0, 0), window=frameVehiculosInterior, anchor="nw")



### Añadir contenido al frame interno ###
#Titulo de marcas
labelVehiculos = tk.Label(frameVehiculosInterior, text="MARCAS - Modelos", font=textoBajo, bg=grisClaro, fg=moradoOscuro)
labelVehiculos.grid(row=0, column=1, sticky="w")

#Titulo de tiempos
labelTiemposVehiculos = tk.Label(frameVehiculosInterior, text="Tiempos", font=textoBajo, bg=grisClaro, fg=moradoOscuro)
labelTiemposVehiculos.grid(row=0, column=2, columnspan=5, sticky="ew")



#Botón de crear modelo nuevo
button_CrearModelo = tk.Button(frameVehiculosInterior,text="Crear Modelo", font=textoBajo, bg=grisOscuro, fg=grisClaro,
                               command=eventos.crear_modelo)
button_CrearModelo.grid(row=0, column=7, padx=3)


#Botones de editar modelo
#button_variables_camMod = {}              #Diccionario para almacenar nombres de Botones de editar modelos
for filasCambiarMod in range (1, calcula_modelos()+1):
    button_name = f"ButtonAgregar{filasCambiarMod}"
    dicc_variables.button_variables_camMod[button_name] = tk.Button(frameVehiculosInterior,text="Editar", font=textoMinimo, bg=moradoClaro, fg=moradoOscuro,
                                                                    command=lambda varBoton=button_name:eventos.editar_modelo(varBoton))
    dicc_variables.button_variables_camMod[button_name].grid(row=filasCambiarMod, column=0, padx=3)


#label_variables_vehiculos = {}            # Diccionario para almacenar las variables de los Labels y sus textos
# Crear etiquetas para vehículos con nombres segun BD
for filasVehiculos, textos in zip(range(1, calcula_modelos()+1), leer_modelos()):                 
    label_name_vehiculo = f"labelVehiculo{filasVehiculos}"
    print(label_name_vehiculo)
    #Lee los nombres desde la BBDD
    dicc_variables.label_variables_vehiculos[label_name_vehiculo] = tk.Label(frameVehiculosInterior, text=textos[0]+" - "+textos[1], font=textoBajo, bg=grisClaro, fg=moradoOscuro)
    dicc_variables.label_variables_vehiculos[label_name_vehiculo].grid(row=filasVehiculos, column=1, sticky="ew")



# Diccionarios para almacenar las variables y los textos de los entry de tiempos por filas_columnas, ejemplo textExtryTime1_9
#string_variables = {}
#entry_variables = {}

#Crea los campos con los tiempos de proceso 
for columnastimes in range (1,6):

    for filastimes in range (1, calcula_modelos()+1):
        #Damos un nombre a la variable objeto
        string_name = f"textExtryTime{filastimes}_{columnastimes}"
        #print(string_name)
        #Relacionamos el nombre a al variable
        dicc_variables.string_variables[string_name] = tk.StringVar()
        #Extraemos el texto del label correspondiente a al marca-modelo
        texto_label = dicc_variables.label_variables_vehiculos[f"labelVehiculo{filastimes}"].cget("text")
        #Filtramos la última palabra: "modelo"
        palabra_modelo = re.search(r'\b(\w+)\b$', texto_label).group(1)

        #Buscamos en BD el tiempo de proceso correspondiente al modelo
        dicc_variables.string_variables[string_name].set(leer_tiempo(palabra_modelo, columnastimes + 1))
        entry_name = f"ExtryTime{filastimes}_{columnastimes}"
        #print(entry_name)
        dicc_variables.entry_variables[entry_name] = tk.Entry(frameVehiculosInterior, font=numerosPequeños, width=4, bg=moradoOscuro, fg=amarilloOscuro,
                                                              textvariable=dicc_variables.string_variables[string_name])
        dicc_variables.entry_variables[entry_name].grid(row=filastimes, column=columnastimes + 1)

button_variables_agregVh = {}

for filasAgregarVH in range (1, calcula_modelos()+1):
    button_name = f"ButtonAgregar{filasAgregarVH}"
    button_variables_agregVh[button_name] = tk.Button(frameVehiculosInterior,text="Agregar a Pedido", font=textoMinimo, bg=moradoMedio, fg=blancoFrio,
                                                      command=lambda varBoton=button_name:eventos.agregar_a_pedido(varBoton))
    button_variables_agregVh[button_name].grid(row=filasAgregarVH, column= 7, padx=3)


#######################################################################################################################################################
########################################################## FRAME DE PEDIDOS (DERECHA) ################################################################
#######################################################################################################################################################
frameTablaPedido = tk.Frame(framePedido)
frameTablaPedido.pack(fill="both", expand=True, padx=5,)


# Estilo personalizado para Treeview
styletreeview = ttk.Style()

# Cambiar el color de fondo y el color de la fuente para Treeview
styletreeview.configure("Treeview", background=grisOscuro, foreground=blancoHueso, rowheight=25, fieldbackground=grisMedio, font=textoBajo)

# Cambiar el color de selección
styletreeview.map("Treeview", background=[("selected", azulClaro)], foreground=[("selected", moradoOscuro)])


class FiltrosPedido():

    def __init__(self,pedido):
    # Crear un frame para los filtros
        self.frame_filtros = tk.Frame(frameTablaPedido)
        self.frame_filtros.pack(fill=tk.X, padx=2, pady=2, side="top")

    # Crear entradas de texto para los filtros
        self.entry_chasis = tk.Entry(self.frame_filtros, width=10)
        self.entry_chasis.grid(row=0, column=0, padx=5)
        self.entry_fecha = tk.Entry(self.frame_filtros, width=16)
        self.entry_fecha.grid(row=0, column=1, padx=5)
        self.entry_marca = tk.Entry(self.frame_filtros, width=11)
        self.entry_marca.grid(row=0, column=2, padx=5)
        self.entry_modelo = tk.Entry(self.frame_filtros, width=12)
        self.entry_modelo.grid(row=0, column=3, padx=5)
        self.entry_color = tk.Entry(self.frame_filtros, width=9)
        self.entry_color.grid(row=0, column=4, padx=5)
        self.entry_estado = tk.Entry(self.frame_filtros, width=12)
        self.entry_estado.grid(row=0, column=5, padx=5)
        self.entry_tiempos = tk.Entry(self.frame_filtros, width=16)
        self.entry_tiempos.grid(row=0, column=6, padx=5)
        self.entry_novedades = tk.Entry(self.frame_filtros, width=19)
        self.entry_novedades.grid(row=0, column=7, padx=5)
        self.entry_subcontratar = tk.Entry(self.frame_filtros, width=6)
        self.entry_subcontratar.grid(row=0, column=8, padx=5)

        # Crear un botón para aplicar los filtros
        self.boton_filtrar = tk.Button(self.frame_filtros, text="Filtro", command=lambda:self.filtrar_datos(pedido), font=numerosPequeños)
        self.boton_filtrar.grid(row=0, column=9)

    def filtrar_datos(self, pedido):
        # Obtener los criterios de filtro de las entradas
        self.datos = pedido.datos
        filtro_chasis = self.entry_chasis.get()
        filtro_fecha = self.entry_fecha.get()
        filtro_marca = self.entry_marca.get()
        filtro_modelo = self.entry_modelo.get()
        filtro_color = self.entry_color.get()
        filtro_estado = self.entry_estado.get()
        filtro_tiempos = self.entry_tiempos.get()
        filtro_novedades = self.entry_novedades.get()
        filtro_subcontratar = self.entry_subcontratar.get()
        
        # Limpiar la tabla
        for row in pedido.tablaPedidos.get_children():
            pedido.tablaPedidos.delete(row)
        
        # Agregar datos filtrados a la tabla
        for record in self.datos:
            if (filtro_chasis.lower() in str(record[0]).lower() and
                filtro_fecha.lower() in record[1].lower() and
                filtro_marca.lower() in str(record[2]).lower() and
                filtro_modelo.lower() in record[3].lower() and
                filtro_color.lower() in record[4].lower() and
                filtro_estado.lower() in record[5].lower() and
                filtro_tiempos.lower() in record[6].lower() and
                filtro_novedades.lower() in record[7].lower() and
                filtro_subcontratar.lower() in record[8].lower()):
                pedido.tablaPedidos.insert(parent='', index='end', iid=record[0], text='', values=record)


#Tabla para pedido
class TablaPedido():
    def __init__(self): #Crea latabla y un diccionario con los nombres de los campos

        #añadir canvas para manejar color de fondo
        """self.canvas = tk.Canvas(frameTablaPedido, bg=grisOscuro)
        #self.canvas.pack(side='left', fill='both', expand=True)
        #frameTablaPedido.update_idletasks()
        #self.canvas.config(width=frameTablaPedido.winfo_width(), height=frameTablaPedido.winfo_height())"""

        #Crear Tabla
        self.tablaPedidos = ttk.Treeview(frameTablaPedido, show="headings")
        self.tablaPedidos["columns"] = ("Chasis", "Fecha de entrega", "Marca", "Modelo", "Color", "Estado", "Tiempos", "Novedades", "Subcontratar")

        # Formatear las columnas
        self.tablaPedidos.column('#0', width=0, stretch=tk.NO)  # Columna fantasma
        self.tablaPedidos.column('Chasis', anchor=tk.CENTER, width=80)
        self.tablaPedidos.column('Fecha de entrega', anchor=tk.W, width=100)
        self.tablaPedidos.column('Marca', anchor=tk.CENTER, width=80)
        self.tablaPedidos.column('Modelo', anchor=tk.CENTER, width=80)
        self.tablaPedidos.column('Color', anchor=tk.CENTER, width=80)
        self.tablaPedidos.column('Estado', anchor=tk.CENTER, width=80)
        self.tablaPedidos.column('Tiempos', anchor=tk.CENTER, width=100)
        self.tablaPedidos.column('Novedades', anchor=tk.CENTER, width=150)
        self.tablaPedidos.column('Subcontratar', anchor=tk.CENTER, width=80)

        self.tablaPedidos.heading('#0', text='')  # Columna fantasma
        self.tablaPedidos.heading('Chasis', text='Chasis', anchor=tk.CENTER)
        self.tablaPedidos.heading('Fecha de entrega', text='Fecha de entrega', anchor=tk.W)
        self.tablaPedidos.heading('Marca', text='Marca', anchor=tk.CENTER)
        self.tablaPedidos.heading('Modelo', text='Modelo', anchor=tk.CENTER)
        self.tablaPedidos.heading('Color', text='Color', anchor=tk.CENTER)
        self.tablaPedidos.heading('Estado', text='Estado', anchor=tk.CENTER)
        self.tablaPedidos.heading('Tiempos', text='Tiempos', anchor=tk.CENTER)
        self.tablaPedidos.heading('Novedades', text='Novedades', anchor=tk.CENTER)
        self.tablaPedidos.heading('Subcontratar', text='Subcontratar', anchor=tk.CENTER)


    # Crear una barra de desplazamiento para la tabla y configurarla
        self.scrollbar = ttk.Scrollbar(frameTablaPedido, orient=tk.VERTICAL, command=self.tablaPedidos.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.tablaPedidos.configure(yscrollcommand=self.scrollbar.set)


        self.tablaPedidos.pack(expand=True, fill="both", side="bottom")
        self.llenarTabla()
    # Agregar datos a la tabla
        
    def llenarTabla(self):
        
        self.datos = eventos.leepedidoBBDD()

        if self.datos is not None:
            # Modificamos la lista con datos para que agrupe los tiempos
            for i in range(len(self.datos)):
                registro = self.datos[i]                                                            # Convertir los elementos en las posiciones 6 a 10 a una tupla
                tupla_tiempos = tuple(registro[6:11])                                               # Crear una lista modificable con los elementos excepto los que van a ser reemplazados           
                registro_modificado = list(registro[:6])+ [tupla_tiempos] + list(registro[11:])     # Convertir la tupla a una cadena separada por comas
                registro_modificado[6] = ', '.join(map(str, tupla_tiempos))                         # Actualizar la lista original con el registro modificado
                self.datos[i] = registro_modificado                                                 # Asignar el registro modificado al atributo datos
                print(self.datos[i])

            for record in self.datos:
                self.tablaPedidos.insert(parent='', index='end', iid=record[0], text='', values=record)



        #CREAR MENU CONTEXTUAL
        self.menu = tk.Menu(root, tearoff=0)
        self.menu.add_command(label="Modificar", command=lambda: print("Modificar seleccionada"))
        self.menu.add_command(label="Eliminar", command=lambda: print("Eliminar seleccionada"))


                # Manejar el evento del clic derecho
        def mostrar_menu(evento):
            try:
                item_id = self.tablaPedidos.identify_row(evento.y)  # Identificar la fila en la que se hizo clic
                self.tablaPedidos.selection_set(item_id)  # Seleccionar la fila

                # Mostrar el menú contextual en la posición del cursor
                self.menu.post(evento.x_root, evento.y_root)
            except:
                pass

        # Asociar el clic derecho al evento
        self.tablaPedidos.bind("<Button-3>", mostrar_menu)

        def programar_todo():
            pass

        def programar_inmediato():
            pass




    #Botones de programar pedido
        self.botonProgramarTodo = tk.Button(framePedido,text="Programar TODO", font=textoGrande, bg=naranjaMedio, fg=blancoFrio, command=programar_todo)
        self.botonProgramarTodo.pack()

    #Botones de programar pedido
        self.botonProgramarInmediato = tk.Button(framePedido,text="Programar INMEDIATO", font=textoGrande, bg=naranjaMedio, fg=blancoFrio, command=programar_inmediato)
        self.botonProgramarInmediato.pack()

pedido1=TablaPedido()
filtro1=FiltrosPedido(pedido1)
#######################################################################################################################################################
########################################################## FRAME DE TÉCNICOS (ABAJO) ################################################################
#######################################################################################################################################################

# Crear un Canvas en el frame de Tecnicos
canvasTecnicos = tk.Canvas(frameTecnicos, bg=verdeClaro)
canvasTecnicos.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Crear un Scrollbar y conectarlo con el Canvas
scrollbarTecnicos = tk.Scrollbar(frameTecnicos, orient=tk.VERTICAL, command=canvasTecnicos.yview)
scrollbarTecnicos.pack(side=tk.LEFT, fill=tk.Y)

canvasTecnicos.configure(yscrollcommand=scrollbarTecnicos.set)
canvasTecnicos.bind('<Configure>', lambda e: canvasTecnicos.configure(scrollregion=canvasTecnicos.bbox("all")))

# Crear un frame dentro del Canvas
frameTecnicosInterior = tk.Frame(canvasTecnicos, bg=grisOscuro)
canvasTecnicos.create_window((0, 0), window=frameTecnicosInterior, anchor="ne")



# Añadir contenido al frame interno
labelTecnicos = tk.Label(frameTecnicosInterior, text="NOMBRE", font=textoGrande, bg=verdeMedio, fg=verdeOscuro)
labelTecnicos.grid(row=0, column=0, sticky="we")

labelAreaTecnicos = tk.Label(frameTecnicosInterior, text="Área", font=textoGrande, bg=verdeMedio, fg=verdeOscuro)
labelAreaTecnicos.grid(row=0, column=1, sticky="we")

label_id_tecnicos = {}            # Diccionario para almacenar las variables de los Labels
# Crear etiquetas para vehículos con nombres consecutivos
for filasTecnicos in range(1, 26):                 
    label_id_tecnico = f"labelIdTecnico{filasTecnicos}"
    print(label_id_tecnico)
    label_id_tecnicos[label_id_tecnico] = tk.Label(frameTecnicosInterior, text="T# " + str(filasTecnicos), font=textoBajo, bg=verdeOscuro, fg=blancoHueso)
    label_id_tecnicos[label_id_tecnico].grid(row=filasTecnicos, column=0, sticky="we")


label_variables_tecnicos = {}            # Diccionario para almacenar las variables de los Labels
# Crear etiquetas para vehículos con nombres consecutivos
for filasTecnicos in range(1, 26):                 
    label_name_tecnico = f"labelTecnico{filasTecnicos}"
    print(label_name_tecnico)
    label_variables_tecnicos[label_name_tecnico] = tk.Label(frameTecnicosInterior, text="Tecnico " + str(filasTecnicos), font=textoBajo, bg=verdeOscuro, fg=blancoHueso)
    label_variables_tecnicos[label_name_tecnico].grid(row=filasTecnicos, column=1, sticky="we")

label_variables_especialidad = {}            # Diccionario para almacenar las variables de los Labels
for filasEspecialidad in range(1, 26):                 
    label_name_especialidad = f"labelEspecialidad{filasEspecialidad}"
    print(label_name_especialidad)
    label_variables_especialidad[label_name_tecnico] = tk.Label(frameTecnicosInterior, text="Especialidad de T" + str(filasEspecialidad), font=textoBajo, bg=verdeOscuro, fg=blancoHueso)
    label_variables_especialidad[label_name_tecnico].grid(row=filasEspecialidad, column=2, sticky="we")


#Añadir checklist para incluir en la programación a los técnicos
int_variables_tecnicos = {}         #Diccionario que tiene los nombres de las variables objeto
check_variables_tecnicos = {}       #Diccionario que tiene los nombre de los checkbutton

for filasCheck in range (1,26):
    int_name = f"checkName{filasCheck}"
    print(int_name)
    int_variables_tecnicos[int_name] = tk.IntVar(value=1)

    check_name_tecnico = f"checkTecnico{filasCheck}"
    print(check_name_tecnico)
    check_variables_tecnicos[check_name_tecnico] = tk.Checkbutton(frameTecnicosInterior, text="Programar", justify="left", bg=verdeClaro, font=textoMinimo, fg=verdeOscuro, anchor="w",
                                variable=int_variables_tecnicos[int_name],onvalue=1, offvalue=0)
    check_variables_tecnicos[check_name_tecnico].grid(row=filasCheck, column=3, sticky="w")

root.mainloop()