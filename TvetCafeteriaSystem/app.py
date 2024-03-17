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

# CRUD Operations for Users
    
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
            "role": user.role
        } for user in users]

    return jsonify(results), 200

#Update User Detail
@app.route('/api/users/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    data = request.json
    user = Users.query.get_or_404(user_id)

    user.username = data.get('username')
    user.password = data.get('password')
    user.role = data.get('role')

    db.session.commit()

    return jsonify({'message': 'User updated successfully!'}), 200


#Delete User
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    user = Users.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'User deleted successfully!'}), 200

#CRUD Operations for Locations

#Create Locations
@app.route('/api/locations', methods=['POST'])
@jwt_required()
def create_location():
    data = request.json
    location_id = data.get('location_id')
    location_name = data.get('location_name')

    location = Locations(location_id=location_id, location_name=location_name)
    db.session.add(location)
    db.session.commit()

    return jsonify({'message': 'Location created successfully!'}), 201

#Get all locations
@app.route('/api/locations', methods=['GET'])
@jwt_required()
def get_locations():
    locations = Locations.query.all()
    results = [
        {
            "location_id": location.location_id,
            "location_name": location.location_name
        } for location in locations]

    return jsonify(results), 200

#Update Location Detail
@app.route('/api/locations/<int:location_id>', methods=['PUT'])
@jwt_required()
def update_location(location_id):
    data = request.json
    location = Locations.query.get_or_404(location_id)

    location.location_name = data.get('location_name')

    db.session.commit()

    return jsonify({'message': 'Location updated successfully!'}), 200

#Delete Location
@app.route('/api/locations/<int:location_id>', methods=['DELETE'])
@jwt_required()
def delete_location(location_id):
    location = Locations.query.get_or_404(location_id)
    db.session.delete(location)
    db.session.commit()

    return jsonify({'message': 'Location deleted successfully!'}), 200


#Bookshop CRUD Operations

#Add Bookshop

#Get List Of Bookshops

#Update Bookshop

#Delete Bookshop




#Cafeteria CRUD Operations

#Add Cafeteria

#Get List Of Cafeterias

#Update Cafeteria

#Delete Cafeteria


#Digital Center CRUD Operations

#Add Digital Center


#Get List Of Digital Centers

#Update Digital Center

#Delete Digital Center


#Pharmacy CRUD Operations

#Add Pharmacy

#Get List Of Pharmacies

#Update Pharmacy

#Delete Pharmacy


#Product CRUD Operations

#Add Product

#Get List Of Products

#Update Product


#Delete Product


#Tuck Shop CRUD Operations

#Add Tuck Shop

#Get List Of Tuck Shops

#Update Tuck Shop

#Delete Tuck Shop


#Orders CRUD Operations

#Add Order

#Get List Of Orders

#Update Order

#Delete Order

#Landing Page Analytics

#Get Total Sales

#Get Total Orders

#Get Total Users

#Get Total Products



if __name__ == '__main__':
    app.run(debug=True)
