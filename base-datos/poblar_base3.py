import json

from configuracion import SessionLocal
from crear_base_entidades import Carrera, Profesor

RUTA_DATOS = "data/datos_universidad/datos/profesores.json"

session = SessionLocal()

with open(RUTA_DATOS, "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

insertados = 0
for item in datos:
    carrera = session.query(Carrera).filter_by(nombre=item["carrera"]).first()
    if not carrera:
        print(f"Carrera no encontrada: {item['carrera']}")
        continue

    existente = session.query(Profesor).filter_by(correo=item["correo"]).first()
    if existente:
        continue

    profesor = Profesor(
        id=item.get("id"),
        nombres=item["nombres"],
        apellidos=item["apellidos"],
        correo=item["correo"],
        especialidad=item["especialidad"],
        carrera=carrera,
    )
    session.add(profesor)
    insertados += 1

session.commit()
session.close()

print(f"Profesores insertados: {insertados}")
