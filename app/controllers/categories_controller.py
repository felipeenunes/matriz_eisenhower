from flask import request, current_app, jsonify
from app.models.category_model import CategoryModel
from sqlalchemy.exc import IntegrityError
from app.models.exc import NotFoundError

def create_category():
    try:
        session = current_app.db.session
        data = request.get_json()
        category = CategoryModel(**data)

        session.add(category)
        session.commit()

        return jsonify({
            "id": category.id,
            "name": category.name,
            "description": category.description,
        }), 201
    except IntegrityError:
        return jsonify({"message": "Category already exists!"}), 409

def update_category(id: int):
    try:
        session = current_app.db.session
        data = request.get_json()
        category = CategoryModel.query.get(id)
        if not category:
            raise NotFoundError("ID not found.")
        for key, value in data.items():
            setattr(category, key, value)
        session.add(category)
        session.commit()
        return {
            "id": category.id,
            "name": category.name,
            "description": category.description
        }, 200
    except NotFoundError as err:
        return {"message": err.message}, err.code

def delete_category(id: int):
    try:
        session = current_app.db.session
        category = CategoryModel.query.get(id)
        if not category:
            raise NotFoundError("ID not found.")
        session.delete(category)
        session.commit()
        return {}, 204
    except NotFoundError as err:
        return jsonify({"message": err.message}), err.code

def get_all():
    try:
        categories = CategoryModel.query.all()
        if not categories:
            raise NotFoundError("Empty!")
        category_list = []
        for category in categories:
            tasks = []
            for task in category.tasks:
                if task.eisenhower_id == 1:
                    priority = "Do It First"
                if task.eisenhower_id == 2:
                    priority = "Schedule It"
                if task.eisenhower_id == 3:
                    priority = "Delegate It"
                if task.eisenhower_id == 4:
                    priority = "Delete It"
                task = {
                    "id": task.id,
                    "name": task.name,
                    "description": task.description,
                    "priority": priority
                }
                tasks.append(task)
            serializer = {
                "id": category.id,
                "name": category.name,
                "description": category.description,
                "tasks": tasks
            }
            category_list.append(serializer)
        return jsonify(serializer), 200
    except NotFoundError as err:
        return {"message": err.message}, err.code