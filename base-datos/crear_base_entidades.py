from configuracion import get_engine
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Facultad(Base):
    __tablename__ = "facultad"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), nullable=False, unique=True)
    ubicacion = Column(String(120), nullable=False)
    decano = Column(String(120), nullable=False)

    carreras = relationship(
        "Carrera", back_populates="facultad", cascade="all, delete-orphan"
    )


class Carrera(Base):
    __tablename__ = "carrera"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(160), nullable=False, unique=True)
    codigo = Column(String(20), nullable=False, unique=True)
    facultad_id = Column(Integer, ForeignKey("facultad.id"), nullable=False)

    facultad = relationship("Facultad", back_populates="carreras")
    profesores = relationship(
        "Profesor", back_populates="carrera", cascade="all, delete-orphan"
    )


class Profesor(Base):
    __tablename__ = "profesor"

    id = Column(Integer, primary_key=True)
    nombres = Column(String(80), nullable=False)
    apellidos = Column(String(80), nullable=False)
    correo = Column(String(160), nullable=False, unique=True)
    especialidad = Column(String(160), nullable=False)
    carrera_id = Column(Integer, ForeignKey("carrera.id"), nullable=False)

    carrera = relationship("Carrera", back_populates="profesores")
    recursos = relationship(
        "RecursoAcademico", back_populates="profesor", cascade="all, delete-orphan"
    )


class RecursoAcademico(Base):
    __tablename__ = "recurso_academico"

    id = Column(Integer, primary_key=True)
    titulo = Column(String(200), nullable=False)
    fecha_publicacion = Column(Date, nullable=False)
    tipo = Column(String(40), nullable=False)
    url = Column(String(300), nullable=False)
    profesor_id = Column(Integer, ForeignKey("profesor.id"), nullable=False)

    profesor = relationship("Profesor", back_populates="recursos")


if __name__ == "__main__":
    engine = get_engine()
    Base.metadata.create_all(engine)
