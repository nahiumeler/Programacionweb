import sqlite3
ruta_base = 'base1.db'

def crear_tablas(ruta_b):
    conexion = sqlite3.connect(ruta_b)
    cursor = conexion.cursor()
    try:
        tabla = 'CREATE TABLE IF NOT EXISTS usuarios (userid INTEGER PRIMARY KEY AUTOINCREMENT, nombre_usuario VARCHAR(100), email VARCHAR(100), contraseña VARCHAR(100))'
        cursor.execute(tabla)
        tabla2 = 'CREATE TABLE reservas (reservaid INTEGER PRIMARY KEY AUTOINCREMENT, nombre_usuario VARCHAR(100), profesionalid INTEGER(5), fecha VARCHAR(100), comentarios VARCHAR(200))'
        cursor.execute(tabla2)
        tabla3 = 'CREATE TABLE IF NOT EXISTS profesionales (profesionalid INTEGER PRIMARY KEY AUTOINCREMENT,nombre VARCHAR(100),apellido VARCHAR(100),rubro INTEGER(5),imagen VARCHAR(150),precio REAL,localidad VARCHAR(100),descripcion TEXT)'
        cursor.execute(tabla3)
        tabla4 = 'CREATE TABLE rubro (rubroid INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100))'
        cursor.execute(tabla4)
        tabla5 = '''CREATE TABLE IF NOT EXISTS nuevos_profesionales (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100),apellido VARCHAR(100),profesion VARCHAR(100), experiencia TEXT, email VARCHAR(100), telefono VARCHAR(15), conocimiento VARCHAR(100))'''
        cursor.execute(tabla5)
        conexion.close()
        return True
    except:
        return False


existe = crear_tablas(ruta_base)

def obtener_usuario_por_usuarioid(userid):
    conn = sqlite3.connect(ruta_base)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nombre_usuario = ?", (userid,))
    usuario = cursor.fetchone()
    conn.close()
    if usuario:
        return {'userid': usuario[1], 'email': usuario[2], 'contraseña': usuario[3]}
    return None

def registrar_usuario(userid, email, contraseña):
    conexion = sqlite3.connect(ruta_base)
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (nombre_usuario, email, contraseña) VALUES (?, ?, ?)", (userid, email, contraseña))
        conexion.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexion.close()

def insertar_lista_usuarios(ruta_b, lista):
    conexion = sqlite3.connect(ruta_b)
    cursor = conexion.cursor()
    sentenciasql = "INSERT OR IGNORE INTO usuarios (nombre_usuario, email, contraseña) VALUES (?, ?, ?)"
    cursor.executemany(sentenciasql, lista)
    conexion.commit()
    conexion.close()

def insertar_lista_profesional(ruta_b, lista):
    conexion = sqlite3.connect(ruta_b)
    cursor = conexion.cursor()
    sentenciasql = "INSERT OR IGNORE INTO profesionales (nombre, apellido, rubro, imagen, precio, localidad, descripcion) VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.executemany(sentenciasql, lista)
    conexion.commit()
    conexion.close()


def insertar_lista_rubros(ruta_b, lista):
    conexion = sqlite3.connect(ruta_b)
    cursor = conexion.cursor()
    sentenciasql = "INSERT OR IGNORE INTO rubro (nombre) VALUES (?)"
    cursor.executemany(sentenciasql, lista)
    conexion.commit()
    conexion.close()

def insertar_lista_citas(ruta_b, lista):
    conexion = sqlite3.connect(ruta_b)
    cursor = conexion.cursor()
    sentenciasql = "INSERT OR IGNORE INTO reservas (nombre_usuario,profesionalid,fecha,comentarios) VALUES (?,?,?,?)"
    cursor.executemany(sentenciasql, lista)
    conexion.commit()
    conexion.close()

