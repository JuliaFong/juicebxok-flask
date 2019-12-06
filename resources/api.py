from flask import request, jsonify, Blueprint
from playhouse.shortcuts import model_to_dict
from yelp.client import Client

api = Blueprint('apis', 'api')

@api.route('/', methods=["POST"])
def get_locations(): 
    