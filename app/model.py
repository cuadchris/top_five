from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:test123@localhost/rappers"

db.init_app(app)

class Rapper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    bio = db.Column(db.String)

with app.app_context():
    topfive = db.session.query(Rapper).order_by(Rapper.id).all()