from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from mainApp.models.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_app():
    app = Flask(__name__)

    #routes list
    from .routes import routes_list
    routes_list(app)

    @app.route('/')
    def hello_world():
        return 'hello world!'
    
    return app