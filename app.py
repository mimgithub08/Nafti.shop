from flask import Flask
import os

from model import db
from route_admin import init_routes
from route_user import init_routes

app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:7d5ef1@127.0.0.1:5432/try'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db.init_app(app)
init_routes(app)
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True,port=7000)


