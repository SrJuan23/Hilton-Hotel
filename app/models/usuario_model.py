from app import mysql

def buscar_usuario_por_correo(correo):
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, nombre, correo, clave FROM usuarios WHERE correo = %s", (correo,))
    return cur.fetchone()

def insertar_usuario(nombre, correo, clave_hash, pais_codigo):
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO usuarios (nombre, correo, clave, pais_codigo)
        VALUES (%s, %s, %s, %s)
    """, (nombre, correo, clave_hash, pais_codigo))
    mysql.connection.commit()

def buscar_usuario_por_id(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, nombre, correo FROM usuarios WHERE id = %s", (user_id,))
    return cur.fetchone()
