from flask import Blueprint

brief = Blueprint('brief', __name__, url_prefix='/brief',
        template_folder='templates/brief')

def init_app(app):
    app.register_blueprint(brief)


@brief.route('/')
@brief.route('/home')
def design_brief():
    return render_template("design_brief.html")

