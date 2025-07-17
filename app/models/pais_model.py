from app import mysql

def obtener_paises():
    cur = mysql.connection.cursor()
    cur.execute("SELECT pais_codigo, nombre FROM pais")
    return cur.fetchall()
