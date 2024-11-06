from flask import Flask, jsonify, request
from superHeroes import superheroes
from flask_cors import CORS
# Importa Flask, jsonify (para devolver datos en formato JSON), los datos de superheores, y CORS (para permitir solicitudes desde otro dominio).

app = Flask(__name__)
CORS(app)
# Crea la aplicación Flask y habilita CORS para aceptar peticiones desde cualquier origen.

@app.route('/listar', methods = ['GET'])
def listar():
    print(superheroes)
    return jsonify(superheroes)
''' Define la ruta /listar con el método GET para devolver la lista de superhéroes.
print(superheores) muestra la lista en la consola del servidor.
return jsonify(superheores) devuelve la lista en formato JSON como respuesta.'''

@app.route('/agregar', methods=['POST'])
def agregar():
    data = request.get_json()
    new_hero = {
        'name': data['name'],
        'skill': data['skill'],
        'image': data['image']  # Guardamos el nombre del archivo de imagen proporcionado
    }
    superheroes.append(new_hero)
    return jsonify(new_hero), 201

@app.route('/actualizar/<name>', methods=['PUT'])
def actualizar(name):
    data = request.get_json()
    new_skill = data.get('skill')

    for hero in superheroes:
        if hero['name'].lower() == name.lower():  # Comparación insensible a mayúsculas
            hero['skill'] = new_skill  # Actualizamos la habilidad
            return jsonify(hero), 200

    return jsonify({'error': 'Superhéroe no encontrado'}), 404

@app.route('/eliminar_superheroe', methods=['DELETE'])
def eliminar_superheroe():
    data = request.get_json()
    nombre = data.get('name')

    for i, superheroe in enumerate(superheroes):
        if superheroe['name'].lower() == nombre.lower():
            del superheroes[i]
            return jsonify({'message': f'{nombre} eliminado exitosamente'}), 200

    return jsonify({'error': 'Superhéroe no encontrado'}), 404

if __name__ == '__main__':
        app.run(port= 5000, debug=True)
# Ejecuta la aplicación Flask en el puerto 5000 en modo de depuración (debug=True).