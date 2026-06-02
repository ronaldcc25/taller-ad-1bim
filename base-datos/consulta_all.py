from configuracion import SessionLocal
from crear_base_entidades import Facultad

session = SessionLocal()

facultades = session.query(Facultad).all()

for facultad in facultades:
    print(
        f"{facultad.id} | {facultad.nombre} | {facultad.ubicacion} | {facultad.decano}"
    )

session.close()
