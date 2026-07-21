# API BIBLIOTECA

Una API REST sencilla para gestionar libros, autores y préstamos
Armé este proyecto para practicar backend y estructurar el código de forma limpia usando Blueprints, en lugar de dejar todo en un solo archivo gigante

## **STACK TECNOLÓGICO**

* Python (Flask)
* PostgreSQL (Psycopg2)

## **ESTRUCTURA**

El proyecto está separado por dominios para que sea fácil de mantener y escalar:
* `/autores`
* `/libros`
* `/prestamos`

## **CÓMO CORRERLO**

1. Clona el repositorio
2. Crea tu entorno virtual e instala las dependencias (`flask`, `psycopg2`)
3. Ejecuta el archivo `esquema.sql` en tu base de datos PostgreSQL
4. Levanta el servidor con `python run.py`