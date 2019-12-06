import models

from flask import request, jsonify, Blueprint
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user
from playhouse.shortcuts import model_to_dict

user = Blueprint('users', 'user')

@user.route('/register', methods=["POST"])
def register():
    
    #all the da
    payload = request.get_json()
    print(payload)
    payload['signupEmail'].lower()
    new_user_data = {
        "firstName": payload['signupFirstName'],
        "lastName": payload['signupLastName'],
        "username": payload['signupUserName'],
        "email": payload['signupEmail'],
        "location": payload['signupLocation'],
        "password": generate_password_hash(payload['signupPassword'])
    }
    print(new_user_data, "THIS IS THE NEW USER DATA")
    try:
        #finding if the user already exists
        models.User.get(models.User.email == payload['signupEmail'])
        return jsonify(data={}, status={"code": 401, "message": "A user with that name already exists"})
    except models.DoesNotExist:
        
        # payload['firstName'] = payload['signupFirstName']
        # payload['lastName'] = payload['signupLastName']
        # payload['username'] = paylod['signupUserName']
        # payload['email'] = payload['signupEmail']
        # payload['location'] = payload['signupLocation']
        # payload['password'] = generate_password_hash(payload['signupPassword'])
        user = models.User.create(**new_user_data)
        
        #login_user
        login_user(user)
        
        user_dict = model_to_dict(user)
        print(user_dict)
        print(type(user_dict))
        #deletes password- don't want it stored
        del user_dict['password']
        
        return jsonify(data=user_dict, status={"code": 201, "message": "Success"})
    
@user.route('/login', methods=["POST"])
def login():
    payload = request.get_json()
    print(payload, '<--- the payload')
    try:
        user = models.User.get(models.User.email== payload['loginEmail'])
        user_dict = model_to_dict(user)
        if(check_password_hash(user_dict['password'], payload['loginPassword'])):
            del user_dict['password']
            login_user(user)
            print(user, ' the user')
            return jsonify(data=user_dict, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Username or Password is incorrect"})
    
    @user.route('/logout', methods=["GET"])
    def logout():
        logout_user()
        return jsonify(status={"code": 200, "message": "User Logged Out"})
        