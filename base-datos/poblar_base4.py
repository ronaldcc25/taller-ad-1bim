import json
from datetime import date

from configuracion import SessionLocal
from crear_base_entidades import Profesor, RecursoAcademico

RUTA_DATOS = "data/datos_universidad/datos/recursos_academicos.json"

session = SessionLocal()

with open(RUTA_DATOS, "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

insertados = 0
for item in datos:
    nombre_completo = item["profesor"].strip()
    partes = nombre_completo.split()
    nombres = " ".join(partes[:-1])
    apellidos = partes[-1]

    profesor = (
        session.query(Profesor).filter_by(nombres=nombres, apellidos=apellidos).first()
    )
    if not profesor:
        print(f"Profesor no encontrado: {nombre_completo}")
        continue

    existente = session.query(RecursoAcademico).filter_by(titulo=item["titulo"]).first()
    if existente:
        continue

    recurso = RecursoAcademico(
        id=item.get("id"),
        titulo=item["titulo"],
        fecha_publicacion=date.fromisoformat(item["fecha_publicacion"]),
        tipo=item["tipo"],
        url=item["url"],
        profesor=profesor,
    )
    session.add(recurso)
    insertados += 1

session.commit()
session.close()

print(f"Recursos académicos insertados: {insertados}")
