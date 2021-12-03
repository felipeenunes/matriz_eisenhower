from flask import Flask

def init_app(app: Flask) -> None:

    from .task_blueprint import bp as bp_tasks
    app.register_blueprint(bp_tasks)

    from .eisenhowers_blueprint import bp as bp_eisenhowers
    app.register_blueprint(bp_eisenhowers)

    from .category_blueprint import bp as bp_category
    app.register_blueprint(bp_category)