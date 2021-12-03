from flask import Blueprint
from app.controllers.eisenhowers_controller import create_eisenhower

bp = Blueprint("bp_eisenhowers", __name__)

bp.post("/eisenhowers")(create_eisenhower)