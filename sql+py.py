from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:7d5ef1@127.0.0.1:5432/try'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
# 🔗 إنشاء كائن SQLAlchemy
db = SQLAlchemy(app)
# 🧪 نموذج تجريبي: منتج
class Product4(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    price = db.Column(db.Integer, nullable=True) 
    description = db.Column(db.String(10000), nullable=True)

# 🏠 صفحة رئيسية
@app.route('/')
def home():
    return '✔️ PostgreSQL connected to Flask!'

if __name__ == '__main__':
    with app.app_context():
      db.create_all()
   
    app.run(debug=True)