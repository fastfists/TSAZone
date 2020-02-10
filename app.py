from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/officers')
def officers():
    return render_template("officers.html")

@app.route('/pathways')
def pathways():
    return render_template("pathways.html")

if __name__ == "__main__":
    app.run(debug=True)