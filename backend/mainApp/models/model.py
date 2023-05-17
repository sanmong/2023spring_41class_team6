from mainApp import db

class Documents(db.Model):
    docid = db.Column(db.Integer, primary_key=True, nullable=False)
    contents = db.Column(db.Longtext, nullable=False)
    date = db.Column(db.Date)
    source = db.Column(db.Text)

class Chatroom(db.Model):
    chatroom_id = db.Column(db.Integer, primary_key=True, nullable=False)
    chat_start = db.Column(db.Datetime, nullable=False)
    last_interaction = db.Column(db.Datetime, nullable=False)

class Individual_chats(db.Model):
    chat_id = db.Column(db.Integer, primary_key=True, nullable=False)
    chatroom_id = db.Column(db.Integer, foreign_key=True, nullable=False)
    order = db.Column(db.Integer, nullable=False)
    is_system = db.Column(db.Boolean, nullable=False)
    docid = db.Column(db.Integer)
