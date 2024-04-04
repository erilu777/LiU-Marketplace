from flask import Flask, jsonify, abort, request
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
    liu_id = db.Column(db.String, nullable=False)
    #email = db.Column(db.String)
    program = db.Column(db.String)
    year = db.Column(db.Integer)
    is_admin = db.Column(db.Boolean, default=False)
    num_sold_items = db.Column(db.Integer, default=0)
    num_bought_items = db.Column(db.Integer, default=0)
    #items = db.relationship('Item', backref="user", foreign_keys="Item.user_id")
    sold_items = db.relationship('Item', backref="seller", foreign_keys="Item.seller_id")
    bought_items = db.relationship('Item', backref="buyer", foreign_keys="Item.buyer_id")

    @property
    def email(self):
        return self.liu_id + "@student.liu.se"

    def __repr__(self):
        return f"<User {self.id} : {self.name} {self.email}  {self.liu_id} {self.program} {self.year} {self.is_admin} {self.num_sold_items} {self.num_bought_items}>"

    def serialize(self):
        return {
            "id":self.id,
            "name": self.name,
            "email":self.email,
            "liu_id":self.liu_id,
            "program":self.program,
            "year":self.year,
            "is_admin":self.is_admin,
            "num_sold_items":self.num_sold_items,
            "num_bought_items":self.num_bought_items
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

    def serialize(self):
        return {
            'value': self.value,
            'name': self.name
        }

class Condition(Enum):
    Nytt = 1
    Använd_Nyskick = 2
    Använd_Gott_skick = 3
    Använd_Slitet_skick = 4
    
    def serialize(self):
        return {
            'value': self.value,
            'name': self.name
        }


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
    category = db.Column(db.Enum(Category), nullable=True)
    condition = db.Column(db.Enum(Condition), nullable=True)
    is_sold = db.Column(db.Boolean, default=False)
    images = relationship("ItemImage", backref="item")
    seller_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    buyer_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)

    def __repr__(self):
        return f'<Item {self.id} : {self.title} {self.description} {self.price} {self.category} {self.condition} {self.is_sold} {self.seller_id} {self.buyer_id} {self.images} >'

    def serialize(self):
        seller_data = self.seller.serialize() if self.seller else None
        buyer_data = self.buyer.serialize() if self.buyer else None
        return {
            "id":self.id,
            "title": self.title,
            "description":self.description,
            "price":self.price,
            "category": self.category.name if self.category else None,
            "condition":self.condition.name if self.condition else None,
            "is_sold":self.is_sold,
            "images": [image.serialize() for image in self.images],
            "seller": seller_data,
            "buyer": buyer_data
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
        if 'num_sold_items' in data:
            user.num_sold_items = data['num_sold_items']
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
        new_item = Item(title=data.get('title'), description=data.get("description"), price=data.get("price"), category=Category[data.get("category")], condition=Condition[data.get("condition")])
        if 'seller_id' in data:
            seller = User.query.get(data['seller_id'])
            if seller:
                new_item.seller = seller
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
        if 'title' in data:
            item.title = data['title']
        if 'description' in data:
            item.description = data['description']
        if 'price' in data:
            item.price = data['price']
        if 'category' in data:
            item.category = data['category']
        if 'condition' in data:
            item.condition = data['condition']
        if 'is_sold' in data:
            item.is_sold = data['is_sold']
        db.session.commit()
        return jsonify(item.serialize()), 200
    elif request.method == 'DELETE':
        db.session.delete(item)
        db.session.commit()
        return '', 200

@app.route('/items/<int:item_id>/sell', methods=['PUT'])
def sell_item(item_id):
    item = Item.query.get(item_id)
    if item is None:
        abort(404)

    data = request.get_json()
    if 'buyer_id' not in data:
        abort(400, description="buyer_id is required")

    buyer = User.query.get(data['buyer_id'])
    if buyer is None:
        abort(404, description="buyer_id is invalid")

    seller = User.query.get(item.seller_id)
    # if user is None:
        # abort(404, description="user_id is invalid")
    # Felhantering behövs ej för en item kommer alltid att ha en user...?

    item.buyer = buyer
    item.is_sold = True
    seller.num_sold_items += 1
    buyer.num_bought_items += 1
    db.session.commit()

    # TODO: Send an email to the buyer

    return jsonify(item.serialize()), 200


if __name__ == "__main__":
    with app.app_context():
        #db.drop_all() # Drop all tables before creating them, to avoid conflicts
        db.create_all()
    app.run(port=5000)


