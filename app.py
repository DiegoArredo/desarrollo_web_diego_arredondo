from flask import Flask, request, render_template, redirect, url_for, session, flash
from database import db2
from utils.validations import *
import os
import uuid
import hashlib
import filetype
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)
app.debug = True
app.secret_key = "secret_key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

@app.route('/',methods=['GET'])
def home():
    actividades = []
    PAGE_SIZE= 5
    actividades_db = db2.get_all_actividades(PAGE_SIZE)
    for actividad in actividades_db:
        comuna = db2.get_comuna_por_id(actividad.comuna_id)
        foto = db2.get_first_foto_por_actividad_id(actividad.id)
        temas = db2.get_temas_por_actividad_id(actividad.id)
        if foto:
            foto_path = url_for('static', filename=f"uploads/{foto.ruta_archivo}")
            foto = {
                'id': foto.id,
                'ruta': foto_path,
                'nombre': foto.nombre_archivo
            }
        actividades.append({
            'id': actividad.id,
            'nombre': actividad.nombre,
            'sector': actividad.sector,
            'descripcion': actividad.descripcion,
            'fecha_inicio': actividad.dia_hora_inicio,
            'fecha_termino': actividad.dia_hora_termino,
            'comuna_id': actividad.comuna_id,
            'comuna': comuna.nombre if comuna else None,
            'temas':    temas,
            'foto': foto if foto else None
        })
    print(actividades)
    return render_template('main/main.html', data = actividades)

