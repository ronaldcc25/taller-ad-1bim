import json

from configuracion import SessionLocal
from crear_base_entidades import Facultad

RUTA_DATOS = "data/datos_universidad/datos/facultades.json"

session = SessionLocal()

with open(RUTA_DATOS, "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

insertados = 0
for item in datos:
    existente = session.query(Facultad).filter_by(nombre=item["nombre"]).first()
    if existente:
        continue

    facultad = Facultad(
        id=item.get("id"),
        nombre=item["nombre"],
        ubicacion=item["ubicacion"],
        decano=item["decano"],
    )
    session.add(facultad)
    insertados += 1

session.commit()
session.close()

print(f"Facultades insertadas: {insertados}")
