from app import mysql

def obtener_tipos_habitacion():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tipohabitacion")
    return cur.fetchall()

def insertar_tipo_habitacion(nombre, descripcion):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO tipohabitacion (nombre, descripcion) VALUES (%s, %s)", (nombre, descripcion))
    mysql.connection.commit()

def obtener_tipo_por_id(tipo_habitacion_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tipohabitacion WHERE tipo_habitacion_id = %s", (tipo_habitacion_id,))
    return cur.fetchone()

def actualizar_tipo(tipo_habitacion_id, nombre, descripcion):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE tipohabitacion SET nombre = %s, descripcion = %s WHERE tipo_habitacion_id = %s", (nombre, descripcion, tipo_habitacion_id))
    mysql.connection.commit()

def eliminar_tipo(tipo_habitacion_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tipohabitacion WHERE tipo_habitacion_id = %s", (tipo_habitacion_id,))
    mysql.connection.commit()