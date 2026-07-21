from app.conexion import obtener_conexion
from psycopg2.extras import RealDictCursor


def crear_prestamo(libro_id, usuario_nombre):
    conexion = obtener_conexion()
    cursor = conexion.cursor(cursor_factory=RealDictCursor)

    cursor.execute(
        "INSERT INTO prestamos (libro_id,nombre_usuario) VALUES (%s, %s);",
        (libro_id, usuario_nombre),
    )
    cursor.execute(
        "UPDATE libros SET disponible = FALSE WHERE id = %s;",
        (libro_id,),
    )
    conexion.commit()
    cursor.close()
    conexion.close()
    return {"mensaje": "creado con exito"}


def prestamos_por_usuario():
    conexion = obtener_conexion()
    cursor = conexion.cursor(cursor_factory=RealDictCursor)

    cursor.execute(
        "SELECT nombre_usuario, COUNT(libro_id) AS total_prestamos FROM prestamos GROUP BY nombre_usuario ORDER BY total_prestamos DESC;"
    )
    prestamo = cursor.fetchall()
    cursor.close()
    conexion.close()
    return prestamo
