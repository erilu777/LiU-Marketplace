from flask import Flask, request
from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from sqlalchemy.orm import relationship
from enum import Enum


app = Flask(__name__, 
static_folder='../client', 
static_url_path='/')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
##jwt = JWTManager(app)

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    liu_id = db.Column(db.String, nullable=False)
    program = db.Column(db.String)
    year = db.Column(db.Integer)
    is_admin = db.Column(db.Boolean)
    numSoldItems = db.Column(db.Integer)
    items = db.relationship('Item', backref="user")

    def __repr__(self):
        return f"<User {self.id} {self.name} {self.email}  {self.liu_id} {self.program} {self.year} {self.is_admin} {self.numSoldItems} {self.items}>"

    def serialize(self):
        return {
            "id":self.id,
            "name": self.name,
            "email":self.email,
            "liu_id":self.liu_id,
            "program":self.program,
            "year":self.year,
            "is_admin":self.is_admin,
            "numSoldItems":self.numSoldItems,
        } 
        
class Category(Enum):
    Cyklar = 1
    Kurslitteratur = 2
    Böcker = 3
    Biljetter = 4
    Inredning = 5
    Bostad = 6
    Verktyg = 7
    Övrigt = 8

class Condition(Enum):
    Nytt = 1
    Använd_Nyskick = 2
    Använd_Gott_skick = 3
    Använd_Slitet_skick = 4

class ItemImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(120))
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"))
    
    def serialize(self):
        return {
            "id":self.id,
            "image_path": self.image_path,
            "item_id":self.item_id
        }
    
class Item(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(120))
    price = db.Column(db.Integer)
    category = db.Column(db.Enum(Category))
    is_sold = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    images = relationship("ItemImage", backref="item")
    condition = db.Column(db.Enum(Condition))
            
    def __repr__(self):
        return f'<Item {self.title}>'

    def serialize(self):
        return {
            "id":self.id,
            "title": self.title,
            "description":self.description,
            "price":self.price,
            "category":self.category.name,
            "is_sold":self.is_sold,
            "user_id":self.user_id,
            "images": [image.serialize() for image in self.images],
            "condition":self.condition
        }

@app.route("/")
def client():
  return app.send_static_file("client.html")

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        all_users = User.query.all()
        return jsonify([user.serialize() for user in all_users])
    elif request.method == 'POST':
        data = request.get_json()
        new_user = User(name=data.get('name'), liu_id=data.get("liu_id"), program=data.get("program"), year=data.get("year"))
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.serialize()), 201

    
@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_users(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404)
    if request.method == 'GET':
        return jsonify(user.serialize())
    elif request.method == 'PUT':
        data = request.get_json()
        if 'is_admin' in data:
            user.is_admin = data['is_admin']
        if 'nmSoldItems' in data:
            user.nmSoldItems = data['nmSoldItems']
        if 'year' in data:
            user.year = data['year']
        if 'program' in data:
            user.program = data['program']
        db.session.commit()
        return jsonify(user.serialize()), 200
    elif request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return '', 200
    
@app.route('/items', methods=['GET', 'POST'])
def items():
    if request.method == 'GET':
        all_items = Item.query.all()
        return jsonify([item.serialize() for item in all_items])
    elif request.method == 'POST':
        data = request.get_json()
        new_item = Item(title=data['title'], price=data["price"], category=data["category"], description=data["description"], is_sold=data["is_sold"], user_id=data["user_id"])
        db.session.add(new_item)
        db.session.commit()
        return jsonify(new_item.serialize()), 201
    
@app.route('/items/<int:item_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_items(item_id):
    item = Item.query.get(item_id)
    if item is None:
        abort(404)
    if request.method == 'GET':
        return jsonify(item.serialize())
    elif request.method == 'PUT':
        data = request.get_json()
        if 'name' in data:
            item.title = data['title']
        if 'price' in data:
            item.price = data['price']
        if 'category' in data:
            item.category = data['category']
        if 'description' in data:
            item.description = data['description']
        if 'isSold' in data:
            item.isSold = data['isSold']
        db.session.commit()
        return jsonify(item.serialize()), 200
    elif request.method == 'DELETE':
        db.session.delete(item)
        db.session.commit()
        return '', 200
        
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=5000)


