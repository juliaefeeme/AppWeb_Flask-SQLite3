# gestionar bbdd no desde sqlite sino desde el orm alchemy
# configuracion
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# El engine permite a sqlalchemy comunicarse con la BBDD
engine= create_engine("sqlite:///database/tareas.db", connect_args={"check_same_thread":False}) #conexion a mi bbdd en lenguaje sqlite+ubicacion
# Con el segundo parametro advertimos de que puede haber más de un hilo de conexion a la página web
# Advertencia: crear el engine no conecta con la base de datos

# Ahora creamos sesión para realizar transacciones dentro de la bbdd
Session = sessionmaker(bind=engine) #esta sesion va a hacer cosas sobre la bbdd
session=Session() #activar la sesion anterior, que es nuestro punto de entrada

#necesitamos vincular este fichero con el models


Base=declarative_base() #coge las clases (que hayamos marcado) y las mapea para crear estructura de tabla