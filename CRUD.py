import sqlite3
from planta import modelos, marcas, tiempos


#Crear la tabla para modelos
def crear_tabla_modelos():

    conn = sqlite3.connect('produccion.db')
    cursor = conn.cursor()

    create_table_script = """
    CREATE TABLE modelos_vehiculos (
        MARCA VARCHAR NOT NULL,
        MODELO VARCHAR PRIMARY KEY,
        time_telequinox INTEGER NOT NULL,
        time_PDI INTEGER NOT NULL,
        time_LAVADO INTEGER NOT NULL,
        time_PINTURA INTEGER NOT NULL,
        time_CALIDAD INTEGER NOT NULL
    )
    """

    cursor.execute(create_table_script)
    conn.commit()
    conn.close()

    print("Tabla 'modelos_vehiculos' creada exitosamente.")

#Crear la tabla para vehiculos de pedido
def crear_tabla_vehiculos():
    # Conectar a la base de datos (o crearla si no existe)
    conn = sqlite3.connect('produccion.db')
    cursor = conn.cursor()

    create_table_script = """
    CREATE TABLE vehiculos (
        CHASIS VARCHAR PRIMARY KEY,
        FECHA VARCHAR NOT NULL,        
        MARCA VARCHAR NOT NULL,
        MODELO VARCHAR,
        COLOR VARCHAR NOT NULL,
        ESTADO VARCHAR NOT NULL,
        TIME_TEL VARCHAR NOT NULL,
        TIME_PDI VARCHAR NOT NULL,
        TIME_LAV VARCHAR NOT NULL,
        TIME_PIN VARCHAR NOT NULL,
        TIME_CAL VARCHAR NOT NULL,
        NOVEDADES VARCHAR NOT NULL,
        SUBCONTRATAR VARCHAR NOT NULL,
        FOREIGN KEY (MODELO) REFERENCES modelos_vehiculos(MODELO)
    )
    """
    cursor.execute(create_table_script)
    conn.commit()
    conn.close()

    print("Tabla 'Vehiculos_pedido' creada exitosamente.")


def eliminar_tabla(nombre_tabla):
    try:
        # Conectarse a la base de datos
        conn = sqlite3.connect('produccion.db')
        cursor = conn.cursor()
        
        # Crear el comando SQL para eliminar la tabla
        drop_table_script = f"DROP TABLE IF EXISTS {nombre_tabla}"
        cursor.execute(drop_table_script)
        conn.commit()
        print(f"Tabla '{nombre_tabla}' eliminada exitosamente.")
        
    except sqlite3.Error as e:
        print(f"Error al eliminar la tabla: {e}")
    
    finally:
        conn.close()


#Inserta un nuevo registro en la tabla de modelos
def insertar_modelo(marca, modelo, ttel, tpdi, tlav, tpin, tcal):
    try:
        conn = sqlite3.connect('produccion.db')
        cursor = conn.cursor()

        if all(item is not None for item in (marca, modelo, ttel, tpdi, tlav, tpin, tcal)):
           
            insert_data_script = """INSERT INTO modelos_vehiculos 
                                    (MARCA, MODELO, time_telequinox, time_PDI, time_LAVADO, time_PINTURA, time_CALIDAD)
                                    VALUES (?, ?, ?, ?, ?, ?, ?)
                                """
            
        cursor.execute(insert_data_script, (marca, modelo, ttel, tpdi, tlav, tpin, tcal))
        conn.commit()
        print("Registro añadido")
        
    except sqlite3.Error as e:
        print(f"Error al insertar el registro: {e}")

    except UnboundLocalError as e:
        print(f"No se llenaron todos los campos: {e}") 

    finally:
        conn.close()


#Borra un registro en la tabla de modelos basandose en el nombre de modelo
def eliminar_modelo(modelo):
    try:
        conn = sqlite3.connect('produccion.db')
        cursor = conn.cursor()
        
        # Sentencia SQL para eliminar el registro
        delete_data_script = """DELETE FROM modelos_vehiculos
                                WHERE MODELO = ?
                             """
        
        cursor.execute(delete_data_script, (modelo,))
        conn.commit()
        
        # Verificar cuántas filas fueron afectadas
        if cursor.rowcount > 0:
            print("Registro eliminado")
        else:
            print("No se encontró el registro para eliminar")
    
    except sqlite3.Error as e:
        print(f"Error al eliminar el registro: {e}")
    
    finally:
        conn.close()


#Cuenta la cantidad de registros en la tabla de modelos
def calcula_modelos():

    conn = sqlite3.connect('produccion.db')
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM modelos_vehiculos;')
    numero_registros = cursor.fetchone()[0]

    conn.close()
    return numero_registros


