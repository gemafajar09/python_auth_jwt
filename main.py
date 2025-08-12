from flask import Flask
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
import os
import datetime

from routes.auth_routes import auth_bp
from routes.user_routes import user_bp

load_dotenv()
app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'super-secret-key')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=1)

jwt = JWTManager(app)

app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
