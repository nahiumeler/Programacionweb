from flask import Flask, jsonify, request, Response, session
from database import ver_usuarios, crear_tablas, agregar_cita_profesional_usuario,obtener_citas_por_profesionalid,obtener_citas_por_profesionalid_fecha, cambiar_contrasena, verificar_contrasena,obtener_profesional_por_profesionalid, eliminar_cuenta, verCitasUsuario, verProfesionales, registrar_usuario, obtener_usuario_por_usuarioid, registrar_profesional
from flask_cors import CORS  
import mercadopago

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "¡Bienvenido al Mercado de Trabajo! Aquí, los usuarios pueden consultar servicios ofrecidos."

@app.route("/usuarios")
def get_usuarios():
    usuarios = ver_usuarios('base1.db')
    return jsonify(usuarios)    

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    userid = data['userid']
    contrasenia = data['contrasenia']
    
    usuario = obtener_usuario_por_usuarioid(userid)
    
    if usuario and usuario['contraseña'] == contrasenia:  
        return jsonify({'mensaje': 'Inicio de sesión exitoso'}), 200
    else:
        return jsonify({'error': 'Usuario o contraseña incorrectos'}), 401

@app.route("/registrarse", methods=["POST"])
def registrar_api():
    data = request.json
    userid = data.get("userid")
    email = data.get("email")
    contrasenia = data.get("contrasenia")
    
   
    resultado = registrar_usuario(userid, email, contrasenia)
    
    if resultado:  
        return jsonify({"mensaje": "Usuario registrado correctamente"}), 201
    else:  
        return jsonify({"error": "El nombre de usuario ya existe"}), 409


@app.route("/configuracion/cambiar_contrasena", methods=["PUT"])
def api_cambiar_contrasena():
    data = request.json
    user_id = data.get("user_id")
    contrasena_actual = data.get("contrasena_actual")
    nueva_contrasena = data.get("nueva_contrasena")

    if verificar_contrasena(user_id, contrasena_actual):
        cambiar_contrasena(user_id, nueva_contrasena)
        return jsonify({"message": "Contraseña cambiada correctamente"}), 200
    else:
        return jsonify({"message": "Contraseña actual incorrecta"}), 400

    

@app.route("/configuracion/eliminar_cuenta", methods=["DELETE"])
def api_eliminar_cuenta():
    data = request.json
    user_id = data.get("user_id")  
    contrasena = data.get("contrasena")

    if verificar_contrasena(user_id, contrasena):
        eliminar_cuenta(user_id)
        return jsonify({"message": "Cuenta eliminada exitosamente"}), 200
    else:
        return jsonify({"message": "Contraseña incorrecta"}), 400
    
@app.route("/profesionales/<rubro_id>", methods=["GET"])
def get_profesionales_rubro(rubro_id):
    profesionales, rubro = verProfesionales(rubro_id)
    if profesionales:
        return jsonify(profesionales, rubro)
    else:
        return jsonify({"message": "No se encontraron profesionales"}), 404

    
@app.route("/info_profesional/<profesionalid>", methods=["GET"])
def get_profesional(profesionalid):
    profesional = obtener_profesional_por_profesionalid(profesionalid)
    if profesional:
        return jsonify(profesional)
    else:
        return jsonify({"message": "No se encontraron profesionales"}), 404  


@app.route("/reservas/<profesionalid>", methods=["GET"])
def get_profesional_citas(profesionalid):
    profesional = obtener_citas_por_profesionalid(profesionalid)
    if profesional:
        return jsonify(profesional)
    else:
        return jsonify({"message": "No se encontraron profesionales"}), 404
    
@app.route("/reservas_fecha/<profesionalid>/<fecha>", methods=["GET"])
def get_profesional_citas_fecha(profesionalid,fecha):
    cita_fecha = obtener_citas_por_profesionalid_fecha(profesionalid,fecha)    
    return cita_fecha
    
@app.route("/agregarCita/<userid>/<profesionalid>/<fecha>/<comentarios>", methods=["GET"])
def agregarCita(userid,profesionalid,fecha,comentarios):
    try:
        agregar_cita_profesional_usuario(userid,profesionalid,fecha,comentarios)    
        return Response(status=204)
    except Exception as e:
        print(e)
        
        print("Error al agregar la cita:", e)
        
        return jsonify({"error": str(e)}), 500
    


@app.route('/crear_preferencia/<profesionalid>/<fecha>/<comentarios>', methods=['POST'])
def crear_preferencia(profesionalid,fecha,comentarios):
    sdk = mercadopago.SDK("TEST-3472895419018302-101514-3cf4ca40ef6d57f2e5246f746823a093-476449361") 

    
    preference_data = {
        "items": request.json.get('items', []),
        "back_urls": {
            "success": f"http://localhost:4000/static/pago_aprobado.html?profesionalid={profesionalid}&fecha={fecha}&comentarios={comentarios}",
            "failure": f"http://localhost:4000/static/pago_rechazado.html?profesionalid={profesionalid}&fecha={fecha}&comentarios={comentarios}",
            "pending": f"http://localhost:4000/static/pago_pendiente.html?profesionalid={profesionalid}&fecha={fecha}&comentarios={comentarios}"
        },
        "auto_return": "approved"
    }

  
    preference_response = sdk.preference().create(preference_data)
    preference_id = preference_response["response"]["id"]
    return jsonify({"preferenceId": preference_id})
    

@app.route("/VerReservas", methods=["GET"])
def VerReservas():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"message": "Parámetro user_id requerido"}), 400
    
    print(f"Buscando citas para el usuario: {user_id}")
    citas = verCitasUsuario(user_id)
    
    if citas:
        return jsonify(citas)
    else:
        return jsonify({"message": "No se encontraron citas"}), 404

    

@app.route('/usuarios/cerrar_sesion', methods=['POST'])
def cerrar_sesion():
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        
        if not user_id:
            return jsonify({"message": "Error: No se proporcionó el id de usuario."}), 400

        if 'user_id' in session and session['user_id'] == user_id:
            session.pop('user_id', None)  # elimina el user_id de la sesión
        
        return jsonify({"message": "Sesión cerrada"}), 200

    except Exception as e:
        return jsonify({"message": f"Error al cerrar sesión: {str(e)}"}), 500


@app.route('/registro-profesional', methods=['POST'])
def registro_profesional():
    data = request.json
    resultado = registrar_profesional(
        data['nombre'], data['apellido'], data['profesion'],
        data['experiencia'], data['email'], data['telefono'], data['conocimiento']
    )
    return jsonify(resultado)


if __name__ == "__main__":
    crear_tablas('base1.db') 
    app.run(debug=True, port=4000)


