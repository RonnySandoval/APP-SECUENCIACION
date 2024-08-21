import tkinter as tk
import re
import CRUD
import dicc_variables
from ventanas_auxiliares import VentanaCreaEdita, VentanaGestionaPedido


def crear_modelo():
    print("pusó el botón crear modelo")
    ventana = VentanaCreaEdita("CREAR")
    ventana.asignafuncionBoton(lambda:guardar_modelo(ventana), lambda:cancelar(ventana))



def guardar_modelo(ventana):
    print(ventana)
    datos = (ventana.varMarca.get(),
            ventana.varModelo.get(),
            ventana.varTel.get(),
            ventana.varPdi.get(),
            ventana.varLav.get(),
            ventana.varPin.get(),
            ventana.varCal.get()
    )
    CRUD.insertar_modelo(*datos)
    ventana.rootAux.destroy()

    #leer BBDD y rellenar los label con la BBDD actualizada

def agregarVH_pedido(ventana):
    #Se recogen los datos de la fila
    datos = (ventana.varChasis.get(),
             ventana.varFecha.get(),
            ventana.varMarca.get(),
            ventana.varModelo.get(),
            ventana.varColor.get(),
            ventana.varEstado.get(),
            ventana.varTel.get(),
            ventana.varPdi.get(),
            ventana.varLav.get(),
            ventana.varPin.get(),
            ventana.varCal.get(),
            ventana.varNoved.get(),
            ventana.varSubcon.get(),
    )
    for dato in datos:
        print (dato)
    CRUD.insertar_vehiculo(*datos)


def recoger_datos_modelo(filaBoton):
    #extraer el numero dela fila
    fila = re.search(r'(\d+)$', filaBoton).group(1)
    #obtener la marca y el modelo apartir del numero de la fila
    marca_modelo = dicc_variables.label_variables_vehiculos[f"labelVehiculo{fila}"].cget("text")
    marca = re.search(r'^(.*?)\s*-\s*(.*?)$', marca_modelo).group(1).strip()            #trunca solo la marca
    modelo = re.search(r'^(.*?)\s*-\s*(.*?)$', marca_modelo).group(2).strip()           #trunca solo el modelo
    print(f"marca={marca} modelo={modelo}")
    tiempos=[]
    for columna in range(1,6):
        tiempos.append(dicc_variables.entry_variables[f"ExtryTime{fila}_{columna}"].get())  #obtiene el tiempo de proceso y lo agrega a la lista
    print(tiempos)
    return [marca, modelo] + tiempos



def editar_modelo(botonPulsado):
    print(recoger_datos_modelo(botonPulsado))
    datos = recoger_datos_modelo(botonPulsado)
    ventana = VentanaCreaEdita("EDITAR")
    ventana.set_values(datos)
    ventana.asignafuncionBoton(lambda:guardar_modelo(ventana), lambda:cancelar(ventana))

    #recoger datos
    #conectar con BD
    #agregar registro
    #leer BBDD y rellenar los label con la BBDD actualizada


def agregar_a_pedido(botonPulsado):
    print(recoger_datos_modelo(botonPulsado))
    datos = recoger_datos_modelo(botonPulsado)
    ventana = VentanaGestionaPedido("AGREGAR")
    ventana.set_values(datos)
    ventana.asignafuncionBoton(lambda:agregarVH_pedido(ventana), lambda:cancelar(ventana))
    ventana.rootAux.destroy()

def cancelar(ventana):
    ventana.rootAux.destroy()

def leepedidoBBDD():
    return CRUD.leer_vehiculos()

    