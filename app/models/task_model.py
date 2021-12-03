from app.configs.database import db
from app.models.eisenhowers_model import EisenhowerModel
from app.models.exc import OutOfRangeError

class TaskModel(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String)
    duration = db.Column(db.Integer)
    importance = db.Column(db.Integer)
    urgency = db.Column(db.Integer)
    
    eisenhower_id = db.Column(
        db.Integer,
        db.ForeignKey('eisenhowers.id')
    )

    def verify_eisenhower(self):
        if (self.importance!=1 and self.importance!=2) or (self.urgency!=1 and self.urgency!=2):
            raise OutOfRangeError(self.importance, self.urgency)
        elif self.importance==1 and self.urgency==1:
            self.eisenhower_id=1
            return "Do It First"
        elif self.importance==1 and self.urgency==2:
            self.eisenhower_id=2
            return "Schedule It"
        elif self.importance==2 and self.urgency==1:
            self.eisenhower_id=3
            return "Delegate It"
        elif self.importance==2 and self.urgency==2:
            self.eisenhower_id=4
            return "Delete It"