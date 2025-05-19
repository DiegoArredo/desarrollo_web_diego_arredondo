from sqlalchemy import create_engine, Column, Integer, BigInteger, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship,Session

from sqlalchemy.ext.automap import automap_base
import json

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306

DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)

# Base = declarative_base()
Base = automap_base()
Base.prepare(engine, reflect=True)

print("Tablas reflejadas:")
for table_name in Base.classes.keys():
    print(table_name)

Region = Base.classes.region
Comuna = Base.classes.comuna
Actividad = Base.classes.actividad
Foto = Base.classes.foto
ContactarPor = Base.classes.contactar_por
ActividadTema = Base.classes.actividad_tema

session = Session(engine)
regiones = session.query(Region).all()
for r in regiones:
    print(f"Region: {r.nombre}")

# Ejemplo: obtener comunas de la primera región
if regiones:
    primera_region = regiones[0]
    # Nota: las relaciones no siempre se reflejan automáticamente,
    # puede que necesites acceder a las tablas con consultas explícitas
    comunas = session.query(Comuna).filter(Comuna.region_id == primera_region.id).all()
    for c in comunas:
        print(f"Comuna: {c.nombre}")

# --- Models ---

# class Actividad(Base):
#     __tablename__ = 'actividad'

#     id = Column(BigInteger, primary_key=True, autoincrement=True)
#     sector = Column(String(100), nullable=True)
#     email = Column(String(100), nullable=False)
#     nombre = Column(String(200), nullable=False)
#     celular = Column(String(15), nullable=True)
#     dia_hora_inicio = Column(String(100), nullable=False)
#     dia_hora_termino = Column(String(100), nullable=True)
#     descripcion = Column(String(500), nullable=False)
#     comuna_id = relationship("Comuna", back_populates="actividades", cascade="all, delete")

# class Comuna(Base):
#     __tablename__ = 'comuna'

#     id = Column(BigInteger, primary_key=True, autoincrement=True)
#     nombre = Column(String(200), nullable=False)
#     actividades = relationship("Actividad", back_populates="comuna_id", cascade="all, delete")
#     region_id = relationship("Region", back_populates="comunas", cascade="all, delete")

# class Region(Base):
#     __tablename__ = 'region'

#     id = Column(BigInteger, primary_key=True, autoincrement=True)
#     nombre = Column(String(200), nullable=False)
#     comunas = relationship("Comuna", back_populates="region_id", cascade="all, delete")

# class TemaActividad(Base):
    __tablename__ = 'actividad_tema'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    tema = Column(String(200), nullable=False)
    actividades = relationship("Actividad", back_populates="tema_id", cascade="all, delete")
# --- Database Functions ---

# def get_user_by_id(id):
#     session = SessionLocal()
#     user = session.query(Usuario).filter_by(id=id).first()
#     session.close()
#     return user

# def get_user_by_email(email):
#     session = SessionLocal()
#     user = session.query(Usuario).filter_by(email=email).first()
#     session.close()
#     return user

# def get_user_by_username(username):
#     session = SessionLocal()
#     user = session.query(Usuario).filter_by(username=username).first()
#     session.close()
#     return user

# def create_user(username, password, email):
#     session = SessionLocal()
#     new_user = Usuario(username=username, password=password, email=email)
#     session.add(new_user)
#     session.commit()
#     session.close()

# def get_confessions(page_size):
#     session = SessionLocal()
#     confesiones = session.query(Confesion).limit(page_size).all()
#     session.close()
#     return confesiones

# def create_confession(conf_title, conf_text, conf_img, user_id):
#     session = SessionLocal()
#     new_confession = Confesion(conf_title=conf_title,conf_text=conf_text, conf_img=conf_img, user_id=user_id)
#     session.add(new_confession)
#     session.commit()
#     session.close()

# def change_profile_picture(username, new_img):
#     session = SessionLocal()
#     user = session.query(Usuario).filter_by(username=username).first()
#     if user:
#         user.profile_image = new_img
#         session.commit()
#     session.close()

# def get_profile_picture(username):
#     session = SessionLocal()
#     user = session.query(Usuario).filter_by(username=username).first()
#     if user:
#         profile_image = user.profile_image
#     else:
#         profile_image = None
#     session.close()
#     return profile_image

# def register_user(username, password, email):
#     if get_user_by_email(email) is not None:
#         return False, "El correo ya esta en uso."
    
#     if get_user_by_username(username) is not None:
#         return False, "El nombre de usuario esta en uso."
    
#     create_user(username, password, email)
#     return True, None

# def login_user(username, password):
#     a_user = get_user_by_username(username)
#     if a_user is None:
#         return False, "Usuario o contraseña incorrectos."
    
#     if a_user.password != password:
#         return False, "Usuario o contraseña incorrectos."
    
#     return True, None
