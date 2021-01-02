from flask import Flask, render_template, Blueprint, url_for, redirect
from dynamic_stream import init_app

tsa = Blueprint('tsa', __name__, url_prefix='/tsa',
        template_folder='templates/tsa/')

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return redirect(url_for("tsa.index"))

@tsa.route('/')
@tsa.route('/home')
def index():
    return render_template("tsa/home.html")

@tsa.route('/about')
def about():
    return render_template("about.html")

@tsa.route('/officers')
def officers():
    return render_template("officers.html")

@tsa.route('/pathways')
def pathways():
    return render_template("pathways.html")


init_app(app)
app.register_blueprint(tsa)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
