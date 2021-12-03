from app.configs.database import db

category_tasks = db.Table('category_tasks',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id')),
    db.Column('task_id', db.Integer, db.ForeignKey('tasks.id'))
)