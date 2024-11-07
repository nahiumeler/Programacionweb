from hola import lista,agregar, eliminar,editar
from flask import Flask, jsonify,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/listar', methods = ['GET'])
def listar():
    print(lista)
    return jsonify(lista)

@app.route("/agregar", methods=["POST"])
def agregar_ingrediente():
    data = request.json
    ingrediente=data.get("ingrediente")
    cantidad=data.get("cantidad")
    marca=data.get("marca")
    resultado = agregar(ingrediente,cantidad,marca)
    if resultado:  
        return jsonify({"mensaje": "Ingrediente agregado exitosamente"}), 201
    else:  
        return jsonify({"error": "No se pudo agregar el ingrediente"}), 409
    

@app.route("/eliminar", methods=["DELETE"])
def eliminar_ingrediente():
    data=request.json
    ingrediente_eliminado=data.get("ingrediente_a_eliminar")
    resultado2=eliminar(ingrediente_eliminado)
    if resultado2:  
        return jsonify({"mensaje": "Ingrediente borrado exitosamente"}), 201
    else:  
        return jsonify({"error": "No se pudo borrar el ingrediente"}), 409


@app.route("/editar",methods=['PUT']) 
def editar_ingrediente():
    data=request.json
    viejo=data.get("ingrediente_a_editar")
    nuevo=data.get("ingrediente_actualizado")
    rubro=data.get("rubro")

    resultado3=editar(viejo,rubro,nuevo)
    if resultado3:  
        return jsonify({"mensaje": "Ingrediente editado exitosamente"}), 201
    else:  
        return jsonify({"error": "No se pudo editar el ingrediente"}), 409


if __name__ == '__main__':
        app.run(port= 5000, debug=True)


