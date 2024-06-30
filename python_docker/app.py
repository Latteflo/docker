from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def hello():
    app_name = os.getenv("APP_NAME", "Docker")
    return f"Hello, {app_name}!"


@app.route('/api')
def api():
    return {"message": "Welcome to the API!"}


@app.route('/add_user/<name>')
def add_user(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return {"message": f"User {name} added!"}


@app.route('/users')
def get_users():
    users = User.query.all()
    return {"users": [user.name for user in users]}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
