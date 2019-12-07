from flask import request, jsonify, Blueprint
from playhouse.shortcuts import model_to_dict
from yelp.client import Client

import config

api = Blueprint('apis', 'api')
client = Client(config.API_KEY)


@api.route('/', methods=["POST"])
def get_locations():
        