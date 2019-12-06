from flask import request, jsonify, Blueprint
from playhouse.shortcuts import model_to_dict
from yelp.client import Client

api = Blueprint('apis', 'api')
client = Client(process.env.API_KEY)


@api.route('/', methods=["POST"])
def get_locations():
    print(process.env.API_KEY)
    