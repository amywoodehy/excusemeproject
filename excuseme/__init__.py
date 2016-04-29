import os
from flask import Flask
from flask.ext.mongoengine import MongoEngine


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'excusemeproject',
    'host': os.environ['EXCUSEMEPROJECT_MONGODB_1_PORT_27017_TCP_ADDR'],
    'port': 27017
}

db = MongoEngine(app)


if __name__ == '__main__':
    app.run(debug=True)
