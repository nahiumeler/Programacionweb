from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

from productos import productos

#configuraciones del servidor/ secret permite generar una conexión segura
app.secret_key = 'mysecretkey'
@app.route('/')
def Index():
    return render_template('index.html')


@app.route('/listar', methods=['GET'])
def listar():
    print(productos)
    return jsonify(productos)
    # return jsonify({'productos': productos})


@app.route('/registrar_pedido', methods=['POST'])
def registrar_pedido():
    if request.method == 'POST':
       
        return redirect(url_for('Index'))



if __name__ == '__main__':
    app.run(port = 3000, debug = True)


