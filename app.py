import os
from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from resources.errors import errors

app = Flask(__name__)
api = Api(app, errors=errors)

app.config['MONGODB_SETTINGS'] = {
    'db': os.environ.get('MONGO_DB_NAME'),
    'host': os.environ.get('MONGO_HOST_NAME'),
    'port': int(os.environ.get('MONGO_PORT')),
    'username': os.environ.get('MONGO_USERNAME'),
    'password': os.environ.get('MONGO_PASSWORD'),
    'authentication_source': os.environ.get('MONGO_AUTHENTICATION_SOURCE')
}

initialize_db(app)
initialize_routes(api)

if __name__ == '__main__':
    app.run()