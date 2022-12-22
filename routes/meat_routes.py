import controllers
from flask import request, Response, Blueprint

meats = Blueprint('meats', __name__)

@meats.route("/meat/add", methods=["POST"])
def meat_add() -> Response:
    return controllers.meat_add(request)

@meats.route("/meat/get", methods=["GET"])
def get_meats() -> Response:
    return controllers.get_meats(request)

@meats.route("/meat/update", methods=["POST"])
def meat_update() -> Response:
    return controllers.meat_update(request)

@meats.route("/meat/delete/<meat_id>", methods=["DELETE"])
def meat_delete(meat_id) -> Response:
    return controllers.meat_delete(request, meat_id)

