from app.configs.database import db

class EisenhowerModel(db.Model):
    __tablename__ = 'eisenhowers'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))

    tasks = db.relationship("TaskModel", backref="task", uselist=True)