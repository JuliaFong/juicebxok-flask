from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

import models
import config


from resources.user import user

login_manager = LoginManager()

app = Flask(__name__)
# CORS(app)

app.secret_key = config.SECRET_KEY
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userId):
    try:
        return models.User.get(models.User.id == userId)
    except models.DoesNotExist:
        return None
    
@app.before_request
def before_request():
    """Connect to database before each request"""
    g.db = models.DATABASE
    g.db.connect()

app.after_request
def after_request(response):
    """Close database connection after each request."""
    g.db.close()
    return response

CORS(user, origin=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(user, url_prefix='/api/v1/users')

if __name__ == '__main__':
    models.initialize()
    app.run(debug=config.DEBUG, port=config.PORT)