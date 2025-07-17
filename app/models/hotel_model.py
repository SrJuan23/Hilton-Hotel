from app import mysql

def obtener_hoteles():
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT h.hotel_id, h.nombre, h.direccion, h.telefono, h.ano_construccion,
               c.nombre AS categoria, p.nombre AS pais
        FROM hotel h
        JOIN categoria c ON h.categoria_id = c.categoria_id
        JOIN pais p ON h.pais_codigo = p.pais_codigo
    """)
    return cur.fetchall()

def insertar_hotel(nombre, direccion, telefono, anio, categoria_id, pais_codigo):
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO hotel (nombre, direccion, telefono, ano_construccion, categoria_id, pais_codigo)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (nombre, direccion, telefono, anio, categoria_id, pais_codigo))
    mysql.connection.commit()

def eliminar_hotel_por_id(hotel_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM hotel WHERE hotel_id = %s", (hotel_id,))
    mysql.connection.commit()

def obtener_hotel_por_id(hotel_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM hotel WHERE hotel_id = %s", (hotel_id,))
    return cur.fetchone()

def actualizar_hotel(hotel_id, nombre, direccion, telefono, ano_construccion, categoria_id, pais_codigo):
    cur = mysql.connection.cursor()
    cur.execute("""
    UPDATE hotel
    SET nombre = %s, direccion = %s, telefono = %s, ano_construccion = %s, categoria_id = %s, pais_codigo = %s
    WHERE hotel_id = %s
""", (nombre, direccion, ano_construccion, telefono, categoria_id, pais_codigo, hotel_id))
    mysql.connection.commit()