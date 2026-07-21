import psycopg2


def obtener_conexion():
    return psycopg2.connect(
        host="localhost", database="biblioteca_db", user="postgres", password="12345678"
    )
