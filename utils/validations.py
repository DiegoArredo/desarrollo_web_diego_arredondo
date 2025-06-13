import re
import filetype

import re
from datetime import datetime

def validate_region(region):
  
    return bool(region)

def validate_comuna(comuna):
    return bool(comuna)

def validate_sector(sector):
  
    if sector is None:
        return False
    return len(sector.strip()) <= 100

def validate_nombre(nombre):
  
    if not nombre:
        return False
    return len(nombre.strip()) <= 200

def validate_email(email):
    if not email:
        return False
    email = email.strip()
    if len(email) > 100:
        return False
    # Regex JS: /^[\w.]+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/
    pattern = r'^[\w.]+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$'
    return re.match(pattern, email) is not None

def validate_telefono(telefono):
    telefono = telefono.strip()
    if len(telefono) < 8:
        return False
    if not telefono.isdigit():
        return False
    return True

def validate_contactar(contacto):
    if not contacto:
        return False
    length = len(contacto.strip())
    return 4 < length <= 50

def validar_fecha_inicio(fecha_inicio):

    return bool(fecha_inicio)

def validar_fecha_fin(fecha_fin, fecha_inicio):
    if not fecha_fin or not fecha_inicio:
        return False
    try:
        f_inicio = datetime.fromisoformat(fecha_inicio)
        f_fin = datetime.fromisoformat(fecha_fin)
        return f_fin >= f_inicio
    except ValueError:
        return False

def validate_tema(tema, glosa_otro=None):
    if not tema:
        return False
    if tema == "otro":
        if not glosa_otro:
            return False
        length = len(glosa_otro.strip())
        return 2 <= length <= 15
    return True

def validar_files(files):
    
    if not files:
        return False
    length = len(files)
    return 0 < length <= 5

def validate_img(file):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    # check if a file was submitted
    if file is None:
        return False

    # check if the browser submitted an empty file
    if file.filename == "":
        return False
    
    # check file extension
    ftype_guess = filetype.guess(file)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    return True


def validate_nombre_comentario(nombre_comentario):
    if not nombre_comentario:
        return False
    length = len(nombre_comentario.strip())
    if (not 3 <= length <= 80):
        return False
    return True
def validate_texto_comentario(comentario):
    if not comentario:
        return False
    length = len(comentario.strip())
    if (not 5 <= length <= 1000):
        return False
    return True