from flask import (
    Flask, 
    render_template,
    request,
    redirect,
    url_for
    )
import os
import database as db

# definimos las rutas del proyecto
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
# unir rutas de la carpeta src y templates y la ruta del proyecto de la linea anterior
template_dir = os.path.join(template_dir, 'src', 'templates')

# indicar que se busque el archivo index.html (cuando se ejecute la app)
app = Flask(__name__, template_folder=template_dir)

# rutas de la aplicacion
# @app.route('/'), el decorador vincula una funcion con una URL del sitio.
# En este caso '/' representa la ruta raíz o la homepage.
@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM usuarios")
    miResultado = cursor.fetchall()
    
    #Convertir los datos a diccionario
    insertarObjectos = [] 
    nombreDeColumnas = [columna[0] for columna in cursor.description]
    
    for unRegistro in miResultado:
        insertarObjectos.append(dict(zip(nombreDeColumnas, unRegistro)))
    
    # Cierra el cursor para liberar recursos de memoria.    
    cursor.close()
    
    return render_template('usuarios/listado.html', data=insertarObjectos)


# ruta a la pagina para agregar un usuario
@app.route('/usuarios/agregar')
def agregar():
    return render_template('usuarios/agregar.html')


#Ruta para guardar usuarios en la bdd
@app.route('/usuario', methods=['POST'])
def addUser():
    idUsuario = request.form['id']
    cuil = request.form['cuil']
    nombre = request.form['nombre']
    direccion = request.form['direccion']
    email = request.form['email']
    nivel_acc = request.form['nivel_acc']


    if idUsuario and cuil and nombre and direccion and email and nivel_acc:
        cursor = db.database.cursor()
        sql = "INSERT INTO usuarios (idUsuarios, cuil, nombre, direccion, email, nivelAcc) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (idUsuario, cuil, nombre, direccion, email, nivel_acc)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))


@app.route('/editar/<int:idUsuarios>', methods=['POST'])
def editar(idUsuarios):
    nombre = request.form['nombre']
    direccion = request.form['direccion']
    email = request.form['email']
    nivel_acc = request.form['nivel_acc']


    if nombre and direccion and email:
        cursor = db.database.cursor()
        sql = "UPDATE usuarios SET nombre = %s, direccion = %s, email = %s, nivelAcc = %s WHERE idUsuarios = %s"
        data = (nombre, direccion, email, nivel_acc, idUsuarios)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))


@app.route('/borrar/<int:id>')
def borrar(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM usuarios WHERE idUsuarios = %s"
    data = (id,) # SE DEBE AGREGAR LA COMA AL FINAL, SINO NO FUNCIONA, data DEBE SER UNA TUPLA
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))


########################### PROFESIONALES ##################################
@app.route('/profesionales/listado_profesionales')
def listado_profesionales():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM profesionales")
    miResultado = cursor.fetchall()
    
    #Convertir los datos a diccionario
    insertarObjectos = [] 
    nombreDeColumnas = [columna[0] for columna in cursor.description]
    
    for unRegistro in miResultado:
        insertarObjectos.append(dict(zip(nombreDeColumnas, unRegistro)))
    
    # Cierra el cursor para liberar recursos de memoria.    
    cursor.close()
    
    return render_template('profesionales/listado.html', data=insertarObjectos)


# ruta a la pagina para agregar un profesional
@app.route('/profesionales/agregar_profesional')
def agregar_profesional():
    return render_template('profesionales/agregar.html')


#Ruta para guardar profesionales en la bdd
@app.route('/profesional', methods=['POST'])
def addProfessional():
    idProfesional = request.form['id']
    cuil = request.form['cuil']
    nombre = request.form['nombre']
    matricula = request.form['matricula']
    direccion = request.form['direccion']
    nivel_acc = request.form['nivel_acc']
    especialidad = request.form['especialidad']


    if idProfesional and cuil and nombre and matricula and direccion and nivel_acc and especialidad:
        cursor = db.database.cursor()
        sql = "INSERT INTO profesionales (idProfesionales, cuil, nombre, matricula, direccion, nivelAcc, especialidad) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (idProfesional, cuil, nombre, matricula, direccion, nivel_acc, especialidad)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('listado_profesionales'))


@app.route('/editar_profesional/<int:idProfesionales>', methods=['POST'])
def editar_profesional(idProfesionales):
    nombre = request.form['nombre']
    direccion = request.form['direccion']
    especialidad = request.form['especialidad']


    if nombre and direccion and especialidad:
        cursor = db.database.cursor()
        sql = "UPDATE profesionales SET nombre = %s, direccion = %s, especialidad = %s WHERE idProfesionales = %s"
        data = (nombre, direccion, especialidad, idProfesionales)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('listado_profesionales'))


