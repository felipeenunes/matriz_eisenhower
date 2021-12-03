from flask import request, current_app, jsonify
from app.models.category_model import CategoryModel
from app.models.exc import OutOfRangeError, NotFoundError
from app.models.task_model import TaskModel
from sqlalchemy.exc import IntegrityError

def create_task():
    try:
        session = current_app.db.session
        data = request.get_json()
        categories = data.pop('categories')
        task = TaskModel(**data)
        message = task.verify_eisenhower()
        for category in categories:
            category_name = CategoryModel.query.filter_by(name=category['name']).first()
            if not category_name:
                new_category = CategoryModel(**category)
                session.add(new_category)
                category_name = CategoryModel.query.filter_by(name=category['name']).first()
            task.categories.append(category_name)
        session.add(task)
        session.commit()    
        
        return jsonify({
            "id": task.id,
            "name": task.name,
            "description": task.description,
            "duration": task.duration,
            "eisenhower_classification": message,
            "categories": categories
        }), 201
    except OutOfRangeError as err:
        return jsonify(err.message), err.code
    except IntegrityError as err:
        return jsonify({"message": "Task already exists!"}), 409

def update_task(id: int):
    try:
        session = current_app.db.session
        data = request.get_json()
        task = TaskModel.query.get(id)
        if not task:
            raise NotFoundError("ID not found.")
        for key, value in data.items():
            setattr(task, key, value)
            message = task.verify_eisenhower()
        session.add(task)
        session.commit()
        return {
            "id": task.id,
            "name": task.name,
            "description": task.description,
            "duration": task.duration,
            "eisenhower_classification": message

        }, 200
    except NotFoundError as err:
        return {"message": err.message}, err.code

def delete_task(id: int):
    try:
        session = current_app.db.session
        task = TaskModel.query.get(id)
        if not task:
            raise NotFoundError("ID not found.")
        session.delete(task)
        session.commit()
        return {}, 204
    except NotFoundError as err:
        return jsonify({"message": err.message}), err.code