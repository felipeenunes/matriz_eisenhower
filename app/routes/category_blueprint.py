from flask import Blueprint
from app.controllers.categories_controller import create_category, delete_category, update_category, get_all

bp = Blueprint("bp_category", __name__)

bp.post("/category")(create_category)
bp.patch("/category/<id>")(update_category)
bp.delete("/category/<id>")(delete_category)
bp.get("/")(get_all)