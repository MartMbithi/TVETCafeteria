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
class Products(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.String(100))
    product_name = db.Column(db.String(100))
    product_name = db.Column(db.String(100))
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
@app.route('/api/bookshops', methods=['POST'])
@jwt_required()
def create_bookshop():
    data = request.json
    bookshop_id = data.get('bookshop_id')
    location_id = data.get('location_id')
    bookshop_name = data.get('bookshop_name')

    bookshop = Bookshop(bookshop_id=bookshop_id, location_id=location_id, bookshop_name=bookshop_name)
    db.session.add(bookshop)
    db.session.commit()

    return jsonify({'message': 'Bookshop created successfully!'}), 201

#Get List Of Bookshops
@app.route('/api/bookshops', methods=['GET'])
@jwt_required()
def get_bookshops():
    bookshops = Bookshop.query.all()
    results = [
        {
            "bookshop_id": bookshop.bookshop_id,
            "location_id": bookshop.location_id,
            "bookshop_name": bookshop.bookshop_name
        } for bookshop in bookshops]

    return jsonify(results), 200


#Update Bookshop
@app.route('/api/bookshops/<int:bookshop_id>', methods=['PUT'])
@jwt_required()
def update_bookshop(bookshop_id):
    data = request.json
    bookshop = Bookshop.query.get_or_404(bookshop_id)

    bookshop.location_id = data.get('location_id')
    bookshop.bookshop_name = data.get('bookshop_name')

    db.session.commit()

    return jsonify({'message': 'Bookshop updated successfully!'}), 200


#Delete Bookshop
@app.route('/api/bookshops/<int:bookshop_id>', methods=['DELETE'])
@jwt_required()
def delete_bookshop(bookshop_id):
    bookshop = Bookshop.query.get_or_404(bookshop_id)
    db.session.delete(bookshop)
    db.session.commit()

    return jsonify({'message': 'Bookshop deleted successfully!'}), 200



#Cafeteria CRUD Operations

#Add Cafeteria
@app.route('/api/cafeterias', methods=['POST'])
@jwt_required()
def create_cafeteria():
    data = request.json
    cafeteria_id = data.get('cafeteria_id')
    location_id = data.get('location_id')
    cafeteria_name = data.get('cafeteria_name')

    cafeteria = Cafeteria(cafeteria_id=cafeteria_id, location_id=location_id, cafeteria_name=cafeteria_name)
    db.session.add(cafeteria)
    db.session.commit()

    return jsonify({'message': 'Cafeteria created successfully!'}), 201


#Get List Of Cafeterias
@app.route('/api/cafeterias', methods=['GET'])
@jwt_required()
def get_cafeterias():
    cafeterias = Cafeteria.query.all()
    results = [
        {
            "cafeteria_id": cafeteria.cafeteria_id,
            "location_id": cafeteria.location_id,
            "cafeteria_name": cafeteria.cafeteria_name
        } for cafeteria in cafeterias]

    return jsonify(results), 200


#Update Cafeteria
@app.route('/api/cafeterias/<int:cafeteria_id>', methods=['PUT'])
@jwt_required()
def update_cafeteria(cafeteria_id):
    data = request.json
    cafeteria = Cafeteria.query.get_or_404(cafeteria_id)

    cafeteria.location_id = data.get('location_id')
    cafeteria.cafeteria_name = data.get('cafeteria_name')

    db.session.commit()

    return jsonify({'message': 'Cafeteria updated successfully!'}), 200



#Delete Cafeteria
@app.route('/api/cafeterias/<int:cafeteria_id>', methods=['DELETE'])
@jwt_required()
def delete_cafeteria(cafeteria_id):
    cafeteria = Cafeteria.query.get_or_404(cafeteria_id)
    db.session.delete(cafeteria)
    db.session.commit()

    return jsonify({'message': 'Cafeteria deleted successfully!'}), 200



#Digital Center CRUD Operations

#Add Digital Center
@app.route('/api/digital_centers', methods=['POST'])
@jwt_required()
def create_digital_center():
    data = request.json
    digital_center_id = data.get('digital_center_id')
    location_id = data.get('location_id')
    digital_center_name = data.get('digital_center_name')

    digital_center = DigitalCenter(digital_center_id=digital_center_id, location_id=location_id, digital_center_name=digital_center_name)
    db.session.add(digital_center)
    db.session.commit()

    return jsonify({'message': 'Digital Center created successfully!'}), 201