usuarios = [
    ("nmeler", "nmeler@gmail.com", "12345"),
    ("martu122", "martu122@gmail.com", "simona321"),
    ("nico", "nico@gmail.com", "123"),
    ("julieta95", "julieta95@hotmail.com", "clave123"),
    ("roberto_gym", "roberto@hotmail.com", "gym1234"),
    ("luciana_p", "luciana@hotmail.com", "luciana456"),
    ("marcos_viajes", "marcos@gmail.com", "viajero321"),
    ("valentina_tech", "valentina@gmail.com", "valen_tech"),
    ("lucas_figue", "lucas@gmail.com", "lucasfi333"),
    ("carolina_t", "carolina@hotmail.com", "carovet"),
    ("leo_fit", "leo@gmail.com", "leo123")
]

profesionales = [
    ("Lucila", "Martinez", 1, "imagenes/Lucila-Martinez.jpg", 10000, "Belgrano", "Maquillaje para eventos, sesiones fotográficas y producciones "),
    ("Alma", "Torres", 1, "imagenes/Alma-Torres.jpg", 8000, "Berazategui", "Maquillaje para sesiones fotográficas, eventos temáticos y producciones audiovisuales"),
    ("Joaquín", "Pereyra", 1, "imagenes/Joaquin-Pereyra.jpg", 6000, "Villa Crespo", "Maquillaje para novias, maquillaje para pasarela, asesoramiento"),
    ("Clara", "Alvarez", 1, "imagenes/Clara-Alvarez.jpg", 9000, "Recoleta", "Maquillaje artístico y de fantasía, maquillaje para eventos sociales y para sesiones de fotos temáticas"),
    ("Juana", "Lopez", 1, "imagenes/Juana-Lopez.jpg", 11000, "Palermo", "Maquillaje para ocasiones especiales, desde maquillaje natural y elegante hasta looks más audaces y artísticos"),
    ("Martina", "Romero", 1, "imagenes/Martina-Romero.jpg", 12000, "Caballito", "Maquillaje para eventos sociales y corporativos, maquillaje editorial"),
    ("Susana", "Acosta", 2, "imagenes/Susana-Acosta.jpg", 8000, "Villa Bella Vista", "Cortes de pelo, peinados para ocasiones especiales, coloración"),
    ("Santiago", "Martínez", 2, "imagenes/Santiago-Martinez.jpg", 9000, "Puerto Esmeralda", "Coloración, mechas, alisados"),
    ("Lourdes", "Arias", 2, "imagenes/Lourdes-Arias.jpg", 10000, "Avellaneda", "Alisados, permanentes, servicios para niños"),
    ("Constanza", "Herrera", 2, "imagenes/Constanza-Herrera.jpg", 9000, "Bahía Blanca", "Tratamientos de keratina, peinados para eventos"),
    ("María", "Sánchez", 2, "imagenes/Maria-Sanchez.jpg", 10000, "La Plata", "Tintura fantasia, extensiones de cabello"),
    ("Julia", "Sosa", 2, "imagenes/Julia-Sosa.jpg", 9000, "Morón", "Tratamientos capilares, tintura fantasia"),
    ("Angelina", "Benitez", 3, "imagenes/Angelina-Benitez.jpg", 7000, "La Plata", "Tratamientos de spa para manos, esmaltado permanente y diseños de uñas personalizados"),
    ("Paula", "González", 3, "imagenes/Paula-Gonzalez.jpg", 6000, "Campana", "Manicuras clásicas, manicuras francesas y manicuras con esmalte semipermanente"),
    ("Pilar", "Herrera", 3, "imagenes/Pilar-Herrera.jpg", 4500, "Balvanera", "Manicuras básicas"),
    ("Amparo", "Otero", 3, "imagenes/Amparo-Otero.jpg", 5500, "Olivos", "Manicuras tradicionales y manicuras francesas"),
    ("Paloma", "Iglesias", 3, "imagenes/Paloma-Iglesias.jpg", 5000, "Temperley", "Manicuras tradicionales y tratamientos de cutículas"),
    ("Milagros", "Rojas", 3, "imagenes/Milagros-Rojas.jpg", 4500, "Ramos Mejía", "Manicuras clásicas"),
    ("Cintia", "Romero", 4, "imagenes/Cintia-Romero.jpg", 10000, "Lomas de Zamora", "Extensiones clásicas de pestañas para un look natural y elegante"),
    ("Jimena", "Sampedro", 4, "imagenes/Jimena-Sampedro.jpg", 12000, "Martínez", "Volumen ruso para pestañas densas y glamorosas"), 
    ("Ana", "Alonso", 4, "imagenes/Ana-Alonso.jpg", 6750, "Lanús", "Lifting y tintado de pestañas para una mirada natural y definida"), 
    ("Morena", "Cabrera", 4, "imagenes/Morena-Cabrera.jpg", 10000, "San Isidro", "Extensiones híbridas para un equilibrio perfecto entre lo natural y lo voluminoso"), 
    ("Guillermina", "Martín", 4, "imagenes/Guillermina-Martin.jpg", 4500, "Tigre", "Retoque de pestañas que restaura el volumen y la longitud perdidos"), 
    ("Helena", "Flores", 4, "imagenes/Helena-Flores.jpg", 14000, "Avellaneda", "Diseño personalizado de pestañas para ocasiones especiales") 
]


