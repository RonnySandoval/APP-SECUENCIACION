from planta import Vehiculo, VehiculoBase, Tecnico, Pedido
from planta import personal, nombres_procesos, orden_procesos, modelos, tiempos, programa_completo, programa_inmediato, calcular_horizonte

# Instancias de todos lo modelos actuales de la planta

ALTIMA = VehiculoBase('ALTIMA')
FRONTIER = VehiculoBase('FRONTIER')
KICK = VehiculoBase('KICK')
QASHQAI = VehiculoBase('QASHQAI')
LEAFT = VehiculoBase('LEAFT')
VERSA = VehiculoBase('VERSA')
PATHFINDER = VehiculoBase('PATHFINDER')
XTRAIL = VehiculoBase('XTRAIL')
CAPTUR = VehiculoBase('CAPTUR')
KOLEOS = VehiculoBase('KOLEOS')
KWID = VehiculoBase('KWID')
BJ20 = VehiculoBase('BJ20')
BJ40 = VehiculoBase('BJ40')
D50 = VehiculoBase('D50')
NX55 = VehiculoBase('NX55')
X35 = VehiculoBase('X35')
X55 = VehiculoBase('X55')
U5P = VehiculoBase('U5P')
AUMARK = VehiculoBase('AUMARK')
AUMAN = VehiculoBase('AUMAN')
TUNLAND = VehiculoBase('TUNLAND')
VIEW = VehiculoBase('VIEW')
TOANO = VehiculoBase('TOANO')
AZKARRA = VehiculoBase('AZKARRA')
COOLRAY = VehiculoBase('COOLRAY')
RX8 = VehiculoBase('RX8')
RX5 = VehiculoBase('RX5')
MG5 = VehiculoBase('MG5')
ZS = VehiculoBase('ZS')
ONE = VehiculoBase('ONE')


#Ejemplos de técnicos
jair_telequinox     = Tecnico('Ttel01','JAIR', 'telequinox')
osman_telequinox    = Tecnico('Ttel02','OSMAN', 'telequinox')
brayan_telequinox   = Tecnico('Ttel03','BRAYAN', 'telequinox')
cristian_PDI        = Tecnico('Tpdi01','CRISTIAN', 'PDI')
david_PDI           = Tecnico('Tpdi02','DAVID', 'PDI')
luis_lavado         = Tecnico('Tlav01','LUIS', 'lavado')
kevin_lavado        = Tecnico('Tlav02','KEVIN', 'lavado')
jesus_pintura       = Tecnico('Tpin01','JESUS', 'pintura')
daniel_pintura      = Tecnico('Tpin02','DANIEL', 'pintura')
victor_calidad      = Tecnico('Tcal01','VICTOR', 'calidad')


#ejemplos de objetos vehículos únicos.
VHAUK0001=Vehiculo(id_chasis = 'AUK0001',modelo='AUMARK',pedido='quito06')
VHQAS0002=Vehiculo(id_chasis = 'QAS0002',modelo='QASHQAI',pedido='quito06')
VHQAS0003=Vehiculo(id_chasis = 'QAS0003',modelo='QASHQAI',pedido='quito06')
VHXTR0004=Vehiculo(id_chasis = 'XTR0004',modelo='XTRAIL',pedido='quito06')
VHXTR0005=Vehiculo(id_chasis = 'XTR0005',modelo='XTRAIL',pedido='quito06')
VHXTR0006=Vehiculo(id_chasis = 'XTR0006',modelo='XTRAIL',pedido='quito06')
VHXTR0007=Vehiculo(id_chasis = 'XTR0007',modelo='XTRAIL',pedido='quito06')
VHXTR0008=Vehiculo(id_chasis = 'XTR0008',modelo='XTRAIL',pedido='quito06')
VHKOL0009=Vehiculo(id_chasis = 'KOL0009',modelo='KOLEOS',pedido='quito06')
VHBJ40010=Vehiculo(id_chasis = 'BJ40010',modelo='BJ40',pedido='quito06')
VHX350011=Vehiculo(id_chasis = 'X350011',modelo='X35',pedido='quito06')
VHX350012=Vehiculo(id_chasis = 'X350012',modelo='X35',pedido='quito06')
VHVER0013=Vehiculo(id_chasis = 'VER0013',modelo='VERSA',pedido='quito06')
VHKWI0014=Vehiculo(id_chasis = 'KIW0014',modelo='KWID',pedido='quito06')
VHTUN0015=Vehiculo(id_chasis = 'TUN0015',modelo='TUNLAND',pedido='quito06')
VHCAP0016=Vehiculo(id_chasis = 'CAP0016',modelo='CAPTUR',pedido='quito06')
VHVER0017=Vehiculo(id_chasis = 'VER0017',modelo='VERSA',pedido='quito06')
VHTOA0018=Vehiculo(id_chasis = 'TOA0018',modelo='TOANO',pedido='quito06')
VHTOA0019=Vehiculo(id_chasis = 'TOA0019',modelo='TOANO',pedido='quito06')
VHVIE0020=Vehiculo(id_chasis = 'VIE0020',modelo='VIEW',pedido='quito06')
VHKIC0021=Vehiculo(id_chasis = 'KIC0021',modelo='KICKS',pedido='quito06')
VHKIC0022=Vehiculo(id_chasis = 'KIC0022',modelo='KICKS',pedido='quito06')
VHCOL0023=Vehiculo(id_chasis = 'COL0023',modelo='COOLRAY',pedido='quito06')
VHAZK0024=Vehiculo(id_chasis = 'AZK0024',modelo='AZKARRA',pedido='quito06')
VHX550025=Vehiculo(id_chasis = 'X550025',modelo='X55',pedido='quito06')
VHX550026=Vehiculo(id_chasis = 'X550026',modelo='X55',pedido='quito06')

#EJEMPLO DE PEDIDO
pedido_quito06 = Pedido(
                        id_pedido='p_qui06',
                        plazo_entrega = 5000,
                        vehiculos =[VHAUK0001,
                                    VHQAS0002,
                                    VHQAS0003,
                                    VHXTR0004,
                                    VHXTR0005,
                                    VHXTR0006,
                                    VHXTR0007,
                                    VHXTR0008,
                                    VHKOL0009,
                                    VHBJ40010,
                                    VHX350011,
                                    VHX350012,
                                    VHVER0013,
                                    VHKWI0014,
                                    VHTUN0015,
                                    VHCAP0016,
                                    VHVER0017,
                                    VHTOA0018,
                                    VHTOA0019,
                                    VHVIE0020,
                                    VHKIC0021,
                                    VHKIC0022,
                                    VHCOL0023,
                                    VHAZK0024,
                                    VHX550025,
                                    VHX550026,
                                    ],
                        estado ="PENDIENTE"
                        )

programa_inmediato(pedido_quito06, personal, 4000)
horizonte_calculado = calcular_horizonte(pedido_quito06)

print(f"el horizonte es {calcular_horizonte(pedido_quito06)}")