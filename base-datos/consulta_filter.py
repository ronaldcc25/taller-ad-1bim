from configuracion import SessionLocal
from crear_base_entidades import Carrera

session = SessionLocal()

carreras = session.query(Carrera).filter(Carrera.codigo == "ISW001").all()

for carrera in carreras:
    print(f"{carrera.id} | {carrera.nombre} | {carrera.codigo}")

session.close()
