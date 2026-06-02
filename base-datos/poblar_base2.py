import json

from configuracion import SessionLocal
from crear_base_entidades import Carrera, Facultad

RUTA_DATOS = "data/datos_universidad/datos/carreras.json"

session = SessionLocal()

with open(RUTA_DATOS, "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

insertados = 0
for item in datos:
    facultad = session.query(Facultad).filter_by(nombre=item["facultad"]).first()
    if not facultad:
        print(f"Facultad no encontrada: {item['facultad']}")
        continue

    existente = session.query(Carrera).filter_by(nombre=item["nombre"]).first()
    if existente:
        continue

    carrera = Carrera(
        id=item.get("id"),
        nombre=item["nombre"],
        codigo=item["codigo"],
        facultad=facultad,
    )
    session.add(carrera)
    insertados += 1

session.commit()
session.close()

print(f"Carreras insertadas: {insertados}")
