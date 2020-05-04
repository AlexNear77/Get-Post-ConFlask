
def crear_usuario(bd, correo, contra):
    h = hashlib.new('sha256', bytes(contra, 'utf-8'))
    h = h.hexdigest()
    cursor = bd.cursor()
    insertar = ("INSERT INTO usuario(correo, contrasenia) VALUES(%s, %s)")
    cursor.execute(insertar, (correo, h))
    bd.commit()

def existe_usuario(bd, correo):
    cursor = bd.cursor()
    query = "SELECT COUNT(*) FROM usuario WHERE correo = %s"
    cursor.execute(query, (correo,))

    if cursor.fetchone()[0] == 1:
        return True
    else:
        return False

import hashlib
def iniciar_sesion(bd, correo, contra):
    h = hashlib.new('sha256', bytes(contra, 'utf-8'))
    h = h.hexdigest()
    cursor = bd.cursor()
    print(correo)
    print(contra)
    query = "SELECT COUNT(*) FROM usuario WHERE correo = %s AND contrasenia = %s"
    cursor.execute(query, (correo, h))

    if cursor.fetchone()[0] == 1:
        return True
    else:
        return False