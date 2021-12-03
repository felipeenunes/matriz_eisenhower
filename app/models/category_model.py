from app.configs.database import db
from dataclasses import dataclass
from app.configs.database import db
from app.models.category_task_table import category_tasks

@dataclass
class CategoryModel(db.Model):
    id: int
    name: str
    description: str
    tasks: list
    
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String, default='')
    
    tasks = db.relationship(
        "TaskModel",
        secondary=category_tasks,
        backref = "categories"
    )