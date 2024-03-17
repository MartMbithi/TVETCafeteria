# TVET College Application Project API End Points
A local TVET college looks to expand its entrepreneurial activities within its 5 locations around Machakos County. As part of its innovative strategy, the college seeks to have an online presence with an ecommerce web app. This will allow students, staff and guests to access services and products available to the college cafeteria, tuck shops, pharmacy, bookshop and digital center.
# 📁 Folder: Users 


## End-point: Register User
The Register User endpoint allows new users to create an account within the TVET college ecommerce application. Users can register by providing a unique username, a strong password, and specifying their role (e.g.,student, staff, or guest). Upon successful registration, the user will  
be able to access the application's features and functionalities.
### Method: POST
>```
>http://127.0.0.1:5000/api/register
>```
### Body (**raw**)

```json
 {
    "user_id": 8,
    "username": "",
    "password" : "TestPassword20",
    "role": "Staff"

}

```

### 🔑 Authentication noauth

|Param|value|Type|
|---|---|---|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Login User
### Method: POST
>```
>http://127.0.0.1:5000/api/login
>```
### Body (**raw**)

```json
{
    "username":"James Monroe",
    "password": "TestPassword20",
    "role" : "Staff"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Read Users
### Method: GET
>```
>http://127.0.0.1:5000/api/users
>```
### Body (**raw**)

```json

