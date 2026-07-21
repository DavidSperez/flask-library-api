from flask import Flask
from app.autores.routes import autores_bp
from app.libros.routes import libros_bp
from app.prestamos.routes import prestamos_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(autores_bp)
    app.register_blueprint(libros_bp)
    app.register_blueprint(prestamos_bp)
    return app
