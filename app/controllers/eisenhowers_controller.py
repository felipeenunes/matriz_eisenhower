from flask import request, current_app, jsonify
from app.models.eisenhowers_model import EisenhowerModel

def create_eisenhower():
    session = current_app.db.session

    data = request.get_json()

    eisenhower = EisenhowerModel(**data)

    session.add(eisenhower)
    session.commit()

    return jsonify({
        "type": eisenhower.type
    }), 201