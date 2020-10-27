from flask import Flask, request, render_template
from flask.views import MethodView
from markupsafe import escape

app = Flask(__name__)

class Index(MethodView):
    def get(self):
        return render_template("index.html")
    def post(self):
        return "hello from post"

# @app.route('/',methods=["GET","POST"])
# def main():
#     return render_template("index.html")

@app.route('/about',methods=["GET","POST"])
def about():
    return "about"


app.add_url_rule('/',view_func=Index.as_view("Home"))

if __name__ == '__main__':
    app.run(debug=True)