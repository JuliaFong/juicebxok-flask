from flask import request, jsonify, Blueprint
from playhouse.shortcuts import model_to_dict

import config
import requests
import json

api = Blueprint('apis', 'api')

@api.route('/', methods=["POST"])
def get_dispensaries():
    payload = request.get_json()
    headers = {'Authorization': 'Bearer %s' % config.API_KEY}
    url="https://api.yelp.com/v3/businesses/search"
    params = {'term': 'dispensaries', 'location': payload['location']}
    req = requests.get(url, params = params, headers = headers)
    data = json.loads(req.text)
    return data