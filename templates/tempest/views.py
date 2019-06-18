from flask import render_template, Blueprint
tempest_blueprint = Blueprint("tempest",__name__)

@tempest_blueprint.route('/')
@tempest_blueprint.route('/tempest')
def index():
    return render_template("index.html")