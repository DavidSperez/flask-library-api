from app.conexion import obtener_conexion
from psycopg2.extras import RealDictCursor


def listar_libros():
    conexion = obtener_conexion()
    cursor = conexion.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT * FROM libros;")
    libros = cursor.fetchall()
    cursor.close()
    conexion.close()
    return libros


def obtener_libro(libro_id):
    conexion = obtener_conexion()
    cursor = conexion.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT * FROM libros WHERE id =%s;", (libro_id,))
    libro = cursor.fetchone()
    cursor.close()
    conexion.close()
    return libro


def crear_libro(titulo, autor_id):
    conexion = obtener_conexion()
    cursor = conexion.cursor(cursor_factory=RealDictCursor)

    cursor.execute(
        "INSERT INTO libros (titulo, autor_id) VALUES (%s, %s) RETURNING titulo, autor_id;",
        (titulo, autor_id),
    )
    libro = cursor.fetchone()
    conexion.commit()
    cursor.close()
    conexion.close()
    return libro


def actualizar_disponibilidad(libro_id, disponible):
    conexion = obtener_conexion()
    cursor = conexion.cursor(cursor_factory=RealDictCursor)

    cursor.execute(
        "UPDATE libros SET disponible = %s WHERE id = %s RETURNING titulo, disponible;",
        (disponible, libro_id),
    )
    libro = cursor.fetchone()
    conexion.commit()
    cursor.close()
    conexion.close()
    return libro


def eliminar_libro(libro_id):
    conexion = obtener_conexion()
    cursor = conexion.cursor(cursor_factory=RealDictCursor)

    cursor.execute("DELETE FROM libros WHERE id = %s;", (libro_id,))
    conexion.commit()

    cursor.close()
    conexion.close()
    return {"mensaje": "Borrado exitosamente"}


def libros_con_autor():
    conexion = obtener_conexion()
    cursor = conexion.cursor(cursor_factory=RealDictCursor)

    cursor.execute(
        "SELECT titulo, autores.nombre FROM libros INNER JOIN autores ON libros.autor_id = autores.id;"
    )
    libros = cursor.fetchall()
    cursor.close()
    conexion.close()
    return libros
