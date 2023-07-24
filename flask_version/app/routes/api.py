from app.repositories import stagiaires_repository
from flask import Blueprint, current_app, jsonify, request

api = Blueprint("api", __name__)


@api.route("", methods=["GET"])
def root():
    return "api root"


@api.route("/top", methods=["GET"])
def get_top_n():
    """Return the top N documents with the highest scores."""
    n = request.args.get("n", default=1, type=int)
    print("here")
    print(n)
    if n < 1 or n > 100:
        return jsonify(error="Parameter n should be between 1 and 100"), 400

    try:
        documents = stagiaires_repository.get_top_documents(n)
        result = [document.to_dict() for document in documents]
        return jsonify(result), 200
    except Exception as e:
        return jsonify(error=str(e)), 500
