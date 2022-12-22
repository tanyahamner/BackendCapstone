import controllers
from flask import request, Response, Blueprint

wools = Blueprint('wools', __name__)

@wools.route("/wool/add", methods=["POST"])
def wool_add() -> Response:
    return controllers.wool_add(request)

@wools.route("/wool/get", methods=["GET"])
def get_wools() -> Response:
    return controllers.get_wools(request)

@wools.route("/wool/update", methods=["POST"])
def wool_update() -> Response:
    return controllers.wool_update(request)

@wools.route("/wool/delete/<wool_id>", methods=["DELETE"])
def wool_delete(wool_id) -> Response:
    return controllers.wool_delete(request, wool_id)

