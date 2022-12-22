import controllers
from flask import request, Response, Blueprint

purchases = Blueprint('purchases', __name__)

@purchases.route("/purchase/add", methods=["POST"])
def purchase_add() -> Response:
    return controllers.purchase_add(request)

@purchases.route("/purchase/get", methods=["GET"])
def get_purchases() -> Response:
    return controllers.get_purchases(request)

@purchases.route("/purchase/update", methods=["POST"])
def purchase_update() -> Response:
    return controllers.purchase_update(request)

@purchases.route("/purchase/delete/<purchase_id>", methods=["DELETE"])
def purchase_delete(purchase_id) -> Response:
    return controllers.purchase_delete(request, purchase_id)