@app.route("/actividades", methods=['GET'])
def actividades():
    PAGE_SIZE= 5
    page = request.args.get('page', 1, type=int)
    total_actividades = len(db2.get_all_actividades(1000))
    total_pages = (total_actividades // 5) + (1 if total_actividades % 5 > 0 else 0)
    offset = (page - 1) * PAGE_SIZE
    actividades_db = db2.get_all_actividades_paginadas(limit=PAGE_SIZE, offset=offset)
    actividades = []
    for actividad in actividades_db:
        comuna = db2.get_comuna_por_id(actividad.comuna_id)
        fotos = db2.get_fotos_por_actividad_id(actividad.id)
        
        temas = db2.get_temas_por_actividad_id(actividad.id)
        actividades.append({
            'id': actividad.id,
            'nombre': actividad.nombre,
            'sector': actividad.sector,
            'descripcion': actividad.descripcion,
            'fecha_inicio': actividad.dia_hora_inicio,
            'fecha_termino': actividad.dia_hora_termino,
            'comuna_id': actividad.comuna_id,
            'comuna': comuna.nombre if comuna else None,
            'temas':    temas,
            'foto': len(fotos)
        })
    print(actividades)
    return render_template('list_actividad.html', data=actividades,  page=page, total_paginas=total_pages)

@app.route("/add-actividad", methods=['GET', 'POST'])
def add_actividad():
    errores = []
    mensajes = []
    if request.method == 'POST':
        print("POST")
        print(request.form.get('comuna'))
        print(request.form.get('region'))
        print(request.form.get('sector'))
        print(request.form.get('nombre'))
        print(request.form.get('email'))
        print(request.form.get('numero'))
        print(request.form.get('fecha_inicio'))
        print(request.form.get('fecha_fin'))
        print(request.form.get('descripcion'))
        print(request.form.get('whatsapp-id'))
        print(request.form.get('telegram-id'))
        print(request.form.get('instagram-id'))
        print(request.form.get('x-id'))
        print(request.form.get('tiktok-id'))
        print(request.form.get('tema'))
        print(request.form.get('glosa_otro'))
        print(request.files.getlist('foto'))
    
        
        # Obtener los datos del formulario
        comuna_id = request.form.get('comuna')
        region_id = request.form.get('region')
        sector = request.form.get('sector')
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        celular = request.form.get('numero')
        dia_hora_inicio = request.form.get('fecha_inicio')
        dia_hora_termino = request.form.get('fecha_fin')
        descripcion = request.form.get('descripcion')
        whatsapp = request.form.get('whatsapp-id')
        telegram = request.form.get('telegram-id')
        instagram = request.form.get('instagram-id')
        x = request.form.get('x-id')
        tiktok = request.form.get('tiktok-id')
        tema = request.form.get('tema')
        glosa_otro = request.form.get('glosa_otro')

    
        # Obtener los archivos subidos
        print("Obteniendo archivos")
        files = request.files.getlist('foto')
        


        # Validar los datos recibidos
        print("Validando datos")
        if not validate_region(region_id):
            errores.append("Región inválida")
        if not validate_comuna(comuna_id):
            errores.append("Comuna inválida")
        if not validate_sector(sector):
            errores.append("Sector inválido")
        if not validate_nombre(nombre):
            errores.append("Nombre inválido")
        if not validate_email(email):
            errores.append("Email inválido")
        if not validate_telefono(celular):
            errores.append("Celular inválido")
        if not validar_fecha_inicio(dia_hora_inicio):
            errores.append("Fecha inicio inválida")
        if not validar_fecha_fin(dia_hora_termino, dia_hora_inicio):
            errores.append("Fecha término inválida")
        if not validate_tema(tema, glosa_otro):
            errores.append("Tema inválido")
        if not validar_files(files):
            errores.append("Archivos inválidos")
        if files:
            for file in files:
                if not validate_img(file):
                    errores.append("Archivo inválido")


        if not errores:
            # Guardar la actividad en la base de datos
            actividad_id = db2.add_actividad(
                comuna_id=comuna_id,
                sector=sector,
                nombre=nombre,
                email=email,
                celular=celular,
                dia_hora_inicio=dia_hora_inicio,
                dia_hora_termino=dia_hora_termino,
                descripcion=descripcion
            )
            print("Actividad guardada")
            print(actividad_id)
            if not actividad_id:
                errores.append("Error al guardar la actividad")
                
            # Guardar los temas
            if tema == "otro":
                if not db2.add_actividad_tema(actividad_id, tema, glosa_otro):
                    errores.append("Error al guardar el tema")
                   
            else:
                if not db2.add_actividad_tema(actividad_id, tema):
                    errores.append("Error al guardar el tema")
                    
            

            # Guardar los archivos subidos
            for file in files:
                _filename = hashlib.sha256(
                    secure_filename(file.filename).encode("utf-8")
                    ).hexdigest()
                _extension = filetype.guess(file).extension
                img_filename = f"{_filename}_{str(uuid.uuid4())}.{_extension}"
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))

                if not db2.add_foto(actividad_id, img_filename, _filename):
                    errores.append("Error al guardar la foto")
                    return render_template('form_actividad.html', errores=errores ,mensajes=mensajes)

            # Guardar el contacto
            if whatsapp:
                db2.add_contactar_por(actividad_id, "whatsapp", whatsapp)
            if telegram:
                db2.add_contactar_por(actividad_id, "telegram", telegram)
            if instagram:
                db2.add_contactar_por(actividad_id, "instagram", instagram)
            if x:
                db2.add_contactar_por(actividad_id, "x", x)
            if tiktok:
                db2.add_contactar_por(actividad_id, "tiktok", tiktok)

            mensajes.append("Actividad creada con éxito")        
            flash('¡Actividad agregada correctamente!', 'success')
            return redirect(url_for('home'),)
    return render_template('form_actividad.html', errores=errores ,mensajes=mensajes)

@app.route("/actividad/<int:id>", methods=['GET'])
def actividad(id):
    actividad_db = db2.get_actividad_by_id(id)
    comuna = db2.get_comuna_por_id(actividad_db.comuna_id)
    fotos_db = db2.get_fotos_por_actividad_id(actividad_db.id)
    temas = db2.get_temas_por_actividad_id(actividad_db.id)
    fotos = []
    for foto in fotos_db:
        if foto:
            foto_path = url_for('static', filename=f"uploads/{foto.ruta_archivo}")
            fotos.append({
                'id': foto.id,
                'ruta': foto_path,
                'nombre': foto.nombre_archivo
            })
    actividad = {
        'id': actividad_db.id,
        'nombre': actividad_db.nombre,
        'sector': actividad_db.sector,
        'descripcion': actividad_db.descripcion,
        'fecha_inicio': actividad_db.dia_hora_inicio,
        'fecha_termino': actividad_db.dia_hora_termino,
        'comuna_id': actividad_db.comuna_id,
        'comuna': comuna.nombre if comuna else None,
        'temas': temas,
        'fotos': fotos
    }
    return render_template('actividad.html', actividad = actividad)

@app.route("/estadisticas", methods=['GET'])
def estadisticas():

    return render_template('estadisticas.html')

if __name__ == "__main__":
    app.run(debug=True)
