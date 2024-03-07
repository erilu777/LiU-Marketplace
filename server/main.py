from flask import Flask, request
from flask import jsonify
from flask import abort
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, 
static_folder='../client', 
static_url_path='/')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/")
def client():
  return app.send_static_file("client.html")



class User:
    name = db.Column(db.String(80), unique=True, nullable=False, primary_key=False)
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, primary_key=False)
    year = db.Column(db.Integer, unique=False, nullable=True, primary_key=False)
    program = db.Column(db.String(80), unique=False, nullable=True, primary_key=False)
        

if __name__ == "__main__":
    app.run(port=5000)
