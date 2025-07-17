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
