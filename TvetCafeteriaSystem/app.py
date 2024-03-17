from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from datetime import timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:taylorgang@localhost/TvetCafeteria'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'TVETCafeteriaAPP'  # Change this to a random long string
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)

db = SQLAlchemy(app)
jwt = JWTManager(app)


# Database models
# Bookshop Model
class Bookshop(db.Model):
    bookshop_id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.String(100))
    bookshop_name = db.Column(db.String(100))
    
# Cafeteria Model
class Cafeteria(db.Model):
    cafeteria_id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.String(100))
    cafeteria_name = db.Column(db.String(100))

# Digital Center Model
class DigitalCenter(db.Model):
    digital_center_id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.String(100))
    digital_center_name = db.Column(db.String(100))


# Locations Model
class Locations(db.Model):
    location_id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(100))

# Orders Model
class Orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    total = db.Column(db.Float)
    order_date = db.Column(db.DateTime)

# Pharmacy Model
class Pharmacy(db.Model):
    pharmacy_id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.String(100))
    pharmacy_name = db.Column(db.String(100))

# Product Model
class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.String(100))
    product_name = db.Column(db.String(100))
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    category = db.Column(db.String(100))

# Tuck_shop Model
class Tuck_shop(db.Model):
    tuck_shop_id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.String(100))
    tuck_shop_name = db.Column(db.String(100))

# Users Model
class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    role = db.Column(db.String(100))

# Routes

#Register a user  
@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    user_id = data.get('user_id')
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    user = Users(username=username, password=password, role=role)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created successfully!'}), 201

#Login a user
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = Users.query.filter_by(username=username, password=password).first()
    if user:
        access_token = create_access_token(identity=user.user_id)
        return jsonify(
            {'message': 'Login successfull',
                'access_token': access_token}
            ), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

#Get all users
@app.route('/api/users', methods=['GET'])
@jwt_required()
def get_users():
    users = Users.query.all()
    results = [
        {
            "user_id": user.user_id,
            "username": user.username,
            "password": user.password,
            "role": user.role
        } for user in users]

    return jsonify(results), 200



if __name__ == '__main__':
    app.run(debug=True)
