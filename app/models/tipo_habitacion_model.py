from app import mysql

def obtener_tipos_habitacion():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tipohabitacion")
    return cur.fetchall()

def insertar_tipo_habitacion(nombre, descripcion):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO tipohabitacion (nombre, descripcion) VALUES (%s, %s)", (nombre, descripcion))
    mysql.connection.commit()
