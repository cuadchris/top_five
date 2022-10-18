from app import app, db

class Rapper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    bio = db.Column(db.String)

with app.app_context():
    topfive = db.session.query(Rapper).order_by(Rapper.id).all()