```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Update User
### Method: PUT
>```
>http://127.0.0.1:5000/api/users/11
>```
### Body (**raw**)

```json
{
    "username":"Jane_Smith",
    "password":"Test125",
    "role":"Admin"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Delete User
### Method: DELETE
>```
>http://127.0.0.1:5000/api/users/13
>```
### Body (**raw**)

```json

```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
# 📁 Folder: Locations 


## End-point: Register Location
### Method: POST
>```
>http://127.0.0.1:5000/api/locations
>```
### Body (**raw**)

```json
{
    "location_id": "5",
    "location_name": "Mumbuni - Along Machakos Kangundo Road"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get All Locations
### Method: GET
>```
>http://127.0.0.1:5000/api/locations
>```
### Body (**raw**)

```json

```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Update Locations
### Method: PUT
>```
>http://127.0.0.1:5000/api/locations/2
>```
### Body (**raw**)

```json
{
    "location_name" : "Katheka Kai Along Machakos Nairobi Road"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Delete Location
### Method: DELETE
>```
>http://127.0.0.1:5000/api/locations/1
>```
### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
# 📁 Folder: Bookshop 


## End-point: Register Bookshops
### Method: POST
>```
>http://127.0.0.1:5000/api/bookshops
>```
### Body (**raw**)

```json
{
    "bookshop_id" : "3",
    "location_id" : "2",
    "bookshop_name" : "Twiga Tertiary Learners Bookshop"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get Bookshops
### Method: GET
>```
>http://127.0.0.1:5000/api/bookshops
>```
### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Update Bookshop
### Method: PUT
>```
>http://127.0.0.1:5000/api/bookshops/1
>```
### Body (**raw**)

```json
{
    "location_id" : "5",
    "bookshop_name" : "Twiga Junior Learners Bookshop"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Delete Bookshop
### Method: DELETE
>```
>http://127.0.0.1:5000/api/bookshops/1
>```
### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
# 📁 Folder: Cafeteria 


## End-point: Add Cafeteria
### Method: POST
>```
>http://127.0.0.1:5000/api/cafeterias
>```
### Body (**raw**)

```json
{
    "cafeteria_id" : "4",
    "location_id" : "3",
    "cafeteria_name" : "TVET Mess Four"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get Cafeterias
### Method: GET
>```
>http://127.0.0.1:5000/api/cafeterias
>```
### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Update Cafeteria
### Method: PUT
>```
>http://127.0.0.1:5000/api/cafeterias/1
>```
### Body (**raw**)

```json
{
    "location_id" : "3",
    "cafeteria_name" : "TVET Fast Foods"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Delete Request
### Method: DELETE
>```
>http://127.0.0.1:5000/api/cafeterias/5
>```
### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
# 📁 Folder: Digital Centers 


## End-point: Add Digital Centers
### Method: POST
>```
>http://127.0.0.1:5000/api/digital_centers
>```
### Body (**raw**)

```json
{
    "digital_center_id" : "5",
    "location_id" : "5",
    "digital_center_name" : "TVET Medical Trainees Center"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get Centers
### Method: GET
>```
>http://127.0.0.1:5000/api/digital_centers
>```
### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Update Centers
### Method: PUT
>```
>http://127.0.0.1:5000/api/digital_centers/1
>```
### Body (**raw**)

```json
{
    "location_id" : "2",
    "digital_center_name" : "TVET Students Cyber Cafe"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Delete Center
### Method: DELETE
>```
>http://127.0.0.1:5000/api/digital_centers/4
>```
### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
# 📁 Folder: Pharmacies 


## End-point: Add Pharmacy
### Method: POST
>```
>http://127.0.0.1:5000/api/pharmacies
>```
### Body (**raw**)

```json
{
    "pharmacy_id" : "3",
    "location_id" : "4",
    "pharmacy_name" : "TVET Informary 003"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get Pharmacies
### Method: GET
>```
>http://127.0.0.1:5000/api/pharmacies
>```
### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Update Pharmacies
### Method: PUT
>```
>http://127.0.0.1:5000/api/pharmacies/1
>```
### Body (**raw**)

```json
{
    "location_id" : "3",
    "pharmacy_name" : "New TVET Informary"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Delete Pharmacy
### Method: DELETE
>```
>http://127.0.0.1:5000/api/pharmacies/3
>```
### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
# 📁 Folder: Products 


## End-point: Add Product
### Method: POST
>```
>http://127.0.0.1:5000/api/products
>```
### Body (**raw**)

```json
{
    "product_id" : "4",
    "location_id" : "2",
    "product_name" : "Brufen BP 500MG",
    "price" : "2500",
    "category" : "Pharmaceuticals"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get Products
### Method: GET
>```
>http://127.0.0.1:5000/api/products
>```
### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Update Products
### Method: PUT
>```
>http://127.0.0.1:5000/api/products/1
>```
### Body (**raw**)

```json
{
    "location_id" : "3",
    "product_name" : "Malaria Tablets",
    "price" : "4500",
    "category": "Pharmaceuticals"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: New Request
### Method: DELETE
>```
>http://127.0.0.1:5000/api/products/1
>```
### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
# 📁 Folder: Tuck Shop 


## End-point: Add Tuckshop
### Method: POST
>```
>http://127.0.0.1:5000/api/tuck_shops
>```
### Body (**raw**)

```json
{
    "tuck_shop_id" : "4",
    "location_id" : "4",
    "tuck_shop_name" : "TVET Green Groceries Mini Mart"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get Tuckshops
### Method: GET
>```
>http://127.0.0.1:5000/api/tuck_shops
>```
### Body (**raw**)

```json

```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Update Tuckshop
### Method: PUT
>```
>http://127.0.0.1:5000/api/tuck_shops/1
>```
### Body (**raw**)

```json
{
    "location_id" : "2",
    "tuck_shop_name" : "TVET Green Groceries Mini Mart"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Delete Tuckshop
### Method: DELETE
>```
>http://127.0.0.1:5000/api/tuck_shops/1
>```
### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
# 📁 Folder: Orders 


## End-point: Add Order
### Method: POST
>```
>http://127.0.0.1:5000/api/orders
>```
### Body (**raw**)

```json
{
    "order_id" : "4",
    "user_id" : "5",
    "product_id" : "4",
    "quantity" : "1",
    "total" : "2500",
    "order_date": "03/17/2024"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get Orders
### Method: GET
>```
>http://127.0.0.1:5000/api/orders
>```
### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Update Orders
### Method: PUT
>```
>http://127.0.0.1:5000/api/orders/1
>```
### Body (**raw**)

```json
{
    "user_id" : "5",
    "product_id" : "4",
    "quantity" : "1",
    "total" : "2500",
    "order_date": "3/17/2024"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Delete Orders
### Method: DELETE
>```
>http://127.0.0.1:5000/api/orders/1
>```
### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDY2OTM4NCwianRpIjoiNWYzYzE5NjctODAyNC00YWZjLWI1NjAtYjc3YzAxMzU5Yzc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTAsIm5iZiI6MTcxMDY2OTM4NCwiY3NyZiI6IjhlODhiOTgzLWZiMzQtNGM4YS1iNGQ5LTQ0MGYyODBlMWJmOCIsImV4cCI6MTcxMDc1NTc4NH0.yv2pQXvGWGt-t6RJtIuPc0wIC3Mt0AwzuP8K-KPNzWo|string|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
# 📁 Folder: Dashboard Analytics 


## End-point: Revenue
### Method: GET
>```
>http://127.0.0.1:5000/api/sales
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Total Orders
### Method: GET
>```
>http://127.0.0.1:5000/api/all_orders
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Total Products
### Method: GET
>```
>http://127.0.0.1:5000/api/total_products
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