rubros = [
    ("Maquillaje",),
    ("Peluqueria",),
    ("Manicura",),
    ("Lashes",)
]

citas = [
    ("a",1,"12122025","aaaaaaaaaaaa"),
    ("a",1,"12122026","aaaaaaaaaaaa"),
    ("a",2,"12122027","aaaaaaaaaaaa"),
    ("a",2,"12122028","aaaaaaaaaaaa")
]

if existe:
    insertar_lista_usuarios(ruta_base, usuarios)
    insertar_lista_profesional(ruta_base, profesionales)
    insertar_lista_rubros(ruta_base, rubros)
    insertar_lista_citas(ruta_base, citas)

def ver_usuarios(ruta_b):
    conexion = sqlite3.connect(ruta_b)
    cursor = conexion.cursor()
    sentenciasql = "SELECT * FROM usuarios"
    cursor.execute(sentenciasql)
    usuarios = cursor.fetchall()
    conexion.commit()
    conexion.close()
    diccionario_usuarios = []
    for usuario in usuarios:
        diccionario = {
            "userid": usuario[1],
            "email": usuario[2],
            "contraseña": usuario[3]
        }
        diccionario_usuarios.append(diccionario)
    return diccionario_usuarios

def verProfesionales(rubro_id):
    conexion = sqlite3.connect(ruta_base)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM profesionales WHERE rubro=?", (rubro_id,))
    prof = cursor.fetchall()
    diccionario_profesionales = []
    for pro in prof:
        diccionario = {
            "profesionalid": pro[0],
            "nombre": pro[1],
            "apellido": pro[2],
            "rubro": pro[3],
            "imagen": pro[4],
            "precio": pro[5],
            "localidad": pro[6],
            "descripcion": pro[7]
        }
        diccionario_profesionales.append(diccionario)
    cursor.execute("SELECT nombre FROM rubro WHERE rubroid=?", (rubro_id,))
    rubro = cursor.fetchall()
    conexion.close()
    return diccionario_profesionales, rubro

def insertar_lista_profesional(ruta_b, lista):
    conexion = sqlite3.connect(ruta_b)
    cursor = conexion.cursor()
    sentenciasql = "INSERT OR IGNORE INTO profesionales (nombre, apellido, rubro, imagen, precio, localidad, descripcion) VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.executemany(sentenciasql, lista)
    conexion.commit()
    conexion.close()

def obtener_profesional_por_profesionalid(profesionalid):
    conn = sqlite3.connect(ruta_base)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM profesionales WHERE profesionalid = ?", (profesionalid,))
    profesional = cursor.fetchone()
    conn.close()
    if profesional:
        return {'profesionalid': profesional[0], 'nombre': profesional[1], 'apellido': profesional[2], 'rubro':profesional[3], 'imagen':profesional[4], 'precio':profesional[5], 'localidad':profesional[6], 'descripcion':profesional[7],}
    return None

