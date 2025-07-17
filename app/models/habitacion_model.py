from app import mysql

def obtener_habitaciones():
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT h.habitacion_id, h.codigo_habitacion,
               hotel.nombre AS hotel,
               tipo.nombre AS tipo
        FROM habitacion h
        JOIN hotel ON h.hotel_id = hotel.hotel_id
        JOIN tipohabitacion tipo ON h.tipo_habitacion_id = tipo.tipo_habitacion_id
    """)
    return cur.fetchall()

def insertar_habitacion(codigo, hotel_id, tipo_habitacion_id):
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO habitacion (codigo_habitacion, hotel_id, tipo_habitacion_id)
        VALUES (%s, %s, %s)
    """, (codigo, hotel_id, tipo_habitacion_id))
    mysql.connection.commit()

def obtener_habitacion_por_id(habitacion_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM habitacion WHERE habitacion_id = %s", (habitacion_id,))
    return cur.fetchone()

def actualizar_habitacion(habitacion_id, codigo_habitacion, hotel_id, tipo_habitacion_id):
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE habitacion
        SET codigo_habitacion = %s, hotel_id = %s, tipo_habitacion_id = %s
        WHERE habitacion_id = %s
    """, (codigo_habitacion, hotel_id, tipo_habitacion_id, habitacion_id))
    mysql.connection.commit()

def eliminar_habitacion(habitacion_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM habitacion WHERE habitacion_id = %s", (habitacion_id,))
    mysql.connection.commit()
