from flask import Blueprint, jsonify
from app.autores.queries import listar_autores

autores_bp = Blueprint("autores", __name__, url_prefix="/autores")


@autores_bp.route("", methods=["GET"])
def endpoint_listar_autores():
    autores = listar_autores()
    return jsonify(autores), 200
