from configuracion import SessionLocal
from crear_base_entidades import RecursoAcademico
from sqlalchemy import and_

session = SessionLocal()

recursos = (
    session.query(RecursoAcademico)
    .filter(
        and_(
            RecursoAcademico.tipo == "Libro",
            RecursoAcademico.titulo.ilike("%SQL%"),
        )
    )
    .all()
)

for recurso in recursos:
    print(f"{recurso.id} | {recurso.titulo} | {recurso.tipo} | {recurso.url}")

session.close()
