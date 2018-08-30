from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api
from json import dumps
import json

## Using code from https://github.com/narenaryan/Salary-API as starting template

app = Flask(__name__)
api = Api(app)

#app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
#app.config['CORS_HEADERS'] = 'Content-Type

CORS(app, origins="*")

class Hello_World(Resource):
    def get(self):
        # Return string Hello World
        return {'Hello':  'world!'}

class Hey_You(Resource):
    def get(self, user_name):
        # Return string Hello World
        return {'Hello':  user_name}

class postJsonHandler(Resource):
    def post(self):
        '''
        Json used for testing==
        { 
            "device":"TemperatureSensor", 
            "value":"20", 
            "timestamp":"25/01/2017 10:10:05" 
        }
        '''
        print (request.is_json)
        print (request.get_data())
        print (request.get_json(force=True))
        #content = request.get_json()
        #print (content['device'])
        return 'JSON posted'

@app.route('/')
def index():
    return "Welcome to my Python Server" 

api.add_resource(Hello_World, '/helloworld')
api.add_resource(postJsonHandler, '/json')
api.add_resource(Hey_You, '/hey/<string:user_name>')

if __name__ == '__main__':
     app.run(port='5002')