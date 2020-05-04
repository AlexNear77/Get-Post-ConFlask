from flask import Flask, jsonify, request
import mysql.connector
from metodos import existe_usuario, crear_usuario, iniciar_sesion

app = Flask(__name__)
bd = mysql.connector.connect(user='root', password='', database='movies')


@app.route("/api/v1/usuario", methods=["GET", "POST"])
def usuario():
    if request.method == "GET":
        correo = request.args.get("correo")
        contra = request.args.get("contrasenia")
        print(correo)
        print(contra)
        if iniciar_sesion(bd, correo, contra):
            return jsonify({"code": "ok"})
        else:
            return jsonify({"code": "no"})
        return jsonify({"code": "error"})
    elif request.method == "POST" and request.is_json:
        data = request.get_json()
        correo = data["correo"]
        contra = data["contrasenia"]
        #-------------------------
        #   Verificamos coreoo
        #=========================
        if existe_usuario(bd, correo):
            return jsonify({"code":"existe"})
        else:
            # -------------------------
            #   Ecnyptamos y guardamos
            # =========================
            crear_usuario(bd,correo,contra)
            return jsonify({"code": "Registro exitoso"})
        return jsonify({"code": "error"})
    return jsonify({"code": "fatal error"})

app.run(debug=True)