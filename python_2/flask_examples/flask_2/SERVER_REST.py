from flask import Flask
from flask_restful import Resource, Api, reqparse

from random import randint

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world',"hello_1":"from flask"}

class Rand(Resource):
    def __init__(self):
        self.parser= reqparse.RequestParser()
        self.parser.add_argument("a",type=int,help="a must be an integer")
        self.parser.add_argument("b",type=int,help="b must be an integer")
        super(Rand,self).__init__()

    def post(self,var_1,var_2):
        args= self.parser.parse_args()
        return {"RANDOM":randint(args.a,args.b)}

# api.add_resource(HelloWorld, '/')
api.add_resource(Rand,"/variable_1/<var_1>/variable_2/<var_2>")

if __name__ == '__main__':
    app.run(debug=True)