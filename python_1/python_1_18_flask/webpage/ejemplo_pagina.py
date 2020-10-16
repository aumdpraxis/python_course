from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    pagetitle = "HomePage"
    return render_template("index.html",
                            mytitle=pagetitle,
                            mycontent="Hello World")

@app.route("/Menu")
def menu():
    pagetitle = "HomePage"
    return render_template("Menu.html",
                            mytitle=pagetitle,
                            mycontent="Hello World")
@app.route("/about")
def about():
    pagetitle = "HomePage"
    return render_template("about.html",
                            mytitle=pagetitle,
                            mycontent="Hello World")

@app.route("/blog")
def blog():
    pagetitle = "HomePage"
    return render_template("blog.html",
                            mytitle=pagetitle,
                            mycontent="Hello World")

@app.route("/single-blog")
def single_blog():
    pagetitle = "HomePage"
    return render_template("single-blog.html",
                            mytitle=pagetitle,
                            mycontent="Hello World")


@app.route("/elements")
def elements():
    pagetitle = "HomePage"
    return render_template("elements.html",
                            mytitle=pagetitle,
                            mycontent="Hello World")

@app.route("/contact")
def contact():
    pagetitle = "HomePage"
    return render_template("contact.html",
                            mytitle=pagetitle,
                            mycontent="Hello World")

if __name__ == '__main__':
    app.run()