from configuracion import SessionLocal
from crear_base_entidades import Profesor

session = SessionLocal()

profesores = session.query(Profesor).order_by(Profesor.apellidos.asc()).all()

for profesor in profesores:
    print(
        f"{profesor.id} | {profesor.nombres} {profesor.apellidos} | {profesor.correo}"
    )

session.close()
