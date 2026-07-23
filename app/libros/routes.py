from flask import Blueprint, jsonify, request
from app import libros
from app.libros.queries import (
    actualizar_disponibilidad,
    crear_libro,
    eliminar_libro,
    libros_con_autor,
    listar_libros,
    obtener_libro,
)

libros_bp = Blueprint("libros", __name__, url_prefix="/libros")


@libros_bp.route("", methods=["GET"])
def endpoint_listar_libros():
    libros = listar_libros()
    return jsonify(libros), 200


@libros_bp.route("/<int:libro_id>", methods=["GET"])
def endpoint_obtener_libro(libro_id):
    libro = obtener_libro(libro_id)
    if not libro:
        return {"error": "no existe"}, 404
    return jsonify(libro), 200


@libros_bp.route("", methods=["POST"])
def endpoint_crear_libro():
    datos = request.get_json()

    if not datos or "titulo" not in datos or "autor_id" not in datos:
        return {"error": "datos faltantes"}, 400
    nuevo = crear_libro(datos["titulo"], datos["autor_id"])
    return jsonify(nuevo), 201


@libros_bp.route("/<int:libro_id>/disponibilidad", methods=["PUT"])
def endpoint_actualizar_disponibilidad(libro_id):
    datos = request.get_json()
    if not datos or "disponible" not in datos:
        return {"error": "falta el campo disponible"}, 400

    disponibilidad = actualizar_disponibilidad(libro_id, datos["disponible"])
    if not disponibilidad:
        return {"error": "libro no encontrado"}, 404
    return jsonify(disponibilidad), 200


@libros_bp.route("/<int:libro_id>", methods=["DELETE"])
def endpoint_eliminar_libro(libro_id):
    eliminado = eliminar_libro(libro_id)
    if not eliminado:
        return {"error": "no existe"}, 404
    return "", 204