#Get List Of Digital Centers
@app.route('/api/digital_centers', methods=['GET'])
@jwt_required()
def get_digital_centers():
    digital_centers = DigitalCenter.query.all()
    results = [
        {
            "digital_center_id": digital_center.digital_center_id,
            "location_id": digital_center.location_id,
            "digital_center_name": digital_center.digital_center_name
        } for digital_center in digital_centers]

    return jsonify(results), 200


#Update Digital Center
@app.route('/api/digital_centers/<int:digital_center_id>', methods=['PUT'])
@jwt_required()
def update_digital_center(digital_center_id):
    data = request.json
    digital_center = DigitalCenter.query.get_or_404(digital_center_id)

    digital_center.location_id = data.get('location_id')
    digital_center.digital_center_name = data.get('digital_center_name')

    db.session.commit()

    return jsonify({'message': 'Digital Center updated successfully!'}), 200

#Delete Digital Center
@app.route('/api/digital_centers/<int:digital_center_id>', methods=['DELETE'])
@jwt_required()
def delete_digital_center(digital_center_id):
    digital_center = DigitalCenter.query.get_or_404(digital_center_id)
    db.session.delete(digital_center)
    db.session.commit()

    return jsonify({'message': 'Digital Center deleted successfully!'}), 200



#Pharmacy CRUD Operations

#Add Pharmacy
@app.route('/api/pharmacies', methods=['POST'])
@jwt_required()
def create_pharmacy():
    data = request.json
    pharmacy_id = data.get('pharmacy_id')
    location_id = data.get('location_id')
    pharmacy_name = data.get('pharmacy_name')

    pharmacy = Pharmacy(pharmacy_id=pharmacy_id, location_id=location_id, pharmacy_name=pharmacy_name)
    db.session.add(pharmacy)
    db.session.commit()

    return jsonify({'message': 'Pharmacy created successfully!'}), 201


#Get List Of Pharmacies
@app.route('/api/pharmacies', methods=['GET'])
@jwt_required()
def get_pharmacies():
    pharmacies = Pharmacy.query.all()
    results = [
        {
            "pharmacies": pharmacy.pharmacy_id,
            "location_id": pharmacy.location_id,
            "pharmacy_name": pharmacy.pharmacy_name
        } for pharmacy in pharmacies]

    return jsonify(results), 200


#Update Pharmacy
@app.route('/api/pharmacies/<int:pharmacy_id>', methods=['PUT'])
@jwt_required()
def update_pharmacy(pharmacy_id):
    data = request.json
    pharmacy = Pharmacy.query.get_or_404(pharmacy_id)

    pharmacy.location_id = data.get('location_id')
    pharmacy.pharmacy_name = data.get('pharmacy_name')

    db.session.commit()

    return jsonify({'message': 'Pharmacy updated successfully!'}), 200


#Delete Pharmacy
@app.route('/api/pharmacies/<int:pharmacy_id>', methods=['DELETE'])
@jwt_required()
def delete_pharmacy(pharmacy_id):
    pharmacy = Pharmacy.query.get_or_404(pharmacy_id)
    db.session.delete(pharmacy)
    db.session.commit()

    return jsonify({'message': 'Pharmacy deleted successfully!'}), 200



#Product CRUD Operations

#Add Product
@app.route('/api/products', methods=['POST'])
@jwt_required()
def create_product():
    data = request.json
    product_id = data.get('product_id')
    location_id = data.get('location_id')
    product_name = data.get('product_name')
    price = data.get('price')
    category = data.get('category')

    products = Products(product_id=product_id, location_id=location_id,  product_name=product_name, price=price, category=category)
    db.session.add(products)
    db.session.commit()

    return jsonify({'message': 'Product created successfully!'}), 201

#Get List Of Products
@app.route('/api/products', methods=['GET'])
@jwt_required()
def get_products():
    products = Products.query.all()
    results = [
        {
            "product_id": product.product_id,
            "location_id": product.location_id,
            "product_name": product.product_name,
            "price": product.price,
            "category": product.category
        } for product in products]

    return jsonify(results), 200


#Update Product
@app.route('/api/products/<int:product_id>', methods=['PUT'])
@jwt_required()
def update_product(product_id):
    data = request.json
    product = Products.query.get_or_404(product_id)

    product.location_id = data.get('location_id')
    product.product_name = data.get('product_name')
    product.price = data.get('price')
    product.category = data.get('category')

    db.session.commit()

    return jsonify({'message': 'Product updated successfully!'}), 200

#Delete Product
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
@jwt_required()
def delete_product(product_id):
    product = Products.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()

    return jsonify({'message': 'Product deleted successfully!'}), 200



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
