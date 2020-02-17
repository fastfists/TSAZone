from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
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

@app.route('/design-brief')
def design_brief():
    return render_template("design_brief.html")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
