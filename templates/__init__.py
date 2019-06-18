from flask import Flask

app = Flask(__name__,
    static_folder = './public',
    template_folder="./static")

from templates.tempest.views import tempest_blueprint

# register the blueprints
app.register_blueprint(tempest_blueprint)