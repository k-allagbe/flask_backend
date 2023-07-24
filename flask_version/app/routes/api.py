from flask import Blueprint, jsonify, request

api = Blueprint("api", __name__)


@api.route("", methods=["GET"])
def root():
    return "api root"
