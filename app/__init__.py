# Initialize the Flask application.
# Import blueprints for route registration

from flask import Flask
from app.routes import user_routes
from app.database import db

def create_app():
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///RedApple.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    with app.app_context():
        db.create_all()
    
    app.register_blueprint(user_routes)
    return app



# Creates a Flask application.
# Configures the app to use a database.
# Registers the routes (endpoints).

