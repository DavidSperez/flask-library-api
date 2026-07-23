from flask import Blueprint, jsonify, request
from app import prestamos
from app.prestamos.queries import crear_prestamo, prestamos_por_usuario

prestamos_bp = Blueprint("prestamos", __name__, url_prefix="/prestamos")


@prestamos_bp.route("/por-usuario", methods=["GET"])
def endpoint_prestamos_por_usuario():
    prestamos = prestamos_por_usuario()
    return jsonify(prestamos), 200


@prestamos_bp.route("", methods=["POST"])
def endpoint_crear_prestamo():
    datos = request.get_json()
    if not datos or "libro_id" not in datos or "usuario_nombre" not in datos:
        return {"error": "datos faltantes"}, 400
    return jsonify(crear_prestamo(datos["libro_id"], datos["usuario_nombre"])), 201
