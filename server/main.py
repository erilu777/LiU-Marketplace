from flask import Flask, request
from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


app = Flask(__name__, 
static_folder='../client', 
static_url_path='/')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
##jwt = JWTManager(app)


class User(db.Model):
    name = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=False)
    email = db.Column(db.String(120), unique=True, nullable=True, primary_key=False)
    liuId = db.Column(db.String(80), unique=True, nullable=True, primary_key=False)
    year = db.Column(db.Integer, unique=False, nullable=True, primary_key=False)
    program = db.Column(db.String(80), unique=False, nullable=True, primary_key=False)
    isAdmin = db.Column(db.Boolean, unique=False, nullable=True, primary_key=False)
    nmSoldItems = db.Column(db.Integer, unique=False, nullable=True, primary_key=False)
    #items = db.relationship('Item', backref='user', lazy=True)
  
    def __repr__(self):
        return f'<User {self.id} {self.name} {self.email} {self.year} {self.program} {self.nmSoldItems}>'

    def serialize(self):
        return {
          'name': self.name,
          'id': self.id,
          'email': self.email,
          'liuId': self.liuId,
          'year': self.year,
          'program': self.program,
          'isAdmin': self.isAdmin,
          'nmSoldItems': self.nmSoldItems
      }
        

class Item(db.Model):
    name = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    id = db.Column(db.Integer, unique=True, nullable=True, primary_key=False)
    price = db.Column(db.Float, unique=False, nullable=True, primary_key=False)
    category = db.Column(db.String(80), unique=False, nullable=True, primary_key=False)
    description = db.Column(db.String(120), unique=False, nullable=True, primary_key=False)
    isSold = db.Column(db.Boolean, unique=False, nullable=True, primary_key=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
   
    def __repr__(self):
        return f'<Item {self.name}: {self.id} {self.category} {self.description}>'

    def serialize(self):
        return {
          'name': self.name,
          'id': self.id,
        #  'price': self.price,
          'category': self.category,
          'description': self.description,
          'isSold': self.isSold
      }

@app.route("/")
def client():
  return app.send_static_file("client.html")

@app.route("/login", methods=["POST"])
def login():
    pass
    #TODO: Implement SSO login

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        all_users = User.query.all()
        return jsonify([user.serialize() for user in all_users])
    elif request.method == 'POST':
        data = request.get_json()
        new_user = User(name=data['name'], email=data['email'], liuId=data['liuId'])
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
        new_item = Item(name=data['name'])
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
            item.name = data['name']
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


