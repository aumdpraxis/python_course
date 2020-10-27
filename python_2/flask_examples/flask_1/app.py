from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def main():
    return render_template("index.html")

@app.route('/about',methods=["GET","POST"])
def about():
    return "about"


if __name__ == '__main__':
    app.run(debug=True)