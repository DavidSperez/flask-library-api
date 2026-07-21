from app.conexion import obtener_conexion
from psycopg2.extras import RealDictCursor


def listar_autores():
    conexion = obtener_conexion()
    cursor = conexion.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT * FROM autores;")
    autores = cursor.fetchall()
    cursor.close()
    conexion.close()
    return autores


def crear_autor(nombre):
    conexion = obtener_conexion()
    cursor = conexion.cursor(cursor_factory=RealDictCursor)

    cursor.execute(
        "INSERT INTO autores(nombre) VALUES(%s) RETURNING id, nombre;", (nombre,)
    )
    autor_asignado = cursor.fetchone()

    conexion.commit()
    cursor.close()
    conexion.close()
    return autor_asignado
