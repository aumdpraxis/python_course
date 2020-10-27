from flask import Flask, request, render_template
from flask.views import MethodView
from markupsafe import escape

from random import randint
import json

app = Flask(__name__)

class Index(MethodView):
    def get(self,a,b):
        return json.dumps( {"RANDOM":randint(a,b)} )
    def post(self):
        return "hello from post"


# app.add_url_rule('/',view_func=Index.as_view("Home"))
app.add_url_rule('/a/<int>/b/<int>',view_func=Index.as_view("Home"))

if __name__ == '__main__':
    app.run(debug=True)