from configuracion import SessionLocal
from crear_base_entidades import Profesor
from sqlalchemy import or_

session = SessionLocal()

profesores = (
    session.query(Profesor)
    .filter(
        or_(
            Profesor.especialidad == "Bases de Datos",
            Profesor.especialidad == "Inteligencia Artificial",
        )
    )
    .all()
)

for profesor in profesores:
    print(
        f"{profesor.id} | {profesor.nombres} {profesor.apellidos} | {profesor.especialidad}"
    )

session.close()