@app.route('/borra_profesional/<int:id>')
def borrar_profesional(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM profesionales WHERE idProfesionales = %s"
    data = (id,) # SE DEBE AGREGAR LA COMA AL FINAL, SINO NO FUNCIONA, data DEBE SER UNA TUPLA
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('listado_profesionales'))



########################### MASCOTAS ##################################
@app.route('/mascotas/listado_mascotas')
def listado_mascotas():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM mascotas")
    miResultado = cursor.fetchall()
    
    #Convertir los datos a diccionario
    insertarObjectos = [] 
    nombreDeColumnas = [columna[0] for columna in cursor.description]
    
    for unRegistro in miResultado:
        insertarObjectos.append(dict(zip(nombreDeColumnas, unRegistro)))
    
    # Cierra el cursor para liberar recursos de memoria.    
    cursor.close()
    
    return render_template('mascotas/listado.html', data=insertarObjectos)


# ruta a la pagina para agregar una mascota
@app.route('/mascotas/agregar_mascota')
def agregar_mascota():
    return render_template('mascotas/agregar.html')


#Ruta para guardar mascotas en la bdd
@app.route('/mascota', methods=['POST'])
def addPet():
    idMascota = request.form['id']
    nombre = request.form['nombre']
    raza = request.form['raza']
    edad = request.form['edad']
    vacunas = request.form['vacunas']
    duenio = request.form['duenio']


    if idMascota and nombre and raza and edad and vacunas and duenio:
        cursor = db.database.cursor()
        sql = "INSERT INTO mascotas (idMascotas, nombre, raza, edad, vacunas, Usuarios_idUsuarios) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (idMascota, nombre, raza, edad, vacunas, duenio)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('listado_mascotas'))


@app.route('/editar_mascota/<int:idMascotas>', methods=['POST'])
def editar_mascota(idMascotas):
    nombre = request.form['nombre']
    edad = request.form['edad']
    vacunas = request.form['vacunas']


    if nombre and edad and vacunas:
        cursor = db.database.cursor()
        sql = "UPDATE mascotas SET nombre = %s, edad = %s, vacunas = %s WHERE idMascotas = %s"
        data = (nombre, edad, vacunas, idMascotas)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('listado_mascotas'))


@app.route('/borra_mascotar/<int:id>')
def borrar_mascota(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM mascotas WHERE idMascotas = %s"
    data = (id,) # SE DEBE AGREGAR LA COMA AL FINAL, SINO NO FUNCIONA, data DEBE SER UNA TUPLA
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('listado_mascotas'))


########################### SERVICIOS ##################################
@app.route('/servicios/listado_servicios')
def listado_servicios():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM servicios")
    miResultado = cursor.fetchall()
    
    #Convertir los datos a diccionario
    insertarObjectos = [] 
    nombreDeColumnas = [columna[0] for columna in cursor.description]
    
    for unRegistro in miResultado:
        insertarObjectos.append(dict(zip(nombreDeColumnas, unRegistro)))
    
    # Cierra el cursor para liberar recursos de memoria.    
    cursor.close()
    
    return render_template('servicios/listado.html', data=insertarObjectos)


# ruta a la pagina para agregar una mascota
@app.route('/servicios/agregar_servicio')
def agregar_servicio():
    return render_template('servicios/agregar.html')


#Ruta para guardar mascotas en la bdd
@app.route('/servicio', methods=['POST'])
def addService():
    idServicio = request.form['id']
    precio = request.form['precio']
    profesional = request.form['profesional']
    detalle = request.form['detalle']


    if idServicio and precio and profesional and detalle:
        cursor = db.database.cursor()
        sql = "INSERT INTO servicios (idServicios, precio, Profesionales_idProfesionales, detalle) VALUES (%s, %s, %s, %s)"
        data = (idServicio, precio, profesional, detalle)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('listado_servicios'))


@app.route('/editar_servicio/<int:idServicios>', methods=['POST'])
def editar_servicio(idServicios):
    precio = request.form['precio']
    profesional = request.form['profesional']
    detalle = request.form['detalle']


    if precio and profesional and detalle:
        cursor = db.database.cursor()
        sql = "UPDATE servicios SET precio = %s, Profesionales_idProfesionales = %s, detalle = %s WHERE idServicios = %s"
        data = (precio, profesional, detalle, idServicios)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('listado_servicios'))


@app.route('/borra_servicio/<int:id>')
def borrar_servicio(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM servicios WHERE idServicios = %s"
    data = (id,) # SE DEBE AGREGAR LA COMA AL FINAL, SINO NO FUNCIONA, data DEBE SER UNA TUPLA
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('listado_servicios'))




# ejecutacion directa pero en puerto 4000 del localhost o servidor creado por flask
if __name__=='__main__':
    app.run(debug=True, port=4000)