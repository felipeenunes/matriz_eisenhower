from flask import Flask
from flask_migrate import Migrate

def init_app(app: Flask):
    Migrate(app, app.db)

    from app.models.task_model import TaskModel
    from app.models.eisenhowers_model import EisenhowerModel
    from app.models.category_model import CategoryModel
    from app.models.category_task_table import category_tasks