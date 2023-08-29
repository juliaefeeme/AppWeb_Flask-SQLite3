# clases y modelos que vamos a utilizar

import db #para acceder a info del fichero
from sqlalchemy import Column, Integer, String, Boolean

class Tarea(db.Base):
    __tablename__="tarea" #decirle a esta clase cómo se va a llamar cuando pase a ser tabla
    id= Column(Integer, primary_key=True) #tipo de cada columna y la PK se convierte el serial (autoincrementa)
    contenido = Column(String(200), nullable=False)
    hecha= Column(Boolean)

    def __init__(self, contenido, hecha):
        self.contenido=contenido
        self.hecha=hecha

    def __str__(self):
        return "Tarea({}:{},{})".format(self.id, self.contenido, self.hecha)