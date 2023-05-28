from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models.database import SessionLocal
from routes import routes_list

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = Flask(__name__)

#routes list
routes_list(app)

@app.route('/')
def hello_world():
    return 'hello world!'

if __name__=='__main__':
    app.run()