def editar_perfil(user_id, campo, nuevo_valor):
    conn = sqlite3.connect(ruta_base)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE usuarios SET {campo} = ? WHERE nombre_usuario = ?", (nuevo_valor, user_id))
    conn.commit()
    conn.close()

def cambiar_contrasena(user_id, nueva_contrasena):
    conn = sqlite3.connect(ruta_base)
    cursor = conn.cursor()
    cursor.execute("UPDATE usuarios SET contraseña = ? WHERE nombre_usuario = ?", (nueva_contrasena, user_id))
    conn.commit()
    print(f"Contraseña cambiada para el usuario: {user_id}")  
    conn.close()


def eliminar_cuenta(user_id):
    conn = sqlite3.connect(ruta_base)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE nombre_usuario = ?", (user_id,))
    conn.commit()
    conn.close()

def verificar_contrasena(user_id, contrasena):
    conn = sqlite3.connect(ruta_base)
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM usuarios WHERE nombre_usuario = ? AND contraseña = ?", (user_id, contrasena))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def obtener_citas_por_profesionalid(profesionalid):
    conexion = sqlite3.connect(ruta_base)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM reservas WHERE profesionalid=?", (profesionalid,))
    citas = cursor.fetchall()
    conexion.close()

    diccionario_citas_profesional = []
    for cita in citas:
        diccionario = {
            "nombre_usuario": cita[1],
            "profesionalid": cita[2],
            "fecha": cita[3]
        }
        diccionario_citas_profesional.append(diccionario)
    
    return diccionario_citas_profesional

def obtener_citas_por_profesionalid_fecha(profesionalid,fecha):
    conexion = sqlite3.connect(ruta_base)
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM reservas WHERE profesionalid=? AND fecha=?", (profesionalid,fecha,))
    citas = cursor.fetchone()
    conexion.close()

    if citas[0] == 0:
        return "false"
    else:
        return "true"

def verCitasUsuario(user_id):
    conexion = sqlite3.connect(ruta_base)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM reservas WHERE nombre_usuario=?", (user_id,))
    citas = cursor.fetchall() 


    diccionario_citas = []
    for cita in citas:
        diccionario = {
            "nombre_usuario": cita[1],
            "profesionalId": cita[2],
            "fecha": cita[3],
            "comentarios": cita[4],
            "rubro":0
        }
        cursor.execute("SELECT rubro.nombre FROM rubro INNER JOIN profesionales ON profesionales.rubro = rubro.rubroid WHERE profesionalid=?", (diccionario["profesionalId"],))
        rubro = cursor.fetchone() 
        diccionario["rubro"] = rubro[0]
        cursor.execute("SELECT nombre || ' ' || apellido AS nombre_completo FROM profesionales WHERE profesionalid=?", (diccionario["profesionalId"],))
        res = cursor.fetchone()
        diccionario["profesionalId"] = res[0]
        diccionario_citas.append(diccionario)
    conexion.close()
    
    return diccionario_citas

def agregar_cita_profesional_usuario(userid,profesionalid,fecha,comentarios):
    conexion = sqlite3.connect(ruta_base)
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM reservas WHERE profesionalid = ? AND fecha = ?", (profesionalid, fecha))
    resultado = cursor.fetchone()[0]
    if(resultado==0):
        cursor.execute("INSERT INTO reservas (nombre_usuario,profesionalid,fecha,comentarios) VALUES (?,?,?,?)", (userid,profesionalid,fecha,comentarios))
        conexion.commit()
    conexion.close()


def registrar_profesional(nombre, apellido, profesion, experiencia, email, telefono, conocimiento):
    conexion = sqlite3.connect(ruta_base)
    cursor = conexion.cursor()
    try:
        cursor.execute("""
            INSERT INTO nuevos_profesionales (nombre, apellido, profesion, experiencia, email, telefono, conocimiento)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (nombre, apellido, profesion, experiencia, email, telefono, conocimiento))
        conexion.commit()
        return {"mensaje": "Información guardada exitosamente"}
    except sqlite3.Error as e:
        return {"error": f"Error al guardar la información del profesional: {str(e)}"}
    finally:
        conexion.close()
