from sqlalchemy import create_engine, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base, relationship,Session, mapped_column
import enum


DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306

DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


# --- Models ---

class ContactarPorNombre(enum.Enum):
    whatsapp = "whatsapp"
    telegram = "telegram"
    X = "X"
    instagram = "instagram"
    tiktok = "tiktok"
    otra = "otra"

class ActividadTemaTema(enum.Enum):
    música = "música"
    deporte = "deporte"
    ciencias = "ciencias"
    religión = "religión"
    política = "política"
    tecnología = "tecnología"
    juegos = "juegos"
    baile = "baile"
    comida = "comida"
    otro = "otro"


class Region(Base):
    __tablename__ = "region"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre = mapped_column(String(200), nullable=False)

    comunas = relationship("Comuna", back_populates="region")


class Comuna(Base):
    __tablename__ = "comuna"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre = mapped_column(String(200), nullable=False)
    region_id = mapped_column(Integer, ForeignKey("region.id"), nullable=False, index=True)

    region = relationship("Region", back_populates="comunas")
    actividades = relationship("Actividad", back_populates="comuna")


class Actividad(Base):
    __tablename__ = "actividad"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    comuna_id = mapped_column(Integer, ForeignKey("comuna.id"), nullable=False, index=True)
    sector = mapped_column(String(100), nullable=True)
    nombre = mapped_column(String(200), nullable=False)
    email = mapped_column(String(100), nullable=False)
    celular = mapped_column(String(15), nullable=True)
    dia_hora_inicio = mapped_column(DateTime, nullable=False)
    dia_hora_termino = mapped_column(DateTime, nullable=True)
    descripcion = mapped_column(String(500), nullable=True)

    comuna = relationship("Comuna", back_populates="actividades")
    fotos = relationship("Foto", back_populates="actividad")
    contactar_por = relationship("ContactarPor", back_populates="actividad")
    actividad_temas = relationship("ActividadTema", back_populates="actividad")
    comentarios = relationship("Comentario", back_populates="actividad")


class Foto(Base):
    __tablename__ = "foto"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    ruta_archivo = mapped_column(String(300), nullable=False)
    nombre_archivo = mapped_column(String(300), nullable=False)
    actividad_id = mapped_column(Integer, ForeignKey("actividad.id"), nullable=False, index=True)

    actividad = relationship("Actividad", back_populates="fotos")



class ContactarPor(Base):
    __tablename__ = "contactar_por"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre = mapped_column(Enum(ContactarPorNombre), nullable=False)
    identificador = mapped_column(String(150), nullable=False)
    actividad_id = mapped_column(Integer, ForeignKey("actividad.id"), nullable=False, index=True)

    actividad = relationship("Actividad", back_populates="contactar_por")




class ActividadTema(Base):
    __tablename__ = "actividad_tema"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    tema = mapped_column(Enum(ActividadTemaTema), nullable=False)
    glosa_otro = mapped_column(String(15), nullable=True)
    actividad_id = mapped_column(Integer, ForeignKey("actividad.id"), nullable=False, index=True)

    actividad = relationship("Actividad", back_populates="actividad_temas")


class Comentario(Base):
    __tablename__ = "comentario"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre = mapped_column(String(80), nullable=False)
    texto = mapped_column(String(300), nullable=False)
    fecha = mapped_column(DateTime, nullable=False)
    actividad_id = mapped_column(Integer, ForeignKey("actividad.id"), nullable=False, index=True)

    actividad = relationship("Actividad", back_populates="comentarios")
    Actividad.comentarios = relationship("Comentario", back_populates="actividad")

# --- Database Functions ---

def get_all_actividades(page_size):
    session = SessionLocal()
    actividades = session.query(Actividad).limit(page_size).all()
    session.close()
    return actividades

def get_actividad_by_id(id):
    session = SessionLocal()
    actividad = session.query(Actividad).filter_by(id=id).first()
    session.close()
    return actividad

def get_all_regiones():
    session = SessionLocal()
    regiones = session.query(Region).all()
    session.close()
    return regiones

def get_region_por_id(id):
    session = SessionLocal()
    region = session.query(Region).filter_by(id=id).first()
    session.close()
    return region

def get_all_comunas():
    session = SessionLocal()
    comunas = session.query(Comuna).all()
    session.close()
    return comunas

def get_comuna_por_id(id):
    session = SessionLocal()
    comuna = session.query(Comuna).filter_by(id=id).first()
    session.close()
    return comuna


def get_comuna_por_region_id(region_id):
    session = SessionLocal()
    comunas = session.query(Comuna).filter_by(region_id=region_id).all()
    session.close()
    return comunas

