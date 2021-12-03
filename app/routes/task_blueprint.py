from flask import Blueprint
from app.controllers.tasks_controller import create_task, delete_task, update_task

bp = Blueprint("bp_tasks", __name__)

bp.post("/task")(create_task)
bp.patch("/task/<id>")(update_task)
bp.delete("/task/<id>")(delete_task)
