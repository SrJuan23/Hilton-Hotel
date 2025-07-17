from app import mysql

def obtener_categorias():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM categoria")
    return cur.fetchall()

def insertar_categoria(nombre, descripcion, servicios):
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO categoria (nombre, descripcion, servicios_tipicos)
        VALUES (%s, %s, %s)
    """, (nombre, descripcion, servicios))
    mysql.connection.commit()

def obtener_categoria_por_id(categoria_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM categoria WHERE categoria_id = %s", (categoria_id,))
    return cur.fetchone()

def actualizar_categoria(categoria_id, nombre, descripcion, servicios_tipicos):
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE categoria
        SET nombre = %s, descripcion = %s, servicios_tipicos = %s
        WHERE categoria_id = %s
    """, (nombre, descripcion, servicios_tipicos, categoria_id))
    mysql.connection.commit()

def eliminar_categoria(categoria_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM categoria WHERE categoria_id = %s", (categoria_id,))
    mysql.connection.commit()