#Lee las marcas y los modelos y los empaqueta en una lista de tuplas
def leer_modelos():

    conn = sqlite3.connect('produccion.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM modelos_vehiculos;')
    todosRegistros = cursor.fetchall()
    los_modelos = [(registro[0], registro[1]) for registro in todosRegistros]
    print(los_modelos)

    conn.close()
    return los_modelos


#Lee un registro de la tabla modelos basandose en el nombre de modelos
def leer_modelo(modeloVehiculo):

    conn = sqlite3.connect('produccion.db')
    cursor = conn.cursor()
    el_modelo = modeloVehiculo
    cursor.execute('SELECT * FROM modelos_vehiculos WHERE modelo=?',(el_modelo,))
    registro = cursor.fetchone()
    print(registro)

    conn.close()
    return registro


#Buscar el tiempo de un proceso de un modelo en la tabla modelos
def leer_tiempo(modeloVehiculo,indiceColumna):
    # 3 = telequinox, 4 = PDI, 5 = LAVADO, 6 = PINTURA, 7 = CALIDAD

    conn = sqlite3.connect('produccion.db')
    cursor = conn.cursor()
    el_modelo = modeloVehiculo
    cursor.execute('SELECT * FROM modelos_vehiculos WHERE modelo=?',(el_modelo,))
    registro = cursor.fetchone()
    print(registro)
    tiemposIndiv = registro[indiceColumna]
    print(tiemposIndiv)

    conn.close()
    return tiemposIndiv


#Inserta un nuevo registro en la tabla de pedidos
def insertar_vehiculo(chasis, fecha, marca, modelo, color, estado, ttel, tpdi, tlav, tpin, tcal, novedades, subcontratar):
    try:
        conn = sqlite3.connect('produccion.db')
        cursor = conn.cursor()

        if all(item is not None for item in (chasis, fecha, marca, modelo, color, estado, ttel, tpdi, tlav, tpin, tcal, novedades, subcontratar,)):
            
            insert_data_script = """INSERT INTO vehiculos 
                                    (CHASIS, FECHA, MARCA, MODELO, COLOR, ESTADO, TIME_TEL, TIME_PDI, TIME_LAV, TIME_PIN, TIME_CAL, NOVEDADES, SUBCONTRATAR)
                                    VALUES  (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                                """
            
        cursor.execute(insert_data_script, (chasis, fecha, marca, modelo, color, estado, ttel, tpdi, tlav, tpin, tcal, novedades, subcontratar))
        conn.commit()
        print("Registro añadido")
        
    except sqlite3.Error as e:
        print(f"Error al insertar el registro: {e}")

    except UnboundLocalError as e:
        print(f"No se llenaron todos los campos: {e}") 

    finally:
        conn.close()

        


def leer_vehiculos():

    conn = sqlite3.connect('produccion.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM vehiculos;')
    registros = cursor.fetchall()
    print(registros)

    conn.close()
    return registros



def eliminar_vehiculo(chasis):
    try:
        conn = sqlite3.connect('produccion.db')
        cursor = conn.cursor()
        
        # Sentencia SQL para eliminar el registro
        delete_data_script = """DELETE FROM vehiculos
                                WHERE CHASIS = ?
                             """
        
        cursor.execute(delete_data_script, (chasis,))
        conn.commit()
        
        # Verificar cuántas filas fueron afectadas
        if cursor.rowcount > 0:
            print("Registro eliminado")
        else:
            print("No se encontró el registro para eliminar")
    
    except sqlite3.Error as e:
        print(f"Error al eliminar el registro: {e}")
    
    finally:
        conn.close()



#crear_tabla_vehiculos()
#eliminar_tabla("vehiculos")

#insertar_vehiculo(1,2,3,4,5,6,7,8,9)
#eliminar_vehiculo("fvghbd2")



"""
# ITERAR SOBRE MODELOS Y MARCAS PARA ALIMENTAR LA BASE DE DATOS
for marca, lista_modelos in marcas.items():
    for modelo in lista_modelos:
        # Aquí 'modelo' es la clave del diccionario tiempos
        if modelo in tiempos:
            tiempos_modelo = tiempos[modelo]
            
            # Imprimir la marca, el modelo y los tiempos correspondientes
            print(f'Marca: {marca}, Modelo: {modelo}, Tiempos: {tiempos_modelo}')
            
            # Ejemplo de cómo podrías usar los tiempos
            for indice, tiempo in enumerate(tiempos_modelo):
                print(f'  Índice: {indice}, Tiempo: {tiempo}')
                
            insertar_modelo(marca, modelo, tiempos_modelo[0], tiempos_modelo[1], tiempos_modelo[2], tiempos_modelo[3], tiempos_modelo[4])
"""