def add_actividad(comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion):
    session = SessionLocal()
    new_actividad = Actividad(
        comuna_id=comuna_id,
        sector=sector,
        nombre=nombre,
        email=email,
        celular=celular,
        dia_hora_inicio=dia_hora_inicio,
        dia_hora_termino=dia_hora_termino,
        descripcion=descripcion
    )
    session.add(new_actividad)
    session.commit()
    session.refresh(new_actividad)
    id = new_actividad.id
    session.close()
    return id

def get_fotos_por_actividad_id(actividad_id):
    session = SessionLocal()
    fotos = session.query(Foto).filter_by(actividad_id=actividad_id).all()
    session.close()
    return fotos

def get_first_foto_por_actividad_id(actividad_id):
    session = SessionLocal()
    foto = session.query(Foto).filter_by(actividad_id=actividad_id).first()
    session.close()
    return foto

def get_temas_por_actividad_id(actividad_id):
    session = SessionLocal()
    temas = session.query(ActividadTema).filter_by(actividad_id=actividad_id).all()
    session.close()
    return temas

def get_all_temas():
    session = SessionLocal()
    temas = session.query(ActividadTema).all()
    session.close()
    return temas

def get_contactar_por_actividad_id(actividad_id):
    session = SessionLocal()
    contactar_por = session.query(ContactarPor).filter_by(actividad_id=actividad_id).all()
    session.close()
    return contactar_por

def add_contactar_por(actividad_id, nombre, identificador):
    session = SessionLocal()
    new_contactar_por = ContactarPor(
        actividad_id=actividad_id,
        nombre=nombre,
        identificador=identificador
    )
    session.add(new_contactar_por)
    session.commit()
    session.refresh(new_contactar_por)
    id = new_contactar_por.id
    session.close()
    return id

def add_foto(actividad_id, ruta_archivo, nombre_archivo):
    session = SessionLocal()
    new_foto = Foto(
        actividad_id=actividad_id,
        ruta_archivo=ruta_archivo,
        nombre_archivo=nombre_archivo
    )
    session.add(new_foto)
    session.commit()
    session.refresh(new_foto)
    id = new_foto.id
    session.close()
    return id

def add_actividad_tema(actividad_id, tema, glosa_otro=None):
    session = SessionLocal()
    new_actividad_tema = ActividadTema(
        actividad_id=actividad_id,
        tema=tema,
        glosa_otro=glosa_otro
    )
    session.add(new_actividad_tema)
    session.commit()
    session.refresh(new_actividad_tema)
    id = new_actividad_tema.id
    session.close()
    return id

def get_all_actividades_paginadas(limit=5, offset=0):
    session = SessionLocal()
    actividades = session.query(Actividad).order_by(Actividad.id).limit(limit).offset(offset).all()
    session.close()
    return actividades
# add_actividad(10304, "sector", "nombre", "email", "celular", "2023-10-01 10:00:00", "2023-10-01 12:00:00", "descripcion")


#Queries para obtener actividades por diferentes criterios

def get_actividades_por_tema(tema):
    session = SessionLocal()
    actividades = session.query(Actividad).join(Actividad.actividad_temas).filter(ActividadTema.tema == tema).all()
    session.close()
    return actividades


# def get_actividades_por_mes_en_la_mañana(mes):
#     session = SessionLocal()
#     actividades = session.query(Actividad).filter(Actividad.dia_hora_inicio == mes, Actividad.dia_hora_inicio < 12).all()
#     session.close()
#     return actividades

# def get_actividades_por_mes_en_el_mediodia(mes):
#     session = SessionLocal()
#     actividades = session.query(Actividad).filter(Actividad.dia_hora_inicio.month == mes, Actividad.dia_hora_inicio.hour >= 12, Actividad.dia_hora_inicio.hour < 18).all()
#     session.close()
#     return actividades

# def get_actividades_por_mes_en_la_noche(mes):
#     session = SessionLocal()
#     actividades = session.query(Actividad).filter(Actividad.dia_hora_inicio.month == mes, Actividad.dia_hora_inicio.hour >= 18).all()
#     session.close()
#     return actividades
 
#Query para añadir comentarios a las actividades
def add_comentario(actividad_id, nombre, texto, fecha):
    session = SessionLocal()
    new_comentario = Comentario(
        actividad_id=actividad_id,
        nombre=nombre,
        texto=texto,
        fecha=fecha
    )
    session.add(new_comentario)
    session.commit()
    session.refresh(new_comentario)
    id = new_comentario.id
    session.close()
    return id

# Query para obtener comentarios por actividad_id
def get_comentarios_por_actividad_id(actividad_id):
    session = SessionLocal()
    comentarios = session.query(Comentario).filter_by(actividad_id=actividad_id).all()
    session.close()
    return comentarios

#añadir actividad

for r in get_all_regiones():
    print(f"Region: {r.nombre}")
# Ejemplo: obtener todas las regiones



for r in get_comuna_por_region_id(1):
    print(f"Id: {r.id}, Comuna: {r.nombre}")
# Ejemplo: obtener todas las comunas de la región con